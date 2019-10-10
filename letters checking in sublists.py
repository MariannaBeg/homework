a=["aba","cla","csc",'dhfn','amsa','sssssss']
i=0
j=0
count=0
for i in a:
	if a[j][0]==a[j][-1]:
		count+=1
	j+=1	
print ("There are ",count,"words with same first and last letters")