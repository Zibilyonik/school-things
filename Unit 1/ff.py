def deposit(amount,balance): #uses the 1000 balance and adds the amount that is used as an argument in the last function(200)
    balance = balance + amount #1000+200=1200
    print("Deposited", amount, "New balance:", balance) 
    return balance

def withdraw(amount,balance): #the updated global value=1200 so 1200 - argument of ithdraw in the last function (150)
    if balance >= amount:
        balance = balance - amount # 1200-150=1050
        print("Withdrew", amount, "New balance:", balance)
    else:
        print("Insufficient funds!") # if balance is less than the amount of agrument its not enough balance
    return balance

def bank_app(balance): #initial balance and  then used functions in it changing its value for each
    print("Welcome to your bank account!")
    balance=deposit(200,balance) 
    balance=withdraw(150,balance)
    balance=withdraw(1200,balance)
    print("Final balance:", balance)

bank_app(1000) #calls the function that calls other functions with arguments


