print("what is the value of your basket?")
input_value=input("")

def basket_value(input_value):
    float(input_value)
    return float(input_value)
if float(input_value)>1000:
    print("you have a discount")
   

percent="1.5"
percent2="1.1"
discounted_value1= float(input_value)/1.5
discounted_value2= float(input_value)/1.1
discounted_value3= (((float(input_value))/1.1)/1.5)

store_member=(input("are you a store member? True or False: "))
if store_member==("True"):
    store_member=True
if store_member == ("False"):
    store_member=False
else : print("Run again and input correct value of True or False")
    


if store_member==True and float(input_value)<1000:
    print("your total cost is", discounted_value1)
elif store_member==True and float(input_value)>1000:
    print("your total cost is:", discounted_value3)
elif store_member==False and float(input_value)<1000:
    print("your total cost is:", input_value)
elif store_member==False and float(input_value)>1000:
    print("your total cost is:", discounted_value2)