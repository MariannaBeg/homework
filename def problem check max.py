def find_max(num1,num2,num3):
	if num1>num2 and num1>num3:
		return f'{num1}- is bigger'		
	elif num2>num1 and num2>num3:
		return f'{num2} -is bigger'
	elif num3>num1 and num3>num2:
		return f'{num3} - is bigger'
	return f'two or more nums are same'
num1=int(input("please enter num1 -"))
num2=int(input("please enter num2 -"))
num3=int(input("please enter num3 -"))
print(find_max(num1,num2,num3))