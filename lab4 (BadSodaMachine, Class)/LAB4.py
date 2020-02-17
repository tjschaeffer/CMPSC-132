#Lab #4
#Due Date: 09/20/2019, 11:59PM EST
########################################
#                                      
# Name: 
# Collaboration Statement:
#
########################################


class BadSodaMachine:
    '''
        >>> m = BadSodaMachine('Coke', 10)
        >>> m.purchase()
        'Product out of stock'
        >>> m.purchase(2)
        'Product out of stock'
        >>> m.restock(3)
        'Current soda stock: 3'
        >>> m.purchase()
        'Please deposit $10'
        >>> m.deposit(7)
        'Balance: $7'
        >>> m.purchase()
        'Please deposit $3'
        >>> m.purchase(2)
        'Please deposit $13'
        >>> m.deposit(5)
        'Balance: $12'
        >>> m.purchase()
        'Coke dispensed, take your $2'
        >>> m.deposit(20)
        'Balance: $20'
        >>> m.purchase(2)
        'Coke dispensed'
        >>> m.deposit(15)
        'Sorry, out of stock. Take your $15 back'
    '''
    def __init__(self, product, price):
    # --- YOU CODE STARTS HERE
        
        self.product = product
        self.price = price
        self.balance = 0
        self.stock = 0
        if (type(product) != str) or (type(price) != int):
            return("Invalid Input")

    # --- YOU CODE STARTS HERE. Notes from Module 1 could be useful here!
    def purchase(self, amount=1):
       
        if self.stock <= 0: # nothing to buy
            return "Product out of stock"

        if self.stock < amount:
            return "Not enough stock"
        
        if self.balance < (amount * self.price): # not enough money
            balancerequired = abs(self.balance - (amount * self.price)) # removes negative for correct output for doctest
            return 'Please deposit $' + str(balancerequired)
        
        elif self.balance > (amount * self.price): # more money than needed
            self.stock = self.stock - amount
            self.balance = self.balance - (amount * self.price)
            output = self.product + " dispensed, take your $" + str(self.balance)
            self.balance = 0
            return(output)
        
        else: # perfect amount of money
            self.stock = self.stock - amount
            self.balance = self.balance - (amount * self.price)
            return self.product + " dispensed"

    def deposit(self, amount):
    # --- YOU CODE STARTS HERE

        if self.stock == 0: # if there is no stock left
            return "Sorry, out of stock. Take your $" + str(amount) + " back"
        self.balance = self.balance + amount
        return "Balance: $" + str(self.balance)

    def restock(self, amount):
    # --- YOU CODE STARTS HERE

        self.stock = self.stock + amount
        return 'Current soda stock: ' + str(self.stock)
    