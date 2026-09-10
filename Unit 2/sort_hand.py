list_tosort=[5,4,3,6,1,2,7,9,10,8]
while list_tosort!=[1,2,3,4,5,6,7,8,9,10]:
    for x in list_tosort:
        ind=int(list_tosort.index(x))
        if ind!=9:
            ind2=ind+1
            if x>list_tosort[ind2]:
                list_tosort.pop(ind)
                list_tosort.insert(ind2,x)

print(list_tosort)

##Types of sorting algorithms , bubble sort, section sort, quick sort.

