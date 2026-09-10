#Find the biggest element(maximum) in a list. All items will be integers . Your solution should be a finction that takes a parameter.



def element_list1(n):
    list1.append(n)
    return list1

def maximum_value(list1):
    max_v=list1[0]
    for num in list1:
        if num>max_v:
            max_v=num
    print(f"The maximum value in the list is: {max_v}")
    
list1=[]
length=int(input("how many numbers will be in the list?: "))
for i in range (0,length):
    n=int(input("Enter a numeber that must be added to the list: "))
    if n<0:
        print("Only positive numbers, try again")
        n=int(input("Enter a numeber that must be added to the list: "))
    element_list1(n)
maximum_value(list1)