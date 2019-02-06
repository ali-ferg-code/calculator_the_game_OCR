import unittest
import sys, os
sys.path.append('test/../') 


from app.level import *
from app.buttons import *


class MockLevelData(object):

	def __init__(self,goal,moves,start,buttons=[]):
		self.goal 			= goal
		self.moves 			= moves
		self.start 			= start
		self.buttons 		= buttons


class TestLevel(unittest.TestCase):


	def test_solution_exists(self):

		level_one = Level(MockLevelData(1,1,0))

		button_append_one = Append_button(1)
		level_one.buttons = [button_append_one]
		level_one_solution = level_one.compute_every_combination()

		self.assertEqual(list(level_one_solution), [button_append_one])


	def test_compute_series(self):
		data = MockLevelData(5,5,0)
		l = Level(data)
		button = Plus_button(1)
		l.buttons = [button]

		self.assertEqual(list(l.compute_every_combination()), [button]*5)


	def test_harder_series(self):
		data = MockLevelData(500,10,5,["+5","x10","x5","-10"])
		hard_level = Level(data)
		print(hard_level.solution)
		self.assertTrue(hard_level.solution)


	def test_search_space(self):
		data = MockLevelData(4,10,3,["+1","+3"])
		l = Level(data)
		self.assertEqual(l.search_space,1024)


if __name__ == '__main__':
	unittest.main()