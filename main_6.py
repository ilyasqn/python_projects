class Finance:
    def __init__(self):
        self.income = {}
        self.outcome = {}

    def adding(self, name, money):
        if name in self.income:
            self.income[name] += money
        else:
            self.income[name] = money
    def deleting(self, name, money):
        if name in self.outcome:
            self.outcome[name] -= money
        else:
            self.outcome[name] = money

    def total_adding(self):
        self.total_add = 0
        for value in self.income.values():
            self.total_add += value
        return self.total_add

    def total_deleting(self):
        self.total_del = 0
        for value in self.outcome.values():
            self.total_del += value
        return self.total_del
    def get_value(self):
        return self.total_add - self.total_del
    def get_adding(self):
        return self.income
    def get_deleting(self):
        return self.outcome

finance = Finance()
finance.adding("Зарплата", 1000)
finance.adding("Зарплата", 500)
finance.adding("Зарплата", 500)
finance.adding("Зарплата", 500)

finance.deleting("Питание", 1500)
finance.adding("Питание", 200)

print(finance.total_adding())
print(finance.total_deleting())
print(finance.get_value())
print(finance.get_adding())
print(finance.get_deleting())