# . Write a program that accepts a sequence of whitespace separated words as input and prints 
#the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

a=input()
a=a.split()
list1=[]
for i in a:
	if i not in list1:
		list1.append(i)
list1.sort()
print(list1)