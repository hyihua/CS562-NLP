# This write-up is for HW1.

## Part 1: Reading some data

1. Python file 'deserialization.py' is to decompress and serialize the XML files. 

	Firstly, download the data files by a command * wget -c -r -nd -k -L -p https://cslu.ohsu.edu/~bedricks/courses/cs662/resources/GW-cna_eng/ * in the * data/ * folder.
	Secondly, run the command * python deserialization.py -i data/*.xml.gz > deserialized.txt * in the * hw1/ * folder.

	The structure of * hw1/ * folder is as follows:

		hw1/
			data/
				cna_eng_199710.xml.gz
				cna_eng_199712.xml.gz
				...
			deserialization.py
			deserialized.txt
			first_100_lines.txt
			README.md

2. Run * head deserialized.txt -n 100 > first_100_lines.txt * in the * hw1/ * folder. The first 100 lines of its output is in the file * first_100_lines.txt *.

3. My approach: For a compressed XML file I firstly used python's * gzip * library to decompress it, then used a parser to remove blank lines, and finally used * xpath() * to obtain text of all paragraphs. All files are processed through a loop.

   Problem encountered: Initially I wanted to write the extracted text to a file, so the code implemented required the parser parameters to declare the output file. The error was encountered when I tried to write text to the file * code: f_out.write(text + '\n') * which was * Python typeerror: a bytes-like object is required, not ‘str’ *
   
   Solution: Instead of setting the parser parameter for output file, directly use command "< output_file_name.txt" to write text to the target file.
   
   
## Part 2: Structuring the data

	585064.

## Part 3: Counting and comparing

### Word counting & distribution

1. Number of unique types: 143294

2. Number of unigram tokens: 16676531

3. Plot: 

	![Plot](https://github.com/hyihua/CS562-NLP/blob/main/hw1/zipf_law.png)

4. The thirty most common words: ['THE', 'TO', 'OF', 'AND', 'IN', 'A', 'THAT', 'TAIWAN', "'S", 'SAID', 'FOR', 'ON', 'WILL', 'WITH', 'IS', 'AT', 'AS', 'BY', 'HE', 'BE', 'FROM', 'HAS', 'CHINA', 'WAS', 'AN', 'PERCENT', 'ITS', 'HAVE', 'IT', 'NOT']. We see there is a token "'S" in this list which is not a word. This situation occurs because function word_tokenize will separate contractions (somebody_name's, I'll) into different words. In this case, I will replace function word_tokenize with other functions which could separate contractions like I expect, such as function TweetTokenizer from nltk.tokenize.

5. Number of unique types (filtered text): 143156
   Number of unigram tokens (filtered text): 10295204

   Compared the above numbers with question 1, we could easily find that although the numbers of unique types have little difference, the number of unigram tokens after removing stopwords is a lot less than the original number.

6. The thirty most common words after removing stopwords: ['TAIWAN', "'S", 'SAID', 'CHINA', 'PERCENT', 'GOVERNMENT', 'ALSO', 'CHEN', 'PRESIDENT', 'YEAR', 'TAIPEI', 'NT', 'TWO', 'MAINLAND', 'PEOPLE', 'US', 'NEW', 'CHINESE', 'ACCORDING', 'PARTY', 'ECONOMIC', 'BILLION', 'FIRST', 'NATIONAL', 'ONE', 'FOREIGN', 'WOULD', 'INTERNATIONAL', 'OFFICIALS', 'CITY']. 
	 About the stopwords list, I think this list is pretty complete so far. The entries in the list are very common and I cannot come up with other words to add into the list.
	 To buiia a stopwords list, it is necessary to start from the dataset itself (corpus) that is used. It might be no hurt to try to use the default stopwords list first, and then the designer should select other words that have very high occurrence frequencies from related corpus.

### Word association metrics





