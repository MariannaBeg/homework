dict1={"1":"a","2":"b","3":"c","4":"d","5":"a"}
dict2={}

for key,value in dict1.items():
	if value not in dict2.values():
		dict2[key] = value	
print (dict2)
