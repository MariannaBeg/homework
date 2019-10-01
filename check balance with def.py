def check_balance(balance,expences):	
	return balance-expences
balance=int(input("how much money do you have? -"))
first_item_price=int(input("please insert first item price - "))
second_item_price=int(input("please insert second item price -"))
third_item_price=int(input("please insert third item price -"))
price=first_item_price+second_item_price+third_item_price
tax=(price/100)*10
expences=price+tax
print("Your balance after expences is",check_balance(balance,expences))
total=balance-expences
if total>=0:
	print("you can buy all these items")
else:
	print("please refill your balance")

    