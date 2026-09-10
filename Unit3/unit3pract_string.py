"""
Given a random string, return a list with the duplicate letters removed.
Make all letters lowercase for convenience.

hello

[h,e,l,o]

EASY = Using a loop searching the list at every letter

HARD = Using a dict to check for a key to track letters

"""

string=input("Enter a string to operate:").lower()
result = []

for letter in string:
    if letter not in result:
        result.append(letter)

print(result)

print(list(dict.fromkeys(string))) #dictionary ez