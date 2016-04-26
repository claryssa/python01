''' Claryssa Santana
Data Programming with Python
Assignment 7.3
28 Apr 2016 
Purpose: Write a program that opens and reads through a file looking for and counting lines 
of the form X-DSPAM-Confidence:    0.8475'''

import pprint 

totalLines = 0
total = 0 
values = []

fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
	for line in fh:
		if line[:line.find(' ')] == "X-DSPAM-Confidence:":
			totalLines += 1 
			num = line[line.find(':')+1:]
			try: 
				num = float(num)
				values.append(num)
				for number in values:
					total += number
			except:
				print num, "is not a float"
	print "\nLines:", totalLines
	print "Total:", total
	print "Average:", total/totalLines

except:
	print fname, "could not be opened."