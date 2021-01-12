#!/usr/bin/env python

import argparse
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = [word.upper() for word in stopwords.words('english')]

parser = argparse.ArgumentParser(description = 'Word counting -- remove stopwords')
parser.add_argument('-i', '--input')

args = parser.parse_args()

if __name__ == "__main__":
	with open(args.input, 'r') as f:
		text = f.read()
	tokens = word_tokenize(text)
	filtered = [word for word in tokens if word not in stop_words]
	print("Number of unique types (filtered text): " + str(len(set(filtered))))
	print('Number of unigram tokens (filtered text): ' + str(len(filtered)))
	
	result = FreqDist(filtered)
	dict_token = dict(result)
	sort_token = sorted(dict_token.items(), key = lambda item: item[1], reverse = True)
	rank_30 = [i[0] for i in sort_token[:30]]
	print(rank_30)
