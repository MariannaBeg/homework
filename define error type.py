def zero_division():
	print(1/0)

try:
	zero_division()
except Exception as error:
	print(error)