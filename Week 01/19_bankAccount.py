class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self,amount):
        self.balance +=amount
    def withdraw (self,amount):
        self.balance -= amount
    def check_bal(self):
        return self.balance          


acc = BankAccount()
acc.deposit(500000)
acc.withdraw(5400)
print("Balance",acc.check_bal())