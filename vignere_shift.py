#!/usr/bin/python3

# Script by Mike Rosinsky

import sys

if __name__=="__main__":

	key_length = 4
	shift = 0
	out_string = ""

	if len(sys.argv) > 4:
		print("Usage: python3 vignere_shift.py filename key_length [shift]")
		exit(0)
	else:

		try:
			key_length = int(sys.argv[2])
			if len(sys.argv) == 4:
				shift = int(sys.argv[3])
		except:
			print("key_length and [shift] must be an int")
			exit(0)

		try:
			with open(sys.argv[1]) as fh:
				lines = fh.readlines()
		except:
			print("No file named '" + sys.argv[1] + "'")
			exit(0)

		for line in lines:
			line = line.replace(" ", "")
			line = line.replace("\n", "")
			for index in range(shift, len(line)):
				if index % key_length == shift:
					out_string += line[index]

		print(out_string)