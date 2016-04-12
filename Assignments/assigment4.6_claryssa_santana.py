''' Claryssa Santana
Data Programming with Python
Assignment 4.6
7 Apr 2016 
Purpose: Creating a compute pay function building off of assignment 3.1 ''' 

def computePay(h,r):
	hours = float(h)
	rate = float(r)
	if hours <= 40.0 : 
		pay = hours * rate
	elif hours > 40.0 :
	 	standardHours = 40
	 	basePay = standardHours * rate 
	 	overtimeHours = hours - standardHours 
		overtime = overtimeHours * (rate*1.5) 
		pay = basePay + overtime 
	return pay

hours = raw_input("Enter Hours:")
rate = raw_input("Enter Pay Rate: ")
pay = computePay(hours,rate)
print "Pay: ", pay

system("pause")