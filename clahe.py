#!/usr/bin/env python
## @file
# @title Contrast Limited Adaptive Histogram Equalization
# @brief Process input using CLAHE to create output
# @author Ernest Skrzypczyk
# @email emeres.code@onet.eu
# @date 01.07.2017
# @version 0.4.1
# @licence GPLv3
#

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os.path
import argparse

def warn(text):
	print('\033[38;5;226m' + text)

def error(text, errorcode):
	print('\033[38;5;196m' + text)
	exit(errorcode)

#%% Check if run as a script or imported as a library
if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog = os.path.basename(__file__))
	## @todo Add epilog = 'description'
	parser = argparse.ArgumentParser(description = 'Perform basic image processing on input by using CLAHE algorithm to generate output.')
	parser.add_argument('-i', '--input', dest = 'filenameInput', type = str, default = 'input.png', help = 'Input image') # Option for input image
	parser.add_argument('-o', '--output', dest = 'filenameOutput', type = str, default = 'output.png', help = 'Output image') # Option for output image
	parser.add_argument('-c', '--clipping-limit', dest = 'clipLimit', type = float, default = 2.0, help = 'Clipping limit') # Option for clipping limit
	parser.add_argument('-sv', '--save-images', dest = 'saveImages', default = True, action = 'store_true', help = 'Save images') # Option for saving processed images
	parser.add_argument('-si', '--show-images', dest = 'showImages', type = int, default = 0, help = 'Show images', metavar = 'SHOWIMAGES <0-b2><!0>') # Option for displaying images
	parser.add_argument('-t', '--tile-size', dest = 'tileSize', type = int, default = (8, 8), nargs = 2, help = 'Tile size', metavar = 'TILESIZE !8x8') # Option for tile size

	args = parser.parse_args() #Parse arguments and file mask from command line

	# Configuration from command line
	filenameInput = str(args.filenameInput)
	filenameOutput = str(args.filenameOutput)
	saveImages = bool(args.saveImages)
	showImages = int(args.showImages)
	clipLimit = float(args.clipLimit)
	tileSize = tuple(args.tileSize)

else:
	error('No implementation of class or library yet', 127)

if os.path.isfile(filenameInput):
	Input = cv2.imread(filenameInput, cv2.IMREAD_COLOR)
	Input = cv2.cvtColor(Input, cv2.COLOR_BGR2RGB)
else:
	error('No input file:\t' + filenameInput, 1)

# @reference https://stackoverflow.com/questions/19363293/whats-the-fastest-way-to-increase-color-image-contrast-with-opencv-in-python-c
# CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit = clipLimit, tileGridSize = tileSize)

# Convert color space from RGB to LAB
lab = cv2.cvtColor(Input, cv2.COLOR_RGB2LAB)

# Split onto 3 different channels
l, a, b = cv2.split(lab)

# Apply CLAHE to the L-channel
l = clahe.apply(l)

# Merge channels
lab = cv2.merge((l, a, b))

# Convert color space from LAB to RGB
Output = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

# Save images
if saveImages:
	cv2.imwrite(filenameOutput, Output)

# Display comparison
if showImages > 0:
	plt.subplot(121)
	plt.imshow(Input)
	plt.title('Input')
	plt.xticks([])
	plt.yticks([])

	plt.subplot(122)
	plt.imshow(Output)
	plt.title('Output')
	plt.xticks([])
	plt.yticks([])

	plt.show()
