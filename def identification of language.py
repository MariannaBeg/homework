string=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def check_letters(letters):	
	for i in string:		
		for j in letters:
			if j==i:
				return f"congrats it is ENGLISH!!!"
	else:
		return f"-it's not English!"
print(check_letters(letters=input("please insert text...")))