from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw
import cv2
import pytesseract
import os,sys


class ImageReader(object):
	# Object to store text info for a given calculator image

	def __init__(self,args):
		# General constructor

		self.image 	= self.preprocess(args.image)
		self.screen_width = self.image.size[0]
		self.screen_height = self.image.size[1]

		# If an attribute has been overridden by cmd line arguments bypass OCR.
		if(args.buttons is not None):
			self.buttons = args.buttons
			print(f"Overwrote the following buttons: {args.buttons}")
		else:
			self.buttons	= self.get_button_values(self.image)
			print(f"Detected the following buttons: {self.buttons}")

		if(args.moves is not None):
			self.moves = args.moves
			print(f"Overwrote number of moves:\t {args.moves}")
		else:
			self.moves = int(self.get_moves(self.image))
			print(f"Detected number of moves:\t {self.moves}")

		if(args.goal is not None):
			self.goal = args.goal
			print(f"Overwrote goal number:\t\t {args.goal}")
		else:
			self.goal = int(self.get_goal(self.image))
			print(f"Detected goal number:\t\t {self.goal}")

		if(args.start is not None):
			self.start = args.start
			print(f"Overwrote starting number:\t {args.start}")
		else:
			self.start = int(self.get_start_value(self.image))
			print(f"Detected starting number:\t {self.start}")


	def get_button_values(self,full_img):
		# Return a list of button text for the 5 buttons

		buttons = []

		for y in range(0,3):
			for x in range(1,3):
				if((x,y) == (2,0)): # don't care about the CLR button
					continue
				coords = self.get_button_coordinates(x,y) 
				b = full_img.crop(coords)
				text = self.read_button(b)
				if(text): # buttons may be blank, in which case we ignore
					buttons.append(text)
		return buttons


	def get_moves(self,full_img):
		# For a given image, returns the number of moves allowed

		coords = (self.screen_width/1.878,self.screen_height/7.837,self.screen_width/1.693,self.screen_height/6.154)
		b = full_img.crop(coords)
		return self.read_number(b)


	def get_goal(self,full_img):
		# For a given image, returns the goal answer

		coords = (self.screen_width/1.25,self.screen_height/7.837,self.screen_width/1.140,self.screen_height/6.019)
		b = full_img.crop(coords)
		return self.read_number(b)


	def get_start_value(self,full_img):
		# For a given image, returns the start number

		coords = (self.screen_width/6.75,self.screen_height/5.189,self.screen_width/1.125,self.screen_height/3.122)
		b = full_img.crop(coords)
		b = ImageOps.invert(b)
		return self.read_number(b)


	def preprocess(self,path,blur=5):
		# The first step of the OCR process is to clean up the image:
		# We first load the image and add a small blur.
		# Then we binarize the image into black and white ( inverted )

		if(not os.path.isfile(path)):
			print(f"Error - could not find file {path}")
			raise FileNotFoundError

		print(f"Reading image path: {path}")
		img = cv2.imread(path, 0)
		if(blur > 0):
			blur = cv2.GaussianBlur(img,(blur,blur),0)
		ret2, thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
		return Image.fromarray(thresh)


	def read_button(self,button_image):
		# Attempt to read a cropped image using a restricted set of characters that we are expecting from buttons

		return pytesseract.image_to_string(button_image,lang="eng", config="--psm 6 -c  tessedit_char_whitelist=+/x-<0123456789SUMRrevs=>  ")


	def read_number(self,button_image):
		# Attempt to read a cropped image that we expect to contain only integers

		return pytesseract.image_to_string(button_image,lang="eng", config="--psm 6 -c  tessedit_char_whitelist=0123456789")


	def get_button_coordinates(self,col,row):
		# Translates button position to pixel coordinates of a button

		button_width  = round(self.screen_width/3.272)
		button_height = round(self.screen_height/7.111)

		left_margin = round(self.screen_width/13.5)
		top_margin = round(self.screen_height/2.157)

		text_width = self.screen_width/4
		text_height = self.screen_height/11.294

		top_left_x = left_margin + ( col  * button_width  )
		top_left_y = top_margin  + ( row  * button_height )

		bottom_right_x = top_left_x + text_width
		bottom_right_y = top_left_y + text_height

		return(top_left_x,top_left_y,bottom_right_x,bottom_right_y)
