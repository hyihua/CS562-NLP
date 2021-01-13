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

2. Sample terminal output, showing perhaps the first 100 lines of its output

	 Run * head deserialized.txt -n 100 > first_100_lines.txt * in the * hw1/ * folder. The first 100 lines of its output is in the file * first_100_lines.txt *.

3. A sentence or two describing your approach and any bugs you encountered. 

	 My approach: For a compressed XML file I firstly used python's * gzip * library to decompress it, then used a parser to remove blank lines, and finally used * xpath() * to obtain text of all paragraphs. All files are processed through a loop.

   Problem encountered: Initially I wanted to write the extracted text to a file, so the code implemented required the parser parameters to declare the output file. The error was encountered when I tried to write text to the file * code: f_out.write(text + '\n') * which was * Python typeerror: a bytes-like object is required, not ‘str’ *
   
   Solution: Instead of setting the parser parameter for output file, directly use command "< output_file_name.txt" to write text to the target file.
   
   
## Part 2: Structuring the data

1. How many sentences are there in the CNA-GW corpus?

   585064.

## Part 3: Counting and comparing

### Word counting & distribution

1. How many unique types are present in this corpus? 

    143294.

2. How many unigram tokens?

   16676531

3. Produce a rank-frequency plot (similar to those seen on the Wikipedia page for Zipf’s Law) for this corpus. 

	![Plot](https://github.com/hyihua/CS562-NLP/blob/main/hw1/zipf_law.png)

4. What are the thirty most common words? Stop and reflect: Are there entries in this list that do not look like what you might consider to be a “word”? How might you adjust your processing pipeline from Part 2 to correct for this?

	 The thirty most common words: ['THE', 'TO', 'OF', 'AND', 'IN', 'A', 'THAT', 'TAIWAN', "'S", 'SAID', 'FOR', 'ON', 'WILL', 'WITH', 'IS', 'AT', 'AS', 'BY', 'HE', 'BE', 'FROM', 'HAS', 'CHINA', 'WAS', 'AN', 'PERCENT', 'ITS', 'HAVE', 'IT', 'NOT']. 

	 We see there is a token "'S" in this list which is not a word. This situation occurs because function word_tokenize will separate contractions (somebody_name's, I'll) into different words. In this case, I will replace function word_tokenize with other functions which could separate contractions like I expect, such as function TweetTokenizer from nltk.tokenize.

5. What happens to your type/token counts if you remove stopwords using nltk.corpora’s stopwords list? 

	 Number of unique types (filtered text): 143156
   Number of unigram tokens (filtered text): 10295204

   Compared the above numbers with question 1, we could easily find that although the numbers of unique types have little difference, the number of unigram tokens after removing stopwords is a lot less than the original number.

6. After removing stopwords, what are the thirty most common words? Look at the words contained in the nltk’s stopwords list. Does this list make sense? Are there entries that surprise you? Are there other words you would add? What might some important considerations be when generating a stopwords list?

	 The thirty most common words after removing stopwords: ['TAIWAN', "'S", 'SAID', 'CHINA', 'PERCENT', 'GOVERNMENT', 'ALSO', 'CHEN', 'PRESIDENT', 'YEAR', 'TAIPEI', 'NT', 'TWO', 'MAINLAND', 'PEOPLE', 'US', 'NEW', 'CHINESE', 'ACCORDING', 'PARTY', 'ECONOMIC', 'BILLION', 'FIRST', 'NATIONAL', 'ONE', 'FOREIGN', 'WOULD', 'INTERNATIONAL', 'OFFICIALS', 'CITY']. 

	 About the stopwords list, I think this list is pretty complete so far. The entries in the list are very common and I cannot come up with other words to add into the list.

	 To buiia a stopwords list, it is necessary to start from the dataset itself (corpus) that is used. It might be no hurt to try to use the default stopwords list first, and then the designer should select other words that have very high occurrence frequencies from related corpus.

### Word association metrics

1. Examine the 30 highest-PMI word pairs, along with their unigram and bigram frequencies. What do you notice?

	 These word pairs do not make sense. Although they have very high PMI, their bigram frequencies are very small. (all of them are 1 in this corpus.)

2. Experiment with a few different threshold values, and report on what you observe.

	 In this assignment, I use several thresholds (thresholds = [30, 70, 100, 130, 170, 200, 230, 270, 300, 400]). From the output result, we could easily find that the bigger the threshold given a threshold value between [1, 100]














