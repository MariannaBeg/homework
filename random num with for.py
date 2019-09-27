import random

hidden_number=random.randfloat(0,1)

user_guess=0

while not user_guess==hidden_number:

 	user_guess=int(input("Guess a number:"))

 	if user_guess>hidden_number:
 		print("Too high!")
 	elif user_guess<hidden_number:
 		print("Too low!")
 	else:
 		print("Thats right!")
