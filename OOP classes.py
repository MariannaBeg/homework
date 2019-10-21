class Book:
	def __init__(self,name,year,author,price):
		self.name=name
		self.year=year
		self.author=author
		self.price=price

	def get_author(self):
		return self.author

	def set_price(self,price):
		self.price=price
		

my_book1=Book("Inferno",2012,"Dan Brown","141$")
my_book2=Book("Angels and Demons",2014,"Dan Brown","141$")

print(my_book1.get_author())
print(my_book1.price)
my_book1.set_price("10$")
print(my_book1.price)