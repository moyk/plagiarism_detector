#!/usr/bin/python2
import sys
import collections

# @description: this function helps reading inputfile and store data in 2d list
# @params: filename  - string
# @return: (dataList, wordCount) - tuple
#		   dataList  - List[List] 
#		   wordCount - integer
def readInputFile(filename):
	inputFileData=[]  #2d list used to store data
	wordCount=0   #how many word are in thie file
	with open(filename, "r") as file:
		for line in file:
			lineData=[]
			for eachword in line.rstrip('\n').split(" "):
				lineData.append(eachword)
				wordCount+=1
			inputFileData.append(lineData)
	return (inputFileData,wordCount)



# @description: this function helps checking if the tupleSize is larger than the number of words in a file and print error message
# @params: wordCount - integer
#		    tupleSize - integer
# @return: if the tupleSize is smaller than wordCount, void return 
#		    else print error message
def checkWordCount(wordCount,tupleSize):
	if wordCount<tupleSize:
		print "Please enter a smaller tuple size, current tuple size exceeds your inputfile1 size "
		#exit()



# @description: this function helps hashing tuple to a string, and use this string as key for the tupleDictionary
# @params: tuple - list of string
# @return:  string
# @example: input ['go', 'for', 'a'], output 'go,for,a'
def generateTupleKey(tuple):
	return ",".join(tuple)


# @description: this function helps generating tuples using sysnDictionary and add them to tupleDictionary
# @params: tuple - list of string
#			synDictionary - dictionary
#			synData   - List[List]
#			tupleDictionary  -dictionary
# @return:  tupleDictionary - dictionary
# @example: if given input tuple=['a', 'jog'],  synDictionary={'jog':0}, synData=[['jog','run','sprint'], tupleDictionary={}
#			it will return tupleDictionary={'a,jog':1, 'a,run':1, 'a,sprint':1}
def generateSynTuples(tuple, synDictionary,synData,tupleDictionary):
	for index in range(len(tuple)):
		eachWord=tuple[index]
		#if this word has synonyms
		if synDictionary[eachWord]!=-1:
			lineIndex=synDictionary[eachWord]
			synGroup= synData[lineIndex]
			#replace this word by its synonyms to for new tuples
			for eachSyn in synGroup:
				newTuple=tuple[:index]+ [eachSyn]+ tuple[index+1:]
				newTupleKey= generateTupleKey(newTuple)
				#add new tuple to tupleDictionary
				tupleDictionary[newTupleKey]=1
	return tupleDictionary


#if no argument, print usage instructions
if len(sys.argv)==1:
	print "usage: myprog synonym_file input_file1 input_file1 [tuplesize]"
	print "tuplesize: the size of the tuple you want to use for comparison, default is 3"
	exit()

#check valid input size
if len(sys.argv)!=4 and len(sys.argv)!=5:
	print "wrong size of input!"
	exit()

# read command line inputs
synfile = sys.argv[1]	
inputfile1 = sys.argv[2]
inputfile2= sys.argv[3]
tupleSize=3


#if there is optional input, we change default tuplesize to be user defined size
if len(sys.argv)==5:
	tupleSize=int(sys.argv[4])

#initiate a 2dlist  to store data from synonym file 
synData=[]     

#initiate dictionary for synonym file-- key is the word, value is the lineindex of this word in the file
#value is default to be -1 
synDictionary=collections.defaultdict(lambda:-1)  

#read synfile to add data into sysnData and synDictionary
with open(synfile, "r") as file:
	lineIndex=0
	for line in file:
		lineData=[] 
		for eachword in line.rstrip('\n').split(" "):
			lineData.append(eachword)
			synDictionary[eachword]=lineIndex
		synData.append(lineData)
		lineIndex+=1

#initiate dictionary to record all the tuples that have occured -- key is tuple, value is the frequency of its occurrence
#value is deafult to be 0
tupleDictionary=collections.defaultdict(int)

#read inputfile1
inputFileData,wordCount=readInputFile(inputfile1)
checkWordCount(wordCount, tupleSize)

#add N-tuples in inputfile1 and its synonym tuples into tupleDictionary
tupleCount=0 #record how many N-tuples exists in inputfile1
for line in inputFileData:
	for startindex in range(len(line)):
		#check for outbound error
		if startindex+tupleSize>len(line):
			break
		currentTuple=line[startindex:startindex+tupleSize]
		TupleKey=generateTupleKey(currentTuple)     
		tupleDictionary[TupleKey]=1
		tupleDictionary=generateSynTuples(currentTuple,synDictionary,synData, tupleDictionary)
		tupleCount+=1

#check how many valid N-tuple exits in the inputfile1 
if tupleCount==0:
	print "print enter a smaller tuple size, no N-tuples found in input_file1"
	exit()

#read inputfile2
inputFileData2,wordCount2=readInputFile(inputfile2)
checkWordCount(wordCount2, tupleSize)

#check how many N-tuples in inputfile2 matches the ones in inputfile1
tupleCount2=0.0 	  #record how many N-tuples inputfile2
matchCount=0.0     #record how many N-tuples in the inputfile2 match the ones in inputfile1
for line in inputFileData2:
	for startindex in range(len(line)):
		#check for outbound error
		if startindex+tupleSize>len(line):
			break
		currentTuple=line[startindex:startindex+tupleSize]
		TupleKey=generateTupleKey(currentTuple) 
		#check if the tuple match the tuple in inputfile1   
		if tupleDictionary[TupleKey]==1:
			matchCount+=1
		tupleCount2+=1

#check how many valid N-tuple exits in the inputfile2
if tupleCount2==0:
	print "enter a smaller tuple size, no N-tuples found in input_file2"
	exit()

#compute result and print it
result=matchCount/tupleCount*100
print str(result)+"%"














