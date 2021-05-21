'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods 
work as expected.
'''

class Bank(object):
    def __init__(self,balance=0.0):
        self.balance=balance
    def display_balance(self):
        print(f'Your available balance is {self.balance}')
    def deposit_balance(self):
        amount=float(input('Please inset a balance: '))
        self.balance+=amount
        print(f'Your balance is {self.balance}')
    def make_withdrawal(self):
        amount=float(input("How much would you like to withdraw? "))
        if self.balance<amount:
            print(f'You dont have enough balance {self.balance}')
        else:
            self.balance-=amount
            print(f'Your balance is {self.balance}')

Alek_ac=Bank()
Alek_ac.display_balance()
