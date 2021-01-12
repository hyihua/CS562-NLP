#!/usr/bin/env python

import gzip
import argparse
from nltk.tokenize import sent_tokenize, word_tokenize
import string

punct_set = set(string.punctuation)
other_set = ['``', "''", '...', '--']
all_set = set.union(punct_set, other_set)

parser = argparse.ArgumentParser(description = 'Structuring the data -- split sentences & word tokenize')
parser.add_argument('-i', '--input')
args = parser.parse_args()
			
if __name__ == "__main__":
	with open(args.input, 'r') as f_in:
		text = f_in.read().replace('\n', ' ').upper()
	sentences = sent_tokenize(text)
	for sentence in sentences:
		tokens = word_tokenize(sentence)
		no_punct_toks = [t for t in tokens if t not in all_set]
		print(" ".join(no_punct_toks))
