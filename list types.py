#a = (1, 2)
#print(a)
#def tuple1():
#	user_name = input("Enter your name   -")
#	user_surname = input("Enter your surname   -")
#	return user_name,user_surname
#user_info=tuple1()
#print("Your name is " +user_info[0])
#print("Your surname is "+user_info[1])

#nested_list = [[1,2],[3,4],[5,6]]

#print(nested_list[0])
#print(nested_list[0][0])

my_list = [1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

my_list.remove(23)
print(my_list,":After removing23")

my_list.sort()
print(my_list,": After sorting")

my_list.reverse()
print(my_list,": After reversing")

my_list.pop(0)
print(my_list," : poping")

del my_list[-5:]# verjin 5 haty jnjum e
print(my_list,": After deleting the last five items")
