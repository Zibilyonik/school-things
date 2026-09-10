"""
#Task Description:
#You’ve been hired to write a simple program to help a small juice bar keep track of a single customer’s order.
The program will let the customer order different juices one by one and keep a running total of how much the order costs.
Requirements:
Ask the customer what juice they’d like to order. 
If they type "done" (in any case format), the program should stop and print the total bill.
Use .lower() to handle case-insensitive input.
Ask for the price of the juice they ordered (as a float). Add this amount to the total bill
After each order, print a confirmation message using an
<juice> was added for <price> dollars.

Example output:
"Mango juice was added for 3.5 dollars."
After each addition, print out the running total:
Your total so far is: <total> dollars.
Continue the loop until the customer types "done"
When finished, print a thank-you message and show the .
Example output of the function run:
Welcome to FreshWave Juice Bar!
What juice would you like to order? (input)Mango
How much does Mango juice cost? (input)3.5
Mango was added for 3.5 dollars.
Your total so far is: 3.5 dollars.
What juice would you like to order? (input)Berry Mix
How much does Berry Mix juice cost? (input)4
Berry Mix was added for 4.0 dollars.
Your total so far is: 7.5 dollars.
What juice would you like to order? (input)done
Thank you for your order! Your total is: 7.5 dollars.

EXTRA: You can also track the item count and print it at the end, alongside the total.
EXTRA EXTRA: You can implement a list to track the items ordered, and print them in a loop at the end.
"""
import random 

all_juice= []
number_orders=0
total_cost=0

def bucket_juice(juice):
    all_juice.append(juice)
    return all_juice

 
juice=input("What juice you want?").lower()
number_orders+=1
bucket_juice(juice)
price=float(input(f"What is the pice of the {juice} juice?"))
total_cost+=price
print(f"{juice} was added to the bill for {price}\nThere was total of {number_orders} orders")
print(f"your total so far is {total_cost}")

while juice!="done":
    juice=input("What juice you want?").lower()
    if juice!="done":
        number_orders+=1
        bucket_juice(juice)
        price=float(input(f"What is the pice of the {juice} juice?"))
        total_cost+=price
        print(f"{juice} was added to the bill for {price}\nThere was total of {number_orders} orders")
        print(f"your total so far is {total_cost}")
    else:
        break

print(f"Your total bill is {total_cost} ")
for i in range(0, len(all_juice) ):
    print(f"You bought {all_juice[i]} juice")
    
print("Thank you for seeing my WOnderFULL code:)))))))!!!!")

"""
What juice you want?apple
What is the pice of the apple juice?12
apple was added to the bill for 12.0
There was total of 1 orders
What juice you want?Pineapple
What is the pice of the pineapple juice?30
pineapple was added to the bill for 30.0
There was total of 2 orders
What juice you want?waterMaelon
What is the pice of the watermaelon juice?10
watermaelon was added to the bill for 10.0
There was total of 3 orders
What juice you want?done
Your total bill is52.0 
You bought apple juice
You bought pineapple juice
You bought watermaelon juice
Thank you for seeing my WOnderFULL code:)))))))!!!!
"""