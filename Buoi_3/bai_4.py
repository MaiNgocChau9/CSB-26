class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
account_1 = BankAccount("123456789", 1000)
account_1.deposit(500)
account_1.withdraw(200)
print(f"Account {account_1.account_number} has a balance of {account_1.get_balance()}")