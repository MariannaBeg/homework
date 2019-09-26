print("Please insert a word or sentence")
user_input=input()
if " " in user_input:
	print("it is a sentence")
else:
	print("it is a word")