#!/usr/bin/env python

import sys
import getopt
import os
import glob
from PIL import Image, ImageFilter
from shutil import copyfile

def main(argv):
	options = "i:o:r:dh"
	help_text = """ Help?
		-i images folder
		-o output folder
		-t image type
		-r width:height ratio (e.g. 1:1)
		-d delete non matching
		"""

	# Defaults:
	input_folder = "./PiCam/Images/cylinders/high_contrast_25x25"
	output_folder = "./PiCam/Images/cylinders/high_contrast_25x25/delete"
	image_type = "jpg"
	ratio = 1.0 # w/h
	delete_flag = False

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
			output_folder = arg
		elif opt is "-t":
			image_type = arg
		elif opt is "-r":
			width = arg.split[":"][0]
			height = arg.split[":"][1]
			ratio = width/height*1.0
		elif opt is "-d":
			delete_flag = True

	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	for filename in glob.glob(input_folder + "/*."+ image_type):
		image = Image.open(filename)
		width, height = image.size
		if (width*1.0/height) != ratio:
			#image = image.thumbnail((width, width), Image.ANTIALIAS)
			image.save(output_folder + "/" + os.path.basename(filename))
			os.remove(filename)

if __name__ == "__main__":
	main(sys.argv[1:])








