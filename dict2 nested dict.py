
grades={"Gor_Smbatyan":26,"David_Grigoryan":26,"Vardges_Hovhannisyan":26,"Rafael_Kostanyan":28,"Khachatur_Khachatryan":23,"Marat_Yavrumyan":24,"Artur_Altunyan":23,"Sedrak_Harutyunyan":24,"Marianna_Beglaryan":25,"Vardges_Davtyan":28,"Tigran_Danielyan":28,"Gevorgyan_Arno":23,"Arthur_Ananyan":29,"Arman":28}
for (key,value) in grades.items():# ete uzumenq amboxj koplekty tpi
	print (key,value)
	grades["Marianna_Beglaryan"]=23
	#print(key,value)

#ete cankanum enq mi qani key haytararenq , miqani valuenerov u meki mej mi ban avelacnenq

classes={"Math":["David","Lucy","Dana"], 
		  "Physics":["Addison","Benjamin"],
		  "Chemistry":["Sara","Pele"]}

print("Students in math class",classes["Math"])

classes["Math"].append("Jirayr")# value avelacnelu dzevy

print("Students in math class",classes["Math"])

dictionary={"Nick":{"Phone_number":123,"age":20}}# nested dictionary
print(dictionary)