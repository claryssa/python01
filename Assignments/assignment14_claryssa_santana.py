''' Claryssa Santana
Data Programming with Python
Assignment 13.2
26 May 2016
Purpose: Prompt for a URL, read the XML data from that URL using urlliband
then parse and extract the comment counts from the XML data, and compute the sum of the numbers.
'''

import urllib 
import xml.etree.ElementTree as ET 

while True:
	url = raw_input("Enter URL: ")
	if len(url) < 1 : break 
	total = 0 
	for comment in ET.fromstring(urllib.urlopen(url).read()).findall('comments/comment'): 
		total += int(comment.find('count').text)
	print "Sum:", total 