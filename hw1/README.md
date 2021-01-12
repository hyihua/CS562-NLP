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


