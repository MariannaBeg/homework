def showNumbers(limit):
	i=0
	while i<=limit:
		if i%2==0:
			print(i,"EVEN")
		else:
			print(i,"ODD")
		i+=1
print(showNumbers(limit=int(input("please insert a limit of numbers -"))))	


