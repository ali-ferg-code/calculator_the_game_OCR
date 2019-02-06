import unittest
import sys, os
sys.path.append('test/../') 


from app.buttons import *

class TestButtons(unittest.TestCase):

	def test_button_default_adds(self):
		b = Button(5)
		current_value = 12 
		self.assertEqual(b.press(current_value),17)

	def test_default_button_float(self):
		b = Button(5.234)
		current_value = 2.744
		ans = 7.978
		self.assertEqual(b.press(current_value),ans)

	def test_default_button_nan(self):
		with self.assertRaises(SystemExit):
			b = Button("badnumber")

	def test_plus_button_adds(self):
		b = Plus_button(23)
		current_value = 65
		self.assertEqual(b.press(current_value),88)
		
	def test_plus_button_add_negative(self):
		b = Plus_button(263)
		current_value = -65.5
		self.assertEqual(b.press(current_value),197.5)

	def test_minus_button_subtracts(self):
		b = Minus_button(40)
		current_value = 73
		self.assertEqual(b.press(current_value),33)

	def test_plus_button_is_negative_minus_button(self):
		button_magnitude = 25
		b_minus = Minus_button(button_magnitude)
		b_plus  = Plus_button(-button_magnitude)
		current_value = 55
		self.assertEqual(b_minus.press(current_value),30)
		self.assertEqual(b_plus.press(current_value),b_minus.press(current_value))

	def test_time_button(self):
		b = Times_button(9)
		current_value = 7
		self.assertEqual(b.press(current_value),63)

	def test_time_button_float(self):
		b = Times_button(4.5)
		current_value = 2.75
		ans = b.press(current_value)
		self.assertEqual(ans,12.375)

	def test_divide_factor(self):
		b = Divide_button(4)
		current_value = 20
		ans = b.press(current_value)
		self.assertEqual(ans,5)

	def test_divide_non_factor(self):
		b = Divide_button(4)
		current_value = 17
		ans = b.press(current_value)
		self.assertEqual(ans,4.25)

	def test_divide_float_numerator(self):
		b = Divide_button(4.12)
		current_value = 6
		ans = b.press(current_value)
		self.assertEqual(round(ans,4),round(1.45631,4))

	def test_divide_float_denominator(self):
		b = Divide_button(2)
		current_value = 6.42
		with self.assertRaises(ValueError):
			ans = b.press(current_value)

	def test_divide_by_zero(self):
		b = Divide_button(0)
		current_value = 6
		with self.assertRaises(ZeroDivisionError):
			ans = b.press(current_value)

	def test_sign_flip_integer(self):
		b =Sign_Flip_button()
		self.assertEqual(b.press(4),-4)
		self.assertEqual(b.press(-3),3)
		self.assertEqual(b.press(-4),4)
		self.assertEqual(b.press(0),0)

	def test_sign_flip_float(self):
		b =Sign_Flip_button()
		with self.assertRaises(ValueError):
			b.press(4.3)


	def test_chomp_int(self):
		b =Chomp_button()
		self.assertEqual(b.press(321),32)

	def test_chomp_small(self):
		b =Chomp_button()
		self.assertEqual(b.press(3),0)

	def test_chomp_negative(self):
		b =Chomp_button()
		with self.assertRaises(ValueError):
			b.press(4.3)

	def test_append_on_zero(self):
		b =Append_button(1)
		self.assertEqual(b.press(0),1)

	def test_append_on_natural_number(self):
		b =Append_button(7)
		self.assertEqual(b.press(35),357)

	def test_append_on_float(self):
		b =Append_button(4)
		with self.assertRaises(ValueError):
			b.press(4.53)

	def test_append_on_negative_number(self):
		b =Append_button(3)
		self.assertEqual(b.press(-35),-353)



if __name__ == '__main__':
	unittest.main()