#!/bin/usr/python3

# Script by Mike Rosinsky

import sys

key = ""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if __name__=="__main__":

	out_string = ""

	if (len(sys.argv)) != 3:
		print("Usage: python3 vignere_decoder.py filename key")
		exit(0)
	else:

		key = sys.argv[2]

		print("Decoding file '" + sys.argv[1] + "' with key '" + sys.argv[2] + "':\n")

		try:
			with open(sys.argv[1]) as fh:
				lines = fh.readlines()
		except:
			print("No file named '" + sys.argv[1] + "'")
			exit(0)

		for line in lines:
			line = line.replace(" ", "")
			line = line.replace("\n", "")
			for index in range(len(line)):
				c = alphabet[(alphabet.index(line[index]) - alphabet.index(key[index % len(key)])) % 26]
				out_string += c

	print(out_string)

