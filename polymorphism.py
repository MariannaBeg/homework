class Dog:
	def sound(self):
		print("the sound of dog is Haff")

	def swim(self):
		print("the dog can swim")

class Cat:
	def sound(self):
		print("the sound of cat is Myaauu")

	def swim(self):
		print("Cats don't like to swim")

def sound_test(waouh):
	waouh.sound()
	waouh.swim()

joy=Dog()
catty=Cat()

sound_test(joy)
sound_test(catty)
