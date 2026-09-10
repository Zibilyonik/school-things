#Write a for loop that adds all the numbers from 1 to unser input
total_value=0
user_input=int(input("write the value here"))
for number in range(1, user_input+1):
    print(f"you have {number} of numbers")
    total_value+=number
print(f"total value is {total_value}")
