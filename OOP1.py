class Name:
	def __init__(self): # init-y method e
		self.first_name = "[no first name]"
		self.last_name = "[no last name]"

class Person:
	def __init__(self):
		self.name = Name()
		self.eye_color = "[no eye color]"

# my_person -instance na 
#Person class-i,isk nerqevi persony-funkcian e dra hamar () ov e?
my_person=Person() # constractor of function, ete uzumenq jnjel destructor

print(my_person.name.first_name)
print(my_person.name.last_name)
print(my_person.eye_color)

# ka 4 gorcoxutyan tesak:
#1.constructor, destructor, getter, setter