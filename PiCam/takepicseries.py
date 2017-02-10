#!/usr/bin/env python

from picamera import PiCamera
from time import sleep
import sys
import getopt

def main(argv):
	options = "n:d:H:W:o:gh"
	help_text = """ Help?
		-n number of pictures
		-d delay in sec between pictures
		-h height of image
		-w width of image
		-g gray scale
		-o output folder
		"""

	# Defaults:
	n = 10
	delay = 0.5
	height = 640
	width = 480
	output_folder = "/home/pi/Desktop/images/"
	grayscale_flag = False
	mode = 'rgb'

	try:
		opts, args = getopt.getopt(argv,options)
	except getopt.GetoptError:
		print help_text
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print help_text
			sys.exit()
		elif opt is "-n":
			n = arg
		elif opt is "-d":
			delay = arg
		elif opt is "-h":
			height = arg
		elif opt is "-w":
			width = arg
		elif opt is "-g":
			grayscale_flag = True
			mode = 'yuv'
		elif opt is "-o":
			output_folder = arg


	camera = PiCamera()
	camera.resolution = (width, height)


	print("Ready?")
	for i in range(3,0,-1):
		sleep(1)
		print i
	sleep(0.9)
	print ("Go!")
	sleep(0.1)

	count = 0
	while count < 10:
		print ("Taking picture " + str(count))
		camera.capture( output_folder + '/img'+str(count)+'.jpg', mode)
		sleep(delay)
		count += 1

if __name__ == "__main__":
   main(sys.argv[1:])