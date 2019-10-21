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

print(my_person.Name)
print(my_person.name.first_name)
print(my_person.name.last_name)
print(my_person.age)



