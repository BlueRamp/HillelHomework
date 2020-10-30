import uuid
from datetime import datetime


class Taxes:
    def __init__(self):
        self.tax = 0.01


class BankAccount:
    def __init__(self, account_name: str, balance: float):
        super().__init__()
        self.tax = Taxes().tax
        self.account_name = account_name
        self.uuid = uuid.uuid1()
        self.balance = balance
        self.transactions = []

    def get_transaction(self):
        return self.transactions

    def deposit(self, amount):
        self.balance += amount - amount * self.tax
        transaction = [str(self.uuid), self.balance, "deposit: ", datetime.today().strftime("%Y-%m-%d")]
        self.transactions.append(transaction)
        return self.transactions

    def cash_output(self, amount):
        self.balance -= amount - amount * self.tax
        transaction = [str(self.uuid), self.balance, "cash_output: ", datetime.today().strftime("%Y-%m-%d")]
        self.transactions.append(transaction)
        return self.transactions

    def view_balance(self):
        return self.balance


new_account = BankAccount("omatiukhov", 58500.47)
new_account.cash_output(10)
print(new_account.get_transaction())
