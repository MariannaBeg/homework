#1. Write a Python class which has two methods get_String and print_String.
# get_String accept a string from the user and print_String print the string in upper case.
class Exercise:
	def __init__(self,string):
		self.string=string
		self.num=5
	
	# def getString(self):
	# 	self.string=input()
		
	def printString(self):
		print(self.string.upper()+"  " +str(self.num))

str1=Exercise(input())
str1.num=10
#str1.getString()
str1.printString()


# # doesn't work :((((


# #2. Create a vehicle class. Create two new vehicles called car1 and car2. 
# #Set car1 to be a red convertible worth
# # $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.

# class Vehicle:
# 	def __init__(self,name,color,tapq,price):
# 		self.name=name
# 		self.color=color
# 		self.tapq=tapq
# 		self.price=price

# 	def showCar(self):
# 		description=(str(self.name) +" is "+str(self.color)+", "+str(self.tapq)+"  and the price is - "+str(self.price))
# 		print(description)


# car1=Vehicle("Ferarri","red","convertible","$60000")
# car2=Vehicle("Jump","blue","van","$10000")

# car1.showCar()
# car2.showCar()

#  #work :)))


