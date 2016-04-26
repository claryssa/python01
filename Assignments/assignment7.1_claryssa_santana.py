''' Claryssa Santana
Data Programming with Python
Assignment 7.1
26 Apr 2016 
Purpose: Write a program that prompts for a filename, opens/reads through it, 
and prints the contents of the file in upper case.'''

fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
	for line in fh:
		line = line.upper()
		print line
except:
	print "Could not open", fname

