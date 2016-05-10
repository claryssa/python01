''' Claryssa Santana
Data Programming with Python
Assignment 8.4
3 May 2016 
Purpose: Explore the split() and list() functions
'''

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
	words = line.split()
	for word in words:
		if word not in lst:
			lst.append(word)

lst.sort()

for word in lst:
	print word.lower()
