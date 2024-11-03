# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my implementation of a bank account system where I created
# a class to handle basic banking operations. I used fun examples like Mr. Krabs and
# Spongebob as account holders to make it more interesting while learning about classes
# and object-oriented programming.

class Account:
    def __init__(self, acc_id, name, balance):
        # I'm initializing my account attributes here - each account needs an ID, 
        # holder's name, and starting balance
        self.account_id = acc_id
        self.name = name
        self.balance = balance

    def __str__(self):
        # I created this string method to nicely format how the account info is displayed
        # when I print an account object
        return f' Account ID :{self.account_id} Name : {self.name} Balance : {self.balance}'

    def deposit(self, amount):
        # My deposit method simply adds the given amount to the current balance
        self.balance = self.balance + amount

    def withdraw(self, amount):
        # In my withdraw method, I first check if there's enough money in the account
        # before allowing the withdrawal
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("Insufficient funds")

    def transfer(self, other_account, amount):
        # My transfer method combines withdraw and deposit to move money between accounts
        # but only if there's enough money in the source account
        if self.balance >= amount:
            self.withdraw(amount)
            other_account.deposit(amount)

def main():
    # In my main function, I'm testing all the account operations
    # Creating two test accounts with some initial money
    account1 = Account(1234, 'Mr.Krabs', 2000)
    account2 = Account(3456, 'Spongebob', 100)
    print(account1)  # I'm using the __str__ method here to display account1's info
    print(account2)

    print('Transfer')
    # Testing my transfer method by moving money from Mr. Krabs to Spongebob
    account1.transfer(account2, 250)
    print(account1)
    print(account2)

main()