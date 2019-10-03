def count_words(inputed):
	space=0
	for i in inputed:
		if(i==" "):
			space+=1
	if space==0:
		return f" it's a one word"
	elif space>0:
		return f'{space+1} words- it is a sentence!'
inputed=input("please insert word or sentence ...")
print(count_words(inputed))