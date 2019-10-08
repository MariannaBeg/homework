ord('a')
# kti a - ID n

a="sajdlksdj"
for char in a:
	print(ord(char))

#ete uzum enq bolori kodery imananq ayspes e petq grel

a="յսֆկյֆ"
for char in a:
	print(ord(char))
a="кшдкшф"
for char in a:
	print(ord(char))


c="!"
print(ord(c))

char1="jhsaklhd!!!!hsdj!"
count=0
for i in char1:
	if i ==chr(33):
		count+=1
print(count)
	


# string slicing

a="sdhskjdh"
print(a[3:5])
# sa tpuma 4rd u 5rd elementnery
print(a[-5:-2])
#verjiny ktpi 4rd elemntic sksac 3 element

n="Hello Hrach"
print(n.find('h'))
#aystex kgri vor arajin H=0-aysinqn indexy
#ete chi gtnum gruma -1
print(n.find('hr'))
# aystex gruma 6 aysinqn 2rd h i indexy
print(n.find("h",2,4))
# ays depqum h y kpntri 2-4 rd tareri mej u es depqum kgri -1 qani vor chka

#grel split i orinak aystex 