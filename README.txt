1. File List
----------------------
readme.txt (this file)
plagiarism.py
inputfile1.txt
inputfile2.txt
syns.txt


2. Description
----------------------
plagiarism.py program is written to perform plagiarism detection using a N-tuple comparison algorithm allowing for synonyms in the text.

----------------------
Command Line Arguments
----------------------
usage: myprog synonym_file input_file1 input_file1 [tuplesize]
tuplesize(optional)- Specify the size of the tuple, must be a positive integer
Example: python plagiarism.py syns.txt inputfile1.txt inputfile2.txt 3


3.Algorithm Design
----------------------
Firstly, the program uses a dictionary to store line number for all the word in synonyms file. Then, the program read inputfile1 and save all the N-tuples in inputfile1 to another dictionary. Also for every N-tuple in the inputfile1, we generate synonym N-tuples using synonym file and save them to the dictionary. At last, we read inputfile2 and check how many N-tuple in it matches the one in the inputfile1’s dictionary.

This algorithm is made based on following assumptions: 
1. If the tuple size is larger than the number of words in inputfile1 or inputfile2, it treats it as wrong input and prints error message.
2. Every word in inputfile1 and inputefile2 are divided by single space or \n.
3. Words divided by \n are considered different sentences and therefore words in different sentence can’t form valid tuple.tuple For example, if the input file is following:
	file1.txt:
		go for a \n
		run
In this case, "for a run" can't be count as a tuple of size 3 since they are in different sentences.
4. Based on assumption 3, if no N-tuple found in inputfile1 or inputfile2, it treats as wrong input and print error message