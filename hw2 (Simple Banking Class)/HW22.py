# 10/08 HW2
# Name: 
# Due Date: 
# Collaboration Statement: 

class Person:
	customer_list = {}
	def __init__(self, name):
		self.name = name


class Customer(Person):
	customer_list = {}
	def __init__(self, name, ssn, balance):
		super().__init__(name)
		self.name = name
		self.__ssn = ssn
		self.balance = balance

	def add_account(self): # Add account to bank
		if self.name not in self.customer_list:
			self.customer_list[self.__ssn] = [self.name, self.balance]
		else:
			return self.__ssn

	def withdraw(self, amount): # Input: amount to withdraw, output: remaining amount
		if amount > self.balance:
			return 'Not enough funds'
		self.balance = self.balance - amount
		return f'You have ${self.balance} remaining.'

	def deposit(self, amount): # Input: amount to deposit, output: new amount
		self.balance = self.balance + amount
		return f'You now have {self.balance} in your account'


class Employee(Person):

	def getDetails(self): # Creating abstract function 
		raise NotImplementedError("Subclass must implement abstract method")
		
class Teller(Employee):
	def __init__(self, name):
		super().__init__(name)
		self.name = name

	def getDetails(self, customer): # Input: Customer Name, output: balance
		if customer in self.customer_list[self.name]:
			return f'Balance = ${self.balance}'
		else:
			return 'Not found.'


class Manager(Teller):
	def __init__(self, name):
		self.name = name

	def getDetails(self, customer): # Input: Customer Name, output: balance and ssn
		if customer in self.customer_list[self.__ssn]:
			return f'Balance = ${self.balance}, SSN = {self.__ssn}'
		else:
			return 'Not found.'

	def remove_account(self, customer): # Input: Customer Name, output: remove account
		if customer in self.customer_list[self.__ssn]:
			self.customer_list.pop(self.__ssn)
		else:
			return 'Not found'




