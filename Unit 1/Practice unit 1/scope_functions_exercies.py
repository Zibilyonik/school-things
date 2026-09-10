"""
Find the errors in the code on your own.
Try to fix the errors FIRST USING "global" keyword, write comments to describe the errors.
Use breakpoints and print() calls to see if it functions as it should. (15 mins)
If you finish early, try to also solve the bugs by removing the global variable and using parameters and return values.
Discuss your code in pairs and explain your reasoning to each other (10 mins)
We'll go over the errors together after the exercise to see where you may have had problems
THINGS TO CONSIDER :
    1: Can you explain what the function does without showing the code itself?
    2: Did you avoid using global variables as much as you can?
    3: Are your function and variable names descriptive and concise?
    4: Do your comments describe the functionality well enough?
"""



balance = 1000

def deposit(amount): #uses the 1000 balance and adds the amount that is used as an argument in the last function(200)
    global balance
    balance = balance + amount #1000+200=1200
    print("Deposited", amount, "New balance:", balance) 

def withdraw(amount): #the updated global value=1200 so 1200 - argument of ithdraw in the last function (150)
    global balance
    if balance >= amount:
        balance = balance - amount # 1200-150=1050
        print("Withdrew", amount, "New balance:", balance)
    else:
        print("Insufficient funds!") # if balance is less than the amount of agrument its not enough balance

def bank_app(): #initial balance and  then used functions in it changing its value for each
    print("Welcome to your bank account!")
    deposit(200) 
    withdraw(150)
    withdraw(1200)
    print("Final balance:", balance)

bank_app() #calls the function that calls other functions with arguments





