''' Claryssa Santana
Data Programming with Python
Assignment 4.6
7 Apr 2016 
Purpose: Creating a compute pay function building off of assignment 3.1 ''' 

def computePay(hours, rate):

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

print "Enter your hours and pay rate to view your total salary! (:"
hours = raw_input("Enter Hours:")
rate = raw_input("Enter Pay Rate: ")

try: 
	h = float(hours)
	r = float(rate)
	computePay(h, r)

except:
	print "Incorrect value entered"