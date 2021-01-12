#!/usr/bin/env python

import argparse
from nltk.tokenize import word_tokenize

parser = argparse.ArgumentParser(description = 'Word counting -- token & type')
parser.add_argument('-i', '--input')

args = parser.parse_args()

if __name__ == "__main__":
	with open(args.input, 'r') as f:
		text = f.read()
	tokens = word_tokenize(text)
	print("Number of unique types: " + str(len(set(tokens))))
	print('Number of unigram tokens: ' + str(len(tokens)))
	
	
	

