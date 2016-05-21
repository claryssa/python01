''' Claryssa Santana
Data Programming with Python
Assignment 13.1
24 May 2016
Purpose: Read HTML from the data files provided then parse the data, 
extracting numbers and computing the sum of the numbers.
'''

import urllib 
from BeautifulSoup import * 
lst = [] 

for tag in BeautifulSoup(urllib.urlopen('http://python-data.dr-chuck.net/comments_242237.html').read())('span'):
	lst.append(int(tag.contents[0]))

print "Sum:", sum(lst)