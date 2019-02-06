from itertools import product 
from app.buttons import *


class Level(object):
	# Object to hold and solve a calculator level


	def __init__(self,level_data):
		# General constructor

		self.goal 			= level_data.goal
		self.moves 			= level_data.moves
		self.start 			= level_data.start
		self.buttons 		= [string_to_button(x) for x in level_data.buttons]
		self.search_space 	= len(self.buttons) ** self.moves
		self.solution 		= self.compute_every_combination()


	def __str__(self):
		# string representation

		return f"""
		START:		{self.start}
		GOAL:		{self.goal}
		MOVES:		{self.moves}
		BUTTONS:	{self.buttons}
		SEARCH SPACE:	{self.search_space} Combinations

		SOLUTION:	{self.solution}

		"""

	def compute_combination(self, series):
		# presses a series of buttons in order and returns the result

		current_val = self.start
		for button in series:
			try:
				current_val = button.press(current_val)
			except ValueError:
				continue
		return current_val


	def compute_every_combination(self):
		# Generate all possible series of button presses for a given set of moves
		# and try each one until we find a solution.
		# Complexity here is O(buttons)^moves
		# Luckily for us, number of moves is pretty consistently small ( ~5 )

		print("Solving...")
		possible_orders = product(self.buttons, repeat=self.moves)
		for p in possible_orders:
			ans = self.compute_combination(p)
			if(ans == self.goal):
				return p
		return None

