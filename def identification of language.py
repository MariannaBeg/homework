string="abcdefghijklmnopqrstuvwxyz"

def check_letters(letters):	
	count=0
	count1=0
	for i in letters:		
		if i in string:
			print ({i},"- ENGLISH!!!")
			count+=1		
		else:
			print({i},"-it's NOT English!")
			count1+=1
	print (count,' -symbols are in English')
	print (count1,"-symbols aren't in English")
print(check_letters(letters=input("please insert text...")))