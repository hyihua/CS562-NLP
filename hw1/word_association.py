#!/usr/bin/env python

import gzip
import argparse
from nltk.tokenize import word_tokenize
from nltk import FreqDist
import nltk
from nltk.corpus import stopwords
	
def all_u_prob(u_freqdist, length):
	u_prob_dict = {}
	for word in u_freqdist.keys():
		u_prob_dict[word] = u_freqdist[word] / length
	return u_prob_dict
	
def all_b_prob(b_freqdist, length):
	b_prob_dict = {}
	for b in b_freqdist.keys():
		b_prob_dict[b] = b_freqdist[b] / length
	return b_prob_dict
	
def all_pmi(b_freqdist, bi_length, u_freqdist, uni_length):
	pmi_dict = {}
	all_b_list = all_b_prob(b_freqdist, bi_length)
	all_u_list = all_u_prob(u_freqdist, uni_length)
	for b in all_b_list.keys():
		word1_word2_p = all_b_list[b]
		word1_p = all_u_list[b[0]]
		word2_p = all_u_list[b[0]]
		pmi_dict[b] = word1_word2_p / (word1_p * word2_p)
	return pmi_dict
	
	
if __name__ == "__main__":
	stop_words = [word.upper() for word in stopwords.words('english')]
	parser = argparse.ArgumentParser(description = 'Structuring the data -- split sentences & word tokenize')
	parser.add_argument('-i', '--input')
	args = parser.parse_args()
	with open(args.input, 'r') as f_in:
		text = f_in.read()
	tokens = word_tokenize(text)
	
	u_tokens = [word for word in tokens if word not in stop_words]
	u_freq = dict(FreqDist(u_tokens))

	b_tokens = nltk.bigrams(u_tokens)
	b_freq = dict(FreqDist(b_tokens))
	
	print(len(u_tokens), len(list(nltk.bigrams(u_tokens))))
	print('The 30 highest-PMI word pairs, along with their unigram and bigram frequencies. ')
	

	result_pmi = all_pmi(b_freq, len(list(nltk.bigrams(u_tokens))), u_freq, len(u_tokens))
	sort_pmi = sorted(result_pmi.items(), key = lambda item: item[1], reverse = True)
	pmi_30 = sort_pmi[:30]
	
	for pmi in pmi_30:
		print("Word pairs: ", pmi[0], ', PMI: ', pmi[1], ', Unigram frequency: ', str(u_freq[pmi[0][0]]), str(u_freq[pmi[0][1]]), ', Bigram frequencies: ', str(b_freq[pmi[0]]))
		
	thresholds = [30, 70, 100, 130, 170, 200, 230, 270, 300, 400]
	for t in thresholds:
		print('The 10 hightest-PMI word pairs if bigram frequency is higher than ', str(t))
		count = 0
		for p in sort_pmi:
			if count > 10:
				break
			if b_freq[p[0]] > t:
				print("Word pairs: ", p[0], ', PMI: ', p[1], ', Unigram frequency: ', str(u_freq[p[0][0]]), str(u_freq[p[0][1]]), ', Bigram frequencies: ', str(b_freq[p[0]]))
				count += 1
	print("Take 'NEW YORK' as an example: ")
	test_tuple = ('NEW', 'YORK')
	dict_pmi = dict(sort_pmi)
	print('PMI: ', str(dict_pmi[test_tuple]), ', Unigram frequency: ', str(u_freq['NEW']), str(u_freq['YORK']), ', Bigram frequencies: ', str(b_freq[test_tuple]))
	
			
			
			
		
	
	



