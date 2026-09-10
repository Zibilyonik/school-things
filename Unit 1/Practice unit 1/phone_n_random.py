import random

def user_number(number1,number2,number3):
    numbers=[number1,number2,number3]
    first1=random.choice(numbers)
    second1=random.choice(numbers)
    third1=random.choice(numbers)
    number=first1+second1+third1
    return number

numbers=(input("What 3 numbers you want to include in your code?:\n")).split() #user must have space between numbers
while len(numbers)!=3:
        numbers=(input("You entered numbers incorrectly, 3 numbers you want to include in your code?\\ps: use space between the numbers:\n")).split()

number=user_number(numbers[0], numbers[1], numbers[2])
print(f"yourcode is {number}")  
