class Rectangle:
	def __init__(self,l,w):
		self.length=l
		self.width=w

	def rectangle_area(self):
		return self.length *self.width

	def rectangle_perimeter(self):
		return (self.length + self.width)*2

rectangle_l=int(input("Input rectangle lenght..."))
rectangle_w=int(input("Input rectangle width..."))

my_rectangle = Rectangle(rectangle_l,rectangle_w)

print(my_rectangle.rectangle_area())
print(my_rectangle.recyangle_perimeter())