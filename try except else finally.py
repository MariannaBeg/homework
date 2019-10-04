my_string="12"

try:
	print ("converting my str to int...")
	print("string #"+"1"+":"+my_string)
	my_int=int(my_string)
	print(my_int)
except ValueError:
	print("Can't convert; my_string to a number")
except TypeError:
	print("Can't concatinate number with string")
except:
	print("Unknown error")
else:
	print("No errors occured")
finally:
	print("try-except code is finished")

print("Done!")