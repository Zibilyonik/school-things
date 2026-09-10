mystack=[]

def my_push(calue):
    global mystack
    mystack.append(calue)
    print(mystack)

def my_pop():
    global mystack
    a=mystack[-1]
    mystack.pop()
    print(mystack)


my_push(55)
my_push(78)
my_push(22)
my_pop()

########## OTHER EXAMPLE ############

mystack=[]

def my_push(x):
    global mystack
    mystack= [*mystack, x]
    return mystack

def my_pop():
    global mystack
    a=mystack[-1]
    mystack= mystack[:1]
    return mystack


my_push(55)
my_push(78)
my_push(22)
my_pop()



############ Qeueue example ###########

my_queue=[]
def my_enqueue(v):
    global my_queue
    my_queue=[v, *my_queue]
    return my_queue

def my_dequeue():
    global my_queue
    fi=my_queue[0]
    my_queue=my_queue[1:]
    return my_queue

print(my_enqueue(5))
print(my_enqueue(10))
print(my_enqueue(15))   
print(my_dequeue())
print(my_dequeue())
