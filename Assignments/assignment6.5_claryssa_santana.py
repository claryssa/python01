''' Claryssa Santana
Data Programming with Python
Assignment 6.5
21 Apr 2016 
Purpose: Write a code using find() and string slicing'''

text = "X-DSPAM-Confidence:    0.8475";
print "\nHere is your original input -->", text
print "After a bit of finding and slicing . . .\n"
num = text[text.find(':')+5:]
try:
	num = float(num)
	print "Here is your number", num

except:
	print "Your number was not found."

