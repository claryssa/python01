''' Claryssa Santana
Data Programming with Python
Assignment 12
19 May 2016
Purpose: Retrieve a document using HTTP protocol 
to examine HTTP response headers. 
'''

import urllib 
from BeautifulSoup import * 

print BeautifulSoup(urllib.urlopen("http://www.pythonlearn.com/code/intro-short.txt").read())
