def average(in_list):
	sum=0
	for number in in_list:
		sum+=number
	return sum/len(in_list)
my_list1=[1,2,3,4]
my_list2=[91,92,93,94]

print("The average of my_list1 is: ", average(my_list1))
print("The average of my_list2 is: ", average(my_list2))
