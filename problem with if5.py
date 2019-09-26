num=int(input("Please insert a number of February days or the number of year's days  -"))
if num%28==0 or num%365==0:
	print("this is a non leap year :)))))")
elif num%29==0 or num%366==0:
	print(" this is a leap year:)))")
else:
	print("please insert a right number")