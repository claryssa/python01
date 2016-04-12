''' Claryssa Santana 
	Assignment 3 
	Purpose: Create a payment calculator for laborer that also calculates over time ''' 

hours = raw_input("Enter Hours: ")
rate = raw_input("Enter Pay Rate: ")

try:
	hours = float(hours)
	rate = float(rate)

	if hours <= 40.0 : 
		normalPay = hours * rate
	elif hours > 40.0 : 
		overtime = hours * (rate/2) 
	pay = normalPay + overtime
	print "Total Salary: ", pay

except: 
	print "Incorrect value entered"

