class Account:
    def __init__(self, acc_num, name, balance):
        self.acc_num = acc_num
        self.name = name
        self.balance = balance

    def show(self):
        print("Account:", self.acc_num)
        print("Name:", self.name)
        print("Balance:", self.balance)


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self):
        acc_num = input("Enter new account number: ")
        name = input("Enter name: ")
        dep = input("Enter deposit: ")
        self.accounts[acc_num] = Account(acc_num, name, float(dep))
        print("Account created!")

    def view_account(self):
        acc = input("Enter account number: ")
        if acc in self.accounts:
            self.accounts[acc].show()
        else:
            print("Account not found.")

    def deposit(self):
        acc = input("Account number: ")
        if acc in self.accounts:
            amt = float(input("Amount to deposit: "))
            self.accounts[acc].balance += amt
            print("Deposit done.")
        else:
            print("Account doesn't exist.")

    def withdraw(self):
        acc = input("Account number: ")
        if acc in self.accounts:
            amt = float(input("Amount to withdraw: "))
            if amt <= self.accounts[acc].balance:
                self.accounts[acc].balance -= amt
                print("Withdrawn.")
            else:
                print("Not enough balance.")
        else:
            print("Account not found.")

    def save_to_file(self):
        f = open("accounts.txt", "w")
        for acc in self.accounts.values():
            f.write(acc.acc_num + "," + acc.name + "," + str(acc.balance) + "\n")
        f.close()

    def load_from_file(self):
        try:
            f = open("accounts.txt", "r")
            for line in f:
                data = line.strip().split(",")
                self.accounts[data[0]] = Account(data[0], data[1], float(data[2]))
            f.close()
        except:
            pass

    def menu(self):
        while True:
            print("\n1. Create\n2. View\n3. Deposit\n4. Withdraw\n5. Save\n6. Exit")
            ch = input("Choose: ")
            if ch == "1":
                self.create_account()
            elif ch == "2":
                self.view_account()
            elif ch == "3":
                self.deposit()
            elif ch == "4":
                self.withdraw()
            elif ch == "5":
                self.save_to_file()
            elif ch == "6":
                break
            else:
                print("Invalid input.")


# Run
b = Bank()
b.menu()
