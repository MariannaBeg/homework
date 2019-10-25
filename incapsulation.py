class BankAccount:
	def __init__(self,amount):
		self.__amount=1000
		
	def getBalance(self):
		print(f'{self.__amount},is untouchable amount on your bank account')

	def setAmount(self,amount):
		self.__amount=amount
		print(f'{amount},changed amount is')
		

my_bank_account = BankAccount("")
my_bank_account.getBalance()
my_bank_account.setAmount(800)

