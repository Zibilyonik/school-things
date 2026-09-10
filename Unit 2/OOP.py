#Class: Bank Account; Object:Your Bank Account
#Class: Credit Card ;
#Credit score
#Balance
#History
#Name
#show_balance()
#withdraw()
#deposuit()
#close()
#object= BankAccount("username")

class BankAccount: # Class names start with capital letter and have capital word. (Naming Conventions)
    def __init__(self, name): #OR double under functions aka Dunder functions, is when we do default without requiring users input
        self.name = name
        self.balance = 0
        self.history = []
    def show_balance(self):
        print(f"Your bank account has {self.balance} money")
    def deposit(self, amount):
        self.balance+=amount
        print(f"Deposit sucessful, you now have {self.balance} added to your bank account")
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"You only have {self.balance} in your accund, withdrawal impossible")
        else:
            self.balance -= amount
            print(f"You withdrew {amount}, now u have {self.balance} left")
    def crumple():
        print("Crumple crumple")



my_account = BankAccount("Senya")
my_account.balance