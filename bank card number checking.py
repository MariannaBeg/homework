ameria='0001'
converse='0002'
ineco='0003'
evoca='0004'
AMEX='0005'
balance =500
def check_balance(purchase_price):
	if purchase_price>balance:
		return "you have not enough balance"
	else:
		return "Your balance after purchase is" + str(balance-purchase_price)
def validate_credit_card(card_number):
	if len(card_number)==16 and card_number[0:4] != AMEX:
		return True
	elif len(card_number)==15 and card_number[0:4] == AMEX:
		return True
	else:
		return False
def check_card_bank(card_number):
	if card_number[0:4]==ameria:
		return "Ameria bank"
	elif card_number[0:4]==converse:
		return "Converse bank"
	elif card_number[0:4]==ineco:
		return "Ineco bank"
	elif card_number[0:4]==evoca:
		return "Evoca bank"
	else:
		return "American Express Card"
card=input("input your card number")

if validate_credit_card(card):# it works if true:
	print("your credit card belongs to "+check_card_bank(card))
	purchase=input("Enter your purchase price")
	print(check_balance(int(purchase)))
else:
	print("Tou have entered wrong credentials")



