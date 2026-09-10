#1 writer 1 yapper argorithm that accepts u 
#Ceate a list that takses as many user inputs as the user asks it to, then prints the items one ny one

n=int(input("How many items will it be?:  "))
all_names=[]

for i in range(0,n):
    items_names=input("what Item u want?: ")
    all_names.append(items_names)
    
for names in all_names:
    print(f"You have item: {names}")


