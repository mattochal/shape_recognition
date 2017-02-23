#!/usr/bin/env python

import sys
import getopt
import os
import glob
from PIL import Image, ImageFilter
from shutil import copyfile

def main(argv):
	options = "i:hx:y:t:"
	help_text = """ Help?
		-i input folder
		-o output file
		-t image type
		-x name of matrix X
		-y name of matrix y
		-h help
		"""

	# Defaults:
	input_folder = "./PiCam/Images/cylinders/contour_lines_25x25"
	output_file = "./NeuralNetworks/matrixCyln.m"
	image_type = "png"
	x_name = "Xcyln"
	y_name = "y"

	try:
		opts, args = getopt.getopt(argv,options)
	except getopt.GetoptError:
		print help_text
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print help_text
			sys.exit()
		elif opt is "-i":
			input_folder = arg
		elif opt is "-o":
			output_file = arg
		elif opt is "-t":
			image_type = arg
		elif opt is "-x":
			x_name = arg
		elif opt is "-y":
			y_name = arg

	X_line = x_name + " = ["

	if os.path.exists(output_file):
		os.remove(output_file)

	file = open(output_file, 'w')
	filenames = glob.glob(input_folder + "/*."+ image_type)

	for f in range(len(filenames)):
		image = Image.open(filenames[f])
		image = image.convert('LA')
		width, height = image.size

		for i in range(0, width):
			for j in range(0, height):
				if not (i == 0 and j == 0):
					X_line += ", "
				X_line += str(image.getpixel((i, j))[0])
		if f+1 < len(filenames):
			X_line += ";\n"
		file.write(X_line)
		X_line = ""

	file.write("];")

if __name__ == "__main__":
	main(sys.argv[1:])
