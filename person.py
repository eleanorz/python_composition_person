class Person:
	eyes = "black"

	def gender(self, gender) :
		print "I am %s" %(gender)
	def name(self, name):
		print "My name is %s" %(name)
	def age(self, age):
		print "I am %s years old" %(age)

class Employee(Person):
	def position(self, position):
		print "I am the %s" %(position)

john = Employee()
john.gender("male")
john.name("John")
john.age(24)
john.position("janitor")