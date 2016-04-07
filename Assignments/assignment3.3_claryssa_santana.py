''' Claryssa Santana 
Data Programming with Python
Assignment 3.3 
7 Apr 2016 ''' 

print "Hello! Welcome to the Score-Grade Converter (:"
score = raw_input("Enter Score Here: ")

try: 
	score = float(score)

	if 1.0 >= score >= 0.9:
		print "Grade: A"
		print ":)"
	elif 0.9 > score >= 0.8:
		print "Grade: B"
	elif 0.8 > score >= 0.7:
		print "Grade: C"
	elif 0.7 > score >= 0.6:
		print "Grade: D"
	elif score < 0.6:
		print "Grade: F"
		print ":("
	else:
		print "The number you've entered is too big!"

except: 
	print "Oh no! You've entered an incorrect value"
