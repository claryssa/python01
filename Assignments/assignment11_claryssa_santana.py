''' Claryssa Santana
Data Programming with Python
Assignment 11 
19 May 2016
Purpose: Read and parse a file extracting all 
numbers and computing their sum.
'''
import re

fh = raw_input("Enter file name here: ")

#.read() file method puts the entire file in one line
print "Sum:", sum(map(int, (re.findall('[0-9]+', (open(fh, 'r').read())))))
