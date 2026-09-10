##SEC 1

#Declaration: Declare a list of integers named scores that can hold exactly 5 elements. Initialise it with the values 85, 92, 78, 95, and 88.
scores = [0]*5
scores = [85,92,78,95,88]
#Access: Print the third element of the scores list.
print(scores[2])
#Modification: Change the value of the first element in scores to 100. Then, print the entire list to verify the change.
scores[0]=100
print(scores)
#Traversal: Write a for loop to print every element in the scores list.
for elemet in scores :
    print(elemet)
#Sum: Write a program that calculates and prints the sum of all elements in the scores list.
sum=0
for elements in scores:
    sum+=elements
print(sum)
#  Average: Write a program that calculates and prints the average of all elements in the scores list.
def average(list):
    avg =sum / len(list)
    return avg
print(average(scores))
#  Find Highest: Write a program to find and print the highest score in the scores list.
maxi=0
def highest(x):
    global maxi
    for num in x:
        if num>maxi:
            maxi=num
        else:
            maxi=maxi

    print(maxi)
highest(scores)
#Find Lowest: Write a program to find and print the lowest score in the scores list.
 
def lowest(x):
    global maxi
    lowest=scores[0]
    for num in x:
        if num<lowest:
            lowest=num
    print(lowest)
lowest(scores)
#Search: Ask the user for an integer. Check if that number exists in the scores list and print a message indicating whether it was found or not.
search=int(input("provide your number"))
err=0
for num in scores:
    if num==search:
        print("there is your number in the score")
    else:
        err+=1
if err==5 :
    print("there is no number in the score")
#  Copy: Create a new list called new_scores that is a copy of the scores list. Change an element in new_scores and print both lists to show they are independent.
new_scores= [100,92,78,95,88]
new_scores[2]=33
print(new_scores)
print(scores)
    

       




