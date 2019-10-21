class Person:
	def __init__(self,name,eyecolor,age):
		self.name = name
		self.eyecolor = eyecolor
		self.age = age

my_person1 = Person("Jirayr MElikyan","Brown",19)

my_person2 = Person(my_person1.name, my_person1.eyecolor,my_person1.age)

print(my_person1.name)
print(my_person2.name)

my_person1.name="aaaa"

print(my_person1.name)
print(my_person2.name)



