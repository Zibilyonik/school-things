print("what is the value of your basket?")
input_value=float(input(""))

basket_value=input_value
print(input_value)
if input_value>1000:
    print("you have a discount")
   

# percent1=0.5
# percent2=0.9
discounted_value1= input_value*0.5 # 50% discount
discounted_value2= input_value*0.9 #10% discount
discounted_value3= input_value*0.5*0.9 #60% discount

store_member=(input("are you a store member? True or False: "))
if store_member==("True"):
    store_member=True
if store_member == ("False"):
    store_member=False
else : print("Run again and input correct value of True or False")
    


if store_member==True and float(input_value)<1000:
    print("your total cost is", discounted_value1)
    
if store_member==True and float(input_value)>1000:
    print("your total cost is:", discounted_value3)

if store_member==False and float(input_value)<1000:
    print("your total cost is:", input_value)

if store_member==False and float(input_value)>1000:
    print("your total cost is:", discounted_value2)
    
   




    