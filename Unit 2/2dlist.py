#1.Find  the global maximum in a 2d list
#2.Find the local maximum in every list within a 2d list
#3. 2d list : [[1,2,3],[12,18,23],[41,11,26]]
#You can create a new list which will hold the maximums in each row


def max_inrow(number_grade):
    for row in number_grade:
        max_v=row[0]
        for num in row:
            if num>max_v:
                max_v=num
        max_list.append(max_v)  
        print(f"the max value in {row} is: {max_v}")
    number_grade.append(max_list)
    print(max_list)
        

def global_max(number_grade):
    max_v=number_grade[0][0]
    for row in number_grade:
        for num in row:
            if num>max_v:
                max_v=num
    print(f"the global max value of the 2d list is : {max_v}")

number_grade=[[1,2,3],[12,18,23],[41,11,26]]
max_list=[]
max_inrow(number_grade)
global_max(number_grade)

new_list=[n*5 for n in range(0,8994) if n%3==0 ]
print(new_list)