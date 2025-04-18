import random

class Account:
    def __init__(self, name, initial_deposit):
        self.account_number = random.randint(1000, 9999)  # Generate a random account number
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Not enough balance.")

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_deposit):
        account = Account(name, initial_deposit)
        self.accounts[account.account_number] = account
        print(f"Account created for {name} with Account Number: {account.account_number}")

    def view_account(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(account)
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
        else:
            print("Account not found.")

    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            for account in self.accounts.values():
                file.write(f"{account.account_number},{account.name},{account.balance}\n")
        print("Accounts saved to file.")

    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as file:
                for line in file:
                    account_number, name, balance = line.strip().split(',')
                    account = Account(name, float(balance))
                    account.account_number = int(account_number)
                    self.accounts[account.account_number] = account
            print("Accounts loaded from file.")
        except FileNotFoundError:
            print("No file found. Starting with empty bank.")


#usage:
bank = Bank()
bank.load_from_file()  # Load accounts from file (if exists)

#new accounts
bank.create_account("Alice", 1000)
bank.create_account("Bob", 500)

#account details
bank.view_account(1001)  # Replace with a valid account number

#deposit, withdraw
bank.deposit(1001, 200)
bank.withdraw(1001, 100)

#save accounts to file
bank.save_to_file()
