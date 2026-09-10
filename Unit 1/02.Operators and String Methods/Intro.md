# Week 02 - Operators and String Methods

## Introduction

This week, we'll be taking a look at operators and string methods in Python. Operators are special symbols that perform operations on variables and values. String methods are built-in functions that allow you to manipulate and work with strings in various ways.

## Operators

You can think of operators as mathematical symbols that perform calculations or operations on numbers and variables. For example, the `+` operator is used for addition, while the `*` operator is used for multiplication. There are also comparison operators like `==` (equal to) and `!=` (not equal to) that allow you to compare values.

There are several types of operators in Python, including:

- Arithmetic operators: `+`, `-`, `*`, `/`, `%`, `**`, `//`
1. `%` - modulus, the ;eftover of division (125%3=2)
2. `**` - power (6**3=216)
3. `//` - floor devision - rounded devision to the nearest integer (1225//3=31)
- Comparison operators: gives true or false (bool) `==`, `!=`, `>`, `<`, `>=`, `<=`
1. `==` - equal sign 
2. `!=` - not equals
3. `>`- greater (bool - t/f)
4. `<`- smaller (bool - t/f)
5. `>=`- equal or greater (bool - t/f)
6. `<=`- equal or smaller (bool - t/f)
7. `=` - asign name to the value

- Logical operators: `and`, `or`, `not`
1. `and`- they both must we  (bool -  t/f) (ex. a and b ==1 (t/f))
2. `or` 1 one them must be (bool -  t/f)  (ex. a or b ==1 (t/f) , when a is 0 and b is 1)
3. `not` - if that value is not (turns false for a value) ( if a is not 0, that it cant be 0)

You can find a complete list of operators in Python in W3Schools' [Python Operators](https://www.w3schools.com/python/python_operators.asp) page.

Examples:
1. a=8 
2. b=11
3. a and b true
4. a or b  true
5. a>b false
6. a<=b true
7. a or not a True
8. b and not a (true and false) false
- IF it has a value its always TRUE a=8 True
- NOT a is False

variable - location in memory, can hold a value and has unique identifier

## String Methods

String methods are built-in functions that allow you to manipulate and work with strings in various ways. Some common string methods include:

- `str[index]`: Accesses a character at a specific index in a string.
- `find()`: Returns the index of the first occurrence of a specified substring in a string. Returns -1 if the substring is not found.
- `rfind()`: Returns the index of the last occurrence of a specified substring in a string. Returns -1 if the substring is not found.
- `slice()`: Extracts a portion of a string based on specified start and end indices.
- `replace()`: Replaces occurrences of a specified substring with another substring.
- `split()`: Splits a string into a list of substrings based on a specified delimiter.
- `+`: Concatenates two or more strings together.
- `*`: Repeats a string a specified number of times.

IMPORTANT: String methods are called on string objects using dot notation. For example, to use the `find()` method on a string variable named `my_string`, you would write `my_string.find("substring")`.

MORE IMPORTANT: String methods do not modify the original string. Instead, they return a new string with the desired changes. Strings in Python are immutable, meaning they cannot be changed after they are created. As an example, using the `replace()` method will return a new string with the replacements, but the original string will remain unchanged. Therefore, if you want to keep the changes, you need to assign the result of the method to a new variable or overwrite the original variable.

You can find a complete list of string methods in Python in W3Schools' [Python String Methods](https://www.w3schools.com/python/python_strings_methods.asp) page.

int(input()) -- ask input from user and convert to integer  (can be float, balh blaj)

- Conditionals
1. Condition do this 
2. If, elif, else

- Multiple outcomes ex:(T,F . F,T . F,F . T,T)

- Scope , local values available only within the function (variable can not be accessed outside a function)
we can use global key word to maoe it go out of the scope of function and be accesable.
local - enclosing - global - builtin variables

- f string for printing out variables ex"  print(f"hello {number}")

- Loops:
1. "While" loop (until the statment is flase) - conditon (>) - updates the intial value and checks it
2. "For" loop (we know how many loops we need) - range(number) - just loops needed amount of time
3. Do While loop (do first check later)


Funtion is a block of code (def) - allows us to create a reusable block of code that we can call.(the function doesnt run unless its called) = cleaner code, reusable, specific logic

agrument ex: 3 (exists when we are calling the function with an argumental value for it)
print(ad_d(3))
peramiter ex: x (exists inside the function definition)
def ad_d(x):

lists
ex: 
student1= "sally"
student_list = ["sally", "marry", "bobby"]
for student in student_list:
    print student

1. collection = single "variable" used to store multiple valuables
- lists = [] #ordered and changable,duplicates
acces - print(list[n]) - value [0:n-1] , every sencond [::2], backwards [::-1]
for x in list: #for loop
    print(x)
print(dir(fruits))
print(help(l1st_name))
len(list_name) #put print
print("apple" in list_name) #T/F
list[0]=change first valye
list.appned("c)
list.remove("c)
list.sort()
fruits.reverse()
list.clear()
print(list.index("c))
list.count("x)
sum(valuesoflist)


- set= {} #unordered, immutable ,add/remove, no duplicates
print(dir(set))
print(help(set))
print(x in set)
len(set)
set.add()
set.remove()
set.pop()
set.clear()

- tuple= () #ordered and unchangable, duplicates
print(dir(tuple))

print(x in tuple)
tuple.index(x")
tple.count("x)
for x in tuple:
    print(x)

