# 10/08 HW2
# Name: Thomas Schaeffer
# Due Date: 

import datetime
class Account:

    interest = 0.02  

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Not enough funds'
        self.balance = self.balance - amount
        return self.balance


class CheckingAccount(Account):

    withdraw_fee = 1
    interest = 0.01
    minimum=100

    def __init__(self,name,birthdate):
        super().__init__(name)
        self.birthdate=birthdate
    @property
    def age(self):
        month, day, year = self.birthdate.split("/")
        today = datetime.date.today()

        age = today.year - int(year)

        if today < datetime.date(today.year, int(month), int(day)):
            age -= 1

        return age

    def withdraw(self, amount):
        if self.age>21:
            return Account.withdraw(self, amount + self.withdraw_fee)
        else:
            return 'You can only withdraw ${}'.format(CheckingAccount.minimum)

    

class Bank:
    def __init__(self):
        self.accounts = []

    def openAccount(self, holder, amount, account_type=Account):
        """Open an account_type for holder and deposit amount."""
        account = account_type(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def payInterest(self):
        """Pay interest to all accounts."""
        for account in self.accounts:
            account.deposit(account.balance * account.interest)

