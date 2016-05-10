''' Claryssa Santana
Data Programming with Python
Assignment 8.5
3 May 2016 
Purpose: Print and count the email address of those who sent messages 
			within the file mbox-short.txt
'''

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0

for line in fh:
	if line.startswith("From: "):
		count += 1 
		linelst = line.split()
		print linelst[1]

print "There were", count, "lines in the file with From as the first word"

