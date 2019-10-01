def fizz_buzz(num):
	if num%5==0 and num%3==0:
		return f'"FizzBuzz"' 
	elif num%5==0:
		return f'"Buzz"'
	elif num%3==0:
		return f'"Fizz"'
	return f'{num}'
num=int(input("please insert number -"))
print(fizz_buzz(num))	
