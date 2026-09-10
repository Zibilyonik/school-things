pizza=100
for pizza in range (1, 20+1):
    print(f"loop number {pizza}")

#first loop always starts at 0 


burger=1011
range_number=int(input("how many burgers will you eat?"))
if range_number <= 1011 and range_number > 0 :
    for burger in range (1, range_number + 1):
        print(f"you can eat {burger} burgers")


else: print("you cant eat this number of burgers")

burger=1000
range_number=int(input("how many burgers will you eat?"))
for burger in range (1, range_number+1):
    if range_number % 2==0:
        print(f"you eat even number of {burger} burgers")
    else:
        print(f"you will eat odd number of {burger} burgers")

user_while_count=int(input("wah is the max value?"))
while user_while_count >0:
    print(f"loop number {user_while_count}")
    user_while_count -=1

user_while_count=int(input("wah is the max value?"))
counter=0
while counter<= user_while_count:
    if counter % 2==0:
        print(f"you eat even number of {counter} burgers")
    else:
        print(f"you eat odd number of {counter} burgers")
    counter+=1