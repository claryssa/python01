''' Claryssa Santana
Data Programming with Python
Assignment 5.2
18 Apr 2016 
Purpose: Write a program that calculates the largest and smallest of numbers''' 

print "Welcome to Extrema!\nWhere you can fulfill all your minimum and maximum needs (:\n"

largest = None
smallest = 0
numList = [] 

try:
	while True:
		num = raw_input('Enter a number: ')
		if num == 'done': break
		num = int(num)
		numList.append(num)
		for num in numList:
			if num > largest:
				largest = num
			if num < smallest:
				smallest = num
	print "Maximum", largest
	print "Smallest", smallest 

except:
	print "Sorry. That's not a number."

