''' Claryssa Santana 
	Assignment 3 
	Purpose: Create a payment calculator for laborer that also calculates over time ''' 

print "Enter your hours and pay rate to view your total salary! (:"
hours = raw_input("Enter Hours: ")
rate = raw_input("Enter Pay Rate: ")

try:
	hours = float(hours)
	rate = float(rate)

	if hours <= 40.0 : 
		normalPay = hours * rate
		print "Your Salary is $", normalPay
		print "Thank you. Come again ~"
	else: 
		extraHours = hours - 40
		overtime = extraHours * (rate*1.5) 
		totalPay = (40 * rate) + overtime
		print "Your Salary is $", totalPay
		print "Thank you. Come again ~"
		
except: 
	print "Incorrect value entered"


