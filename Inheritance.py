class Vehicle:
	def __init__(self,name,year):
		self.name=name
		self.year=year

	def showCar(self):
		description=(self.name +" is "+"  and the color is - "+self.year)
		print(description)

class Electromobile(Vehicle):

	def __init__(self,name,year,color,price):
		super().__init__(name,year)
		self.color=color
		self.price=price
	def describeCar(self):
		print("The color of this car is "+self.color+"  price is -"+ self.price)



car1=Vehicle("Ferarri","1997")
car2=Vehicle("Jeep","2019")
car3=Electromobile("BMW","2018","red","$90000")
car4=Electromobile("Totota","2019","blue","$30000")
car1.showCar()
car2.showCar()
car3.showCar()
car4.showCar()
car3.describeCar()
car4.describeCar()



