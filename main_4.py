class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        return self.balance

    def withdraw(self, money):
        if money > self.balance or money <= 0:
            print("Error")
        else:
            self.balance -= money
            return self.balance



