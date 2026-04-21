# -*- to Create a bankaccount class for deposit and withdrawl -*-
"""
Created on Tue Apr 21 05:11:49 2026

@author: Shahuraj
"""

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def display_balance(self):
        print("Current Balance:", self.balance)


# Create account
acc = BankAccount()

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        acc.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        acc.withdraw(amount)

    elif choice == 3:
        acc.display_balance()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
