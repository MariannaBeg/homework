my_string="This string is not a number!"

try:
	print ("converting my str to int...")
	1/0
	print("string #"+"1"+":"+my_string)
	my_int=int(my_string)
	print(my_int)
except ValueError:
	print("Can't convert; my_string to a number")
except TypeError:
	print("Can't concatinate number with string")
except:
	print("Unknown error")

print("Done!")