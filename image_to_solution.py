#!/usr/bin/env python3

from app import image_reader
from app import level

import argparse
import sys


def main():

	# get image location and any overwritten values
	args = parse_args()

	# read image
	ocr_information = image_reader.ImageReader(args)

	# create calculator object and solve it
	solved_calculator = level.Level(ocr_information)

	# print calculator object
	print(solved_calculator)


def parse_args():

	parser = argparse.ArgumentParser(description='pass in image with optional attribute override')
	parser.add_argument('--image', required=True, type=str, help='Location of image to read' )
	parser.add_argument('--start', type=int, help='Overwrite initial value' )
	parser.add_argument('--goal', type=int, help='Overwrite goal value' )
	parser.add_argument('--moves', type=int, help='Overwrite number of moves' )
	parser.add_argument('--buttons', nargs='*', help='Overwrite buttons: separate by space eg: 5 x3 +9 -20 +/- << Reverso 3=>5 SUM')
	args = parser.parse_args()

	return parser.parse_args()

if __name__ == "__main__":
	main()