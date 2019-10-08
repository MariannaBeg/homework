my_string=input()
if len (my_string)<=2:
	print (my_string)
elif len (my_string)>=3 and my_string[int(len(my_string))-3:int(len(my_string))]!="ing":
	print(my_string+"ing")
else :
	print(my_string+"ly")


	