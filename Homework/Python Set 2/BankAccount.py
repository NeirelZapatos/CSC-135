class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            return
        self.balance = self.balance + amount

    def withdraw(self, amount):
        new_balance = self.balance - amount
        if new_balance < 0 or amount < 0:
            return
        self.balance = new_balance
