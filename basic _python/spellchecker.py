import sys
import re

sentence_lst = []
for line in sys.stdin: 
	sentence_lst.append(line)

hist_file = open(sys.argv[1])
dict = {}
for line in hist_file: 
	line = line.strip("\n")
	line = line.strip(" ")
	lst_line = line.split(" ")
	if len(lst_line) > 1 and lst_line[1]: 
		lst_line[1] = lst_line[1].lower()
		if lst_line[1] in dict: 
			dict[lst_line[1]] = dict[lst_line[1]] + lst_line[0]
		else: 
			dict[lst_line[1]] = lst_line[0]

for sentence in sentence_lst: 
	print_string = ""
	sentence = sentence.strip("\n")
	lst_sentence = sentence.split(" ")
	for word in lst_sentence: 
		word = word.lower()
		end_punctuation = ""
		if re.search("[!?.,]", word[-1]): 
			end_punctuation = word[-1]
			word = word[0:len(word) - 1]
		if word not in dict:
			print_string += "*"
		print_string += word + end_punctuation + " "
	print(print_string)

	
	
	