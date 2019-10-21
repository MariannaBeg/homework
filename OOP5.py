class Name:
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name

class Person:
	def __init__(self,name,eyecolor,age):
		self.name = name
		self.eyecolor = eyecolor
		self.age = age

my_name=Name("Jirayr","Melikyan")

my_person= Person(my_name,"Brown", 19)

def capitalize_name(name):
	name.first_name = name.first_name.upper()
	name.last_name = name.last_name.upper()

capitalize_name(my_name)

print(my_person.name.first_name,my_person.name.last_name)
