''' Claryssa Santana
Data Programming with Python
Assignment 15.2
31 May 2016
Purpose: Prompt for a URL, read the JSON data from that URL using urlliband 
then parse and extract the comment counts from the JSON data then compute the 
sum of the numbers in the file.
'''
import urllib
import json

while True:
	url = raw_input('\nEnter location: ')
	if len(url) < 1 : break

	print 'Retrieving', url
	print '\nRetrieved',len(urllib.urlopen(url).read()),'characters'
	print 'Count:', len(json.loads(urllib.urlopen(url).read())['comments'])

	total = 0 
	for num in json.loads(urllib.urlopen(url).read())['comments']:
		total += int(num['count'])
	print 'Sum:', total