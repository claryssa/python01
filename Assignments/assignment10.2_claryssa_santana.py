''' Claryssa Santana
Data Programming with Python
Assignment 10.2
5 May 2016 
Purpose: Write a program to figure out the distribution 
by hour of the day for each of the messages'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = {}

for line in handle: 
	if line.startswith("From"):
			linelst = line.split()
			try:
				time = linelst[4]
				timelst = time.split(':')
				hours[timelst[0]] = hours.get(timelst[0], 1) + 1 

			except:
				continue 
print "\nHours & Counts"
print hours