class UserSuperclass:
    members_of_app=[]
    def __init__(self,name, id_user,email):
        self.name=name
        self.id_user=id_user
        self.email=email
        UserSuperclass.members_of_app.append(self)

    def log_in(self, name,email):
        if name==self.name and email==self.email :
            print(f"You logged in at your {self.id_user}")
            return True
        else:
            print(f"You didnt log in")
            return False

    def log_out(self):
        print("YOu been logged out")

    def __str__(self):
        return f"User ID: {self.id_user} | Name: {self.name} | Email: {self.email}"

    

#ENCAPSUALTION::
# private (-) attributes  : __       = has 2  ex: __name
# protected (#) attributes  : _     = has 1 ex. _model
# getter method : getColor(self) : return self.__color
# setter method : setColor(self,newColor) : self.__color=newColor
#In python there is no perferc privatate/protected attributes, but the concept exists outride
# Perfect encapsulation:
#IN python when we use "__" it, oython changes te naem of it in the runtime. This doesnt make attribute unreachable, it just makes it harder
# Polymorphism : static - parameter changes, dynamic- behaviour of funcitin changed
#Static variable : not part of any object, but a part of class itself (before __init)v --- keep track



class CustomerUser(UserSuperclass):
    def __init__(self, name, id_user, email, number_customer,adress,phone_number):
        super().__init__(name, id_user,email )
        self.__number_customer=number_customer
        self.__adress=adress
        self.__phone_number=phone_number

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, new_phone):
        self.__phone_number = new_phone
    def open_acc(self,name,number_customer):
        if self.__number_customer==number_customer and self.name==name:
            return Account(100,0,"savings")
        else:
            print("no acces to account")
        
    def request_loan(self):
        return None
    


class Account:
    def __init__(self,account_num,balance,account_type):
        self.__account_num=account_num
        self.__balance=balance
        self._account_type=account_type
    def show_balance(self):
        print(f"Current balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative")

    def deposit(self,amount):
        self.__balance += amount
        t = Transaction(1, "12-03-2026", amount)
        t.process()
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            t = Transaction(2, "12-03-2026", amount)
            t.process()

    
class Transaction:
    no_transactions=0
    def __init__(self,transaction_id,date,amount):
        self._transaction_id=transaction_id
        self.__date=date
        self.amount=amount
    def process(self):
        print("In action....")
        self.reciept()
    def reciept(self):
        Transaction.no_transactions+=1
        print(f"//{Transaction.no_transactions}// \nYou receipt is {self.amount} , at {self.__date}, id {self._transaction_id}")





user1 = CustomerUser("Anna",101,"anna@mail.com",1,"London","12345")
user2 = CustomerUser("Tom",102,"tom@mail.com",2,"Paris","67890")
user3 = CustomerUser("Eva",103,"eva@mail.com",3,"Berlin","99999")
print("\nAll Members:\n")
for member in UserSuperclass.members_of_app:
    print(member)