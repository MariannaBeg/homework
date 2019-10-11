def find_common_member(a,b):
	count=0
	i=0
	j=0
	for i in a:
		for j in b:
			if i==j:
				count+=1	
	return f'{count} -members in list are same -"True"'
a=[1,2,6,5,8]
b=[5,7,9,2,8,10]
print(find_common_member(a,b))
			