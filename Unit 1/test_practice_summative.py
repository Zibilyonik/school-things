name=(input("What is your name?:"))
name=name.capitalize()
time=(int(input("What time is it? 0-23:")))
time_valid= time>=0 and time<=23
if time_valid==False:
    print("Please run again and input a valid time")
    exit()
i=time

if i==0 or i<12:
    print(f"Good morning {name}")
elif i>=12 and i<18:
     print(f"Good afternoon {name}")
elif i>=18 and i<=23:
    print(f"Good night {name}")

