n=int(input("Please enter a number: "))
count=0
for i in range (1,n):
	for j in range(2,n):
 		if i%j==0 and i!=j:
 			break
 		if j==n-1:
 			print (i)
 			count+=1
print("the count of numbers is -",count)



