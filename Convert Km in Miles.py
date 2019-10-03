def convert(km):
	return f'{km} Km is equal to {miles} Miles'
km=int(input("Please insert speed in Km - " ))
miles=round(km/1.609)
print(convert(km))
