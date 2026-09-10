# IB DP CompSci - Week 2 Exercise: Operators and String Methods

# ARITHMETIC OPERATORS
# Practice with basic math operations
num1 = 15
num2 = 4

# Complete the arithmetic operations
addition = num1 + num2
print(addition)

# TODO: Calculate subtraction
subtraction =num1 - num2
print(subtraction)

# TODO: Calculate multiplication
multiplication = num1 * num2
print(multiplication)

# TODO: Calculate division
division = num1/num2
print(division)

# TODO: Calculate floor division
floor_division = num1//num2
print(floor_division)

# TODO: Calculate modulus (remainder)
modulus = num1%num2
print(modulus)

# Order of operations - what will be printed?
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
print(result1)  # Write your guess as a comment
# 14
print(result2)  # Write your guess as a comment
# 20

# COMPARISON OPERATORS
# Compare ages
your_age = 16
friend_age = 17

print(your_age > friend_age)   # Are you older?
# False
print(your_age == friend_age)  # Same age?
# False
print(your_age < friend_age)   # Are you younger?
# True

# TODO: Check if you are at least 16
at_least_16 = your_age >= 16
print(at_least_16)
# True

# TODO: Check if your friend is not 18
friend_not_18 = friend_age != 18
print(friend_not_18)
#True

# LOGICAL OPERATORS
# Weather decisions
temperature = 22
is_raining = False
is_weekend = True
# weekend is false when week day 

# Can go to beach if warm and not raining
can_go_beach = temperature > 20 and not is_raining
print(can_go_beach)
# True

# TODO: Should study inside if raining OR it's a weekday
should_study = is_raining or not is_weekend
print(should_study)
# False
# is_raining == True or is_weekend == False

# TODO: Wear jacket if cold OR raining
wear_jacket = temperature<20 or is_raining
print(wear_jacket)
# False

# STRING METHODS - BASIC
# Clean up a name
messy_name = "    wonder alice   "
print(messy_name.strip().title()) #Remove spaces #Fix capitalization

#TODO: Remove spaces and fix capitalization
clean_name = "Wonder Alice"
print(clean_name)

# String information
sentence = "Python programming is fun!"
print(len(sentence))        # Length
print(sentence.upper())     # Uppercase
print(sentence.lower())     # Lowercase

# TODO: Count how many 'a' letters
count_a = sentence.count("a")
print(count_a)

# TODO: Check if starts with 'Python'
starts_python = sentence[0:6] or sentence.startswith("Python")  
print(starts_python)

# TODO: Check if ends with '!'
ends_exclamation = sentence[25] or sentence.endswith("!")

print(ends_exclamation)

# STRING METHODS - REPLACING
message = "I love Java programming"

# Replace Java with Python
new_message = message.replace("Java", "Python")
print(message)
print(new_message)

# STRING SPLITTING
full_name = "John Michael Smith"
name_parts = full_name.split()
print(name_parts)
print(name_parts[0])  # First name
print(name_parts[-1]) # Last name

# Email processing
email = "student@school.edu"
email_parts = email.split("@")
username = email_parts[0]
domain = email_parts[1]
print(username)
print(domain)

# COMBINING CONCEPTS
# Grade calculator
student = "alex johnson"
math = 85
science = 92
english = 78

#TODO: Calculate average
average = (math+science+english)/3

#TODO: Format student name
formatted_student = student.title()

print(formatted_student)
print(average)

# TODO: Check if student passed (average >= 80)
passed = average>=80
print(passed)

# String validation
test_string = "12345"

# TODO: Check if all digits
all_digits = test_string.isdecimal()
print(all_digits)

# TODO: Check if contains letters
has_letters = test_string.isalpha()
print(has_letters)

# CHALLENGE: Text analysis
text = "The quick brown fox"
words = text.split()
word_count = len(words)
char_count = len(text)

print(word_count)
print(char_count)

# Write your guesses as comments, then run and check
#4 (cuz it splitted it into 4 words)
#19 (cuz it counted all the characters including spaces)