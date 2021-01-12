#!/usr/bin/env python

import argparse
import collections
import numpy as np
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description = 'Word counting -- token & type')
parser.add_argument('-i', '--input')

args = parser.parse_args()

if __name__ == "__main__":
	with open(args.input, 'r') as f:
		text = f.read()
	result = collections.Counter(text.split())
	dict_token = dict(result)
	sort_token = sorted(dict_token.items(), key = lambda item: item[1], reverse = True)
	
	
	ranks = np.arange(1, len(sort_token) + 1)
	freq = [i[1] for i in sort_token]
	
	plt.loglog(ranks, freq, marker = '.')
	plt.title('Zipf plot for GW-cna_eng corpus')
	plt.grid(True)
	plt.xlabel('Rank of token')
	plt.ylabel('Frequence of token')
	
	plt.savefig('zipf_law.png')
	rank_30 = [i[0] for i in sort_token[:30]]
	print(rank_30)

	
