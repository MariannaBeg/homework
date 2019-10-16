s="jsadlk25"
dict1={}
for i in s:
	if i in dict1:
		dict1[i]+=1
	else:
		dict1[i]=1
print(dict1)