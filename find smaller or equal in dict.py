prices={
		"apple":20,
		"bananas":10,
		"cup":15,
		"disc":16
		}
print(f"price must be at least {min(prices.values())} ")
a=int(input("Please input a price..."))

for key,value in prices.items():
	if value<=a:
		print("you can buy -",key,value)
	else:
		pass