def shopping_experience(customer):#define the whole function to later on  be anle to use in a larger code.
    global wallet #to be able to use the wallet variable from outside the function
    
    total_cost=0
    item_all=[] #write down initial values and initial required inputs for the later operations.

    def manage_items(items_name): # to separate list organization in a function, apart from other code
        item_all.append(items_name)
        return item_all
    
    items_name=input("Which item do you wanna purchase?: ")

    while items_name.lower()!="done" :  #continue the started action, while ensuring input is not "done"
        if wallet>0: #checking if there is money in wallet to continue shopping
            cost_item=int(input("What is the cost of that item in zl?"))
            if cost_item<=wallet : #checking if the cost is less than total money in wallet
                wallet-=cost_item # calculationg left overs and bought things
                total_cost+=cost_item
                manage_items(items_name) #running the function that adds the item to a list
                print(f"{items_name} was purchased for {cost_item} zl, you have {wallet} zl left in your wallet")#all results after each item
            elif cost_item>wallet and wallet!=0 :#if wallet has no enough money all actions stop and we get the summary
                print(f"here is not enough money to affort {items_name}, try buying another item with lower cost")

        elif wallet==0 : #if wallet has no enough money all actions stop and we get the summary
            print(f"You ran out of money, there is 0 dollars in your waller")
            break
        items_name=input("Which item do you wanna purchase?: ")#start the same process again
    print(f"Dear {customer} your shopping is complete")#summary
    print("You bought:")
    #how many items we bough
    print(*(f" {item} item " for item in item_all), sep="\n") if len(item_all)>0 else print ("You didnt buy anything.")



    print(f"You have {wallet} zl remaining in your wallet, and you`ve spent {total_cost}zl. \n Thank you for shopping with us!")

customer=input("Before we begin, please enter you name!:")#the outside of the function
wallet=int(input(f"Hello {customer}, how much money you have in your wallet?: "))
shopping_experience(customer)#calls our whole shopping function with our name in in.
    
