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
print line.rstrip()