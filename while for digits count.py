n=int(input("please insert a number : "))
sum=0
while n!=0:
	n/=10
	n=int(n)
	sum+=1
print("there are", sum,"digits in this number")
