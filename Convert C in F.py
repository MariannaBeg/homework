def convert(temp):
	return f'{temp} C is equal to {farenheit} F'
temp=int(input("Please insert temperature in C - " ))
farenheit=(temp*9)/5+32
print(convert(temp))
