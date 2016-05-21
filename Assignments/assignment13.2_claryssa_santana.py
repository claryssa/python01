''' Claryssa Santana
Data Programming with Python
Assignment 13.2
24 May 2016
Purpose: Read HTML from the data files below, extract the href= values from the anchor tags,
scan for a tag that is in a particular position relative to the first name in the list, 
follow that link and repeat the process a number of times and report the last name you find.
'''
import urllib 
from BeautifulSoup import * 

url = raw_input("Enter URL: ")
count = raw_input("Enter count: ")
position = raw_input("Enter position: ")

try: 
	count = int(count)
	position = int(position)

	while count > 0:
		links = [] 
		tags = BeautifulSoup(urllib.urlopen(url).read())('a')
		
		for tag in tags:
			links.append(tag.get('href', None))

		url = links[position-1]
		count -= 1 

	print "Last URL:", url

except: 
	print "ERROR: Count and/or position are invalid."