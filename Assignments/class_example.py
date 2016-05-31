class Dog: 
	name = "Fido"
	legs = 4 
	def bark(self):
		print "woof " * self.legs
	dog_type = "pitbull"

doggy = Dog()
print doggy.name
doggy.bark() 
doggy.legs = 6 
doggy.bark() 
print type(doggy)
print dir(doggy)