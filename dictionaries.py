human={"name":"Jirayr","surname":"Melikyan","age":19, "is_married":False}

#print(human["name"],human["age"],human["is_married"])
human["age"]=30# arjeqy poxelu hamar e

print(human)

human["have_pet"]=False # ete uzumenq inchvor arjeq avelacnel vory chkar naxnakanum
print(human)

del human['age'] # inchvor arjeq jnjelu hamar
print(human)

human["Boys_name"]="Boy" # ete uzumenq inchvor arjeq avelacnel vory chkar naxnakanum
print(human)

human["Boys_name"]="Boo" # ete uzumenq inchvor arjeqi arjeqiy poxel
print(human)


print(human.keys())# bolor keyery tpelu hamar
print(human.values())# bolor valuenery tpelu hamar

for value in human.values(): # bolor valuenery irar tak grelu hamar
	print(value)

fruits={"apple":5,"orange":14,"pineapple":1,"bananas":4,"pomegranade":4}# arjeqy hamematelu hamar
for key in fruits.keys():
	if fruits[key]>5:
		print(key)
