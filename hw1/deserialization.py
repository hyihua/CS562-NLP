#!/usr/bin/env python

import gzip
from lxml import etree
import argparse


parser = argparse.ArgumentParser(description = 'Decopress XML files and serialize these files')
parser.add_argument('-i', '--input', nargs = '+')

args = parser.parse_args()

if __name__ == "__main__":
	for xml_file in args.input:
		with open(xml_file, 'rb') as f_in:
			docs = gzip.decompress(f_in.read())
			
		parser = etree.XMLParser(remove_blank_text = True)
		xml_str = etree.XML(docs, parser = parser)
		texts = xml_str.xpath('//DOC[@type="story"]/TEXT/P/text()')

		for text in texts:
			print(text)

		


