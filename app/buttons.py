import re

class Button(object):
	# Button object - usually has a "magnitude" ie: plus FIVE, minus EIGHT

	def __init__(self,magnitude):
		# General constructor

		try:
			self.magnitude = float(magnitude)
		except ValueError:
			print(f"Could not parse Button with magnitude {magnitude}.")
			exit()

	def press(self,current_value):
		return current_value+self.magnitude

	def __str__(self):
		return (self.__class__.__name__.replace("_button", " ") + str(self.magnitude))

	def __repr__(self):
		return str(self)


class Plus_button(Button):

	def __init__(self,m):
		super().__init__(m)


class Minus_button(Button):

	def __init__(self,m):
		super().__init__(m)

	def press(self,current_value):
		return current_value-self.magnitude


class Times_button(Button):

	def __init__(self,m):
		super().__init__(m)

	def press(self,current_value):
		return current_value * self.magnitude


class Divide_button(Button):
	# In this game you can't divide a float

	def __init__(self,m):
		super().__init__(m)

	def press(self,current_value):
		if(current_value != int(current_value)):
			raise ValueError("Error - float is indivisible")
		result = current_value / self.magnitude
		if(result == int(result)):
			return (int(result))
		return result


class Sign_Flip_button(Button):
	# In this game you can't do a sign-flip on a float

	def __init__(self):
		super().__init__(0)

	def press(self,current_value):

		if(current_value != int(current_value)):
			raise ValueError("Error - float is not flippable")

		return -current_value


class Chomp_button(Button): 
	# In this game you can't chomp on a float

	def __init__(self):
		super().__init__(0)

	def __str__(self):
		return (f"Button: Chomp" )

	def press(self,current_value):

		if(current_value != int(current_value)):
			raise ValueError("can't chomp a float bro")
		current_value = int(current_value)

		if(current_value < 0):
			raise ValueError("not sure if you can chomp a negative")

		if(current_value < 10):
			return 0


		return int(str(int(current_value))[:-1])


class Reverso_button(Button):
	# In this game you cannot reverse a float


	def __init__(self):

		super().__init__(0)

	def __str__(self):
		return (f"Button: Reverso" )


	def press(self,current_value):

		if(current_value != int(current_value)):
			raise ValueError("Error - float is not reversible")

		if(current_value < 0):
			return int((str(current_value)[1:])[::-1])*-1
		return int(str(current_value)[::-1])


class Replace_button(Button):

	def __init__(self, from_val, to_val):
		self.from_val = from_val
		self.to_val = to_val
		super().__init__(0)

	def __str__(self):
		return (f"Button: Replace {self.from_val}=>{self.to_val}" )

	def press(self,current_value):

		return int(str(current_value).replace(str(self.from_val), str(self.to_val)))


class Append_button(Button):
	# In this game you cannot append to a float

	def __init__(self,m):
		super().__init__(m)

	def press(self,current_value):
		if(current_value != int(current_value)):
			raise ValueError("Error - float is not appendable")

		return int(str(current_value)+str(int(self.magnitude)))


class Sum_button(Button):

	def __init__(self,*arg):
		super().__init__(0)

	def __str__(self):
		return (f"Button: Sum" )

	def __repr__(self):
		return str(self)

	def press(self,current_value):

		if(current_value != int(current_value)):
			raise ValueError("Error - float is not summable")

		return sum(int(digit) for digit in str(int(current_value)))


def string_to_button(raw):
	# General string->button parser

	if(re.search(r'^\+\d*$',raw)):
		return Plus_button(raw[1:])
	if(re.search(r'^\-\d*$',raw)):
		return Minus_button(raw[1:])
	if(re.search(r'^x\d*$',raw)):
		return Times_button(raw[1:])
	if(re.search(r'^\/\d*$',raw)):
		return Divide_button(raw[1:])
	if(re.search(r'^\+/\-$',raw)):
		return Sign_Flip_button()	
	if(re.search(r'^\<\<$',raw)):
		return Chomp_button()
	if(re.search(r'^[Rr]evers[eo]$',raw)):
		return Reverso_button()
	if(re.search(r'^(\d*)=>(\d*)$',raw)):
		p = re.compile(r'^(\d*)=>(\d*)$')
		m = p.match(raw)
		return Replace_button(m.group(1),m.group(2))
	if(re.search(r'^\d*$',raw)):
		return Append_button(raw)
	if(re.search(r'^SUM$',raw)):
		return Sum_button(raw)
	else:
		raise ValueError("Sorry",raw,"cannot be parsed.")
		exit()
