''' Claryssa Santana 
	Assignment 2 
	Purpose: Create a payment calculator for laborer ''' 

hours = raw_input("Enter Hours: ")
hours = float(hours)

rate = raw_input("Enter Pay Rate: ")
rate = float(rate) 

pay = hours * rate
print "Total Salary: ", pay
