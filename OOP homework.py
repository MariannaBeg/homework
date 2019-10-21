class BankAccount:
	def __init__(self,name,balance=0.0):
		self.log("Account created!")
		self.name = name
		self.balance= balance

	def getBalance(self):# getter
		self.log("Balance checked at " + str(self.balance))
		return self.balance

	def deposit(self,amount):#setter
		self.balance+=amount
		self.log("+" + str(amount) + ": " + str(self.balance))

	def withdraw(self,amount):
		self.balance-=amount
		self.log("-" + str(amount) + ": " + str(self.balance))

	def log(self,message):
		print(message)# petqa file baci bolory gri u file-y paki log.txt filum 

my_bank_account = BankAccount("Jirayr Melikyan")
my_bank_account.deposit(20.0)
my_bank_account.getBalance()
my_bank_account.withdraw(10.0)
my_bank_account.getBalance()

