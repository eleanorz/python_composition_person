def display_greeting():
	print "Greetings, User!"

display_greeting()


name = raw_input("What is your name?")
print "you are " + name
# print "you are", name
age = raw_input("How old are you?")
print "you are " + age + "years old"
# print "you are" , age, "years old"

class Person:
	eyes = "black"

	def gender(self, gender) :
		print "I am %s" %(gender)
	def name(self, name):
		print "My name is %s" %(name)
	def age(self, age):
		print "I am %s years old" %(age)
	def pet(self, pet):
		print "My pet's name is %s" %(pet)


class Employee(Person):
	def position(self, position):
		print "I am the %s" %(position)

john = Employee()
john.gender("male")
john.name("John")
john.age(24)
john.position("janitor")
john.pet("rufus")