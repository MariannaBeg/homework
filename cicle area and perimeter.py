import math

print(len(str(math.pi)))

class Cicle:
	def __init__(self,r):
		self.radius = r

	def area(self):
		return self.radius**2*math.pi

	def perimeter(self):
		return 2*self.radius*math.pi

new_cicle=Cicle(8)

print(new_cicle.area())
print(new_cicle.perimeter())

