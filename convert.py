#!/usr/bin/env python

import sys
import getopt
import os
import glob
from PIL import Image, ImageFilter
from shutil import copyfile

def main(argv):
	options = "i:t:r:dh"
	help_text = """ Help?
		-i input folder
		-t image type
		-f filter (e.g. "bw;cl;c")
			bw - black and white
			cl - contour lines
			hc = high contrast
		-W width of trasformed image
		-H height of trasformed image
		-h help
		"""

	# Defaults:
	input_folder = "./PiCam/Images/balls"
	image_type = "jpg"
	filters = [black_and_white, contour_lines, high_contrast]
	height = 25
	width = 25

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
		elif opt is "-t":
			image_type = arg
		elif opt is "-f":
			f = arg.split[";"]
			filters = []
			if "bw" in f:
				filters.append(black_and_white)
			if "cl" in f:
				filters.append(contour_lines)
			if "hc" in f: 
				filters.append(high_contrast)
		elif opt is "-d":
			delete_flag = True
		elif opt is "-H":
			height = arg
		elif opt is "-W":
			width = arg

	suffix = "_" + str(width) + "x" + str(height)

	for filt in filters:
		if not os.path.exists(input_folder + "/" + filt.__name__ + suffix):
			os.makedirs(input_folder + "/"+ filt.__name__ + suffix)

	for filt in filters:
		for filename in glob.glob(input_folder + "/*."+ image_type):
			image = Image.open(filename)
			image = image.resize((width, height), Image.ANTIALIAS)
			image = filt(image)
			image.save(input_folder + "/" + filt.__name__ + suffix + "/" + os.path.basename(filename).split(".")[0] + ".png")

def black_and_white(img):
	return img.convert('LA')

def contour_lines(img):
	img = img.convert('LA').filter(ImageFilter.CONTOUR)
	return img

def high_contrast(img):
	img = img.convert("L")
	img = img.point(lambda x: (x/int(255/16)*(255/14)))
	return img

if __name__ == "__main__":
	main(sys.argv[1:])
