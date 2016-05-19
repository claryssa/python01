''' Claryssa Santana
Data Programming with Python
Assignment 12
19 May 2016
Purpose: Retrieve a document using HTTP protocol 
to examine HTTP response headers. 
'''
import socket 

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect(("www.pythonlearn.com",80))

socket.send("GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n")

while True:
	data = socket.recv(512)
	if (len(data) < 1):
		break
	print data 

socket.close() 