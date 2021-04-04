#!/usr/bin/python


import sys
import math
from PIL import Image
from PIL import ImageOps
import os
from os import path

# FORMATTED HEX OUTPUT FUNCTIONS -------------------------------------------

# Some globals (yeah, I know) used by the outputHex() function
hexLimit   = 0 # Total number of elements in array being printed
hexCounter = 0 # Current array element number, 0 to hexLimit-1
hexDigits  = 0 # Number of digits (after 0x) in array elements
hexColumns = 0 # Max number of elements to output before line wrap
hexColumn  = 0 # Current column number, 0 to hexColumns-1

# Initialize counters, etc. for outputHex() function below
def hexReset(count, columns):
	global hexLimit, hexCounter, hexColumns, hexColumn
	hexLimit   = count
	hexCounter = 0
	hexColumns = columns
	hexColumn  = columns

# Write hex digit (with some formatting for C array) to stdout
def rgb2hex(r, g, b):
	global hexLimit, hexCounter, hexDigits, hexColumns, hexColumn
	if hexCounter > 0:
		sys.stdout.write(",")                  # Comma-delimit prior item
		if hexColumn < (hexColumns - 1):       # If not last item on line,
			sys.stdout.write(" ")              # append space after comma
	hexColumn += 1                             # Increment column number
	if hexColumn >= hexColumns:                # Max column exceeded?
		sys.stdout.write("\n  ")               # Line wrap, indent
		hexColumn = 0						   # Reset column number
	sys.stdout.write("0x"+"{:02x}{:02x}{:02x}".format(r, g, b))
	hexCounter += 1                            # Increment item counter
	if hexCounter >= hexLimit: print("};\n"); # Cap off table


# IMAGE CONVERSION ---------------------------------------------------------
def convertImage():
	try:
		filename   = sys.argv[1]
		prefix     = path.splitext(path.split(filename)[1])[0]

		img        = Image.open(filename)
		pixelCount = img.size[0] * img.size[1]

		pixels     = img.load()

		hexReset(pixelCount, 9)

		sys.stderr.write("Image OK\n")

		sys.stdout.write(
		  "#define ANIM_LENGTH " + str(img.size[0]) + "\n\n"
		  "const uint32_t PROGMEM %sPixelData[] = {\n" %
		  (prefix))

		for x in range(img.size[0]):
			for y in range(img.size[1]):
				p = pixels[x, y]
				r = p[0]
				g = p[1]
				b = p[2]

				rgb2hex(r, g, b)

	except Exception as e:
		logging.Exception("Unexpected exception! %s",e)

# MAIN ---------------------------------------------------------------------
convertImage()
