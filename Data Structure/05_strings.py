"""
Python Strings
==============

A string is a sequence of characters enclosed within
single quotes (' '), double quotes (" "), or triple quotes.

Strings are:
- Ordered
- Immutable
- Indexable
- Sliceable
- Able to contain duplicate characters
"""

# ============================================================
# 1. Creating a String
# ============================================================

name = "Trupti"

city = 'Pune'

message = "I am learning Python."

print(name)
print(city)
print(message)


# Strings can contain different characters.

text = "Python 123 @#$"

print(text)


# Empty string

empty_string = ""

print(empty_string)


# ============================================================
# 2. Single Quotes vs Double Quotes
# ============================================================

name = "Trupti"

name = 'Trupti'

# Both create a string.

print(name)


# Double quotes are useful when the string contains
# a single quote.

message = "It's a Python course."

print(message)


# Single quotes can be used when the string contains
# double quotes.

message = 'She said "Hello".'

print(message)


# ============================================================
# 3. Multi-line Strings
# ============================================================

message = """
Python is easy to learn.
Python is useful for Data Engineering.
Python is also useful for Data Analysis.
"""

print(message)


# Triple quotes can also use single quotes.

message = '''
This is a
multi-line string.
'''

print(message)


# ============================================================
# 4. String Indexing
# ============================================================

language = "Python"

# Indexing starts from 0.

print(language[0])
# P

print(language[1])
# y

print(language[5])
# n


# Negative indexing starts from -1.

print(language[-1])
# n

print(language[-2])
# o


# Index positions:
#
# P  y  t  h  o  n
# 0  1  2  3  4  5
#
# -6 -5 -4 -3 -2 -1


# ============================================================
# 5. String Slicing
# ============================================================

language = "Python"

print(language[0:3])
# Pyt

print(language[2:5])
# tho

print(language[:3])
# Pyt

print(language[3:])
# hon

print(language[:])
# Python


# General syntax:
#
# string[start:stop:step]
#
# stop index is NOT included.


# ============================================================
# 6. String Slicing with Step
# ============================================================

text = "Python"

print(text[::2])
# Pto

print(text[1::2])
# yhn


# ============================================================
# 7. Reversing a String
# ============================================================

text = "Python"

print(text[::-1])
# nohtyP


# ============================================================
# 8. Strings Are Immutable
# ============================================================

text = "Python"

# Strings cannot be modified directly.

# text[0] = "J"

# This raises:
# TypeError: 'str' object does not support item assignment


# Instead, create a new string.

text = "J" + text[1:]

print(text)
# Jython


# ============================================================
# 9. String Length
# ============================================================

text = "Python"

print(len(text))
# 6


# len() returns the number of characters.


# ============================================================
# 10. String Concatenation
# ============================================================

first_name = "Trupti"
last_name = "Jadhav"

full_name = first_name + " " + last_name

print(full_name)
# Trupti Jadhav


# ============================================================
# 11. String Repetition
# ============================================================

text = "Python "

print(text * 3)
# Python Python Python


# ============================================================
# 12. Membership Checking
# ============================================================

text = "Python Programming"

print("Python" in text)
# True

print("Java" in text)
# False

print("Java" not in text)
# True


# ============================================================
# 13. lower()
# ============================================================

text = "PYTHON"

print(text.lower())
# python


# Useful for case-insensitive comparisons.

name = "TrUpTi"

print(name.lower())
# trupti


# ============================================================
# 14. upper()
# ============================================================

text = "python"

print(text.upper())
# PYTHON


# ============================================================
# 15. capitalize()
# ============================================================

text = "python programming"

print(text.capitalize())
# Python programming


# ============================================================
# 16. title()
# ============================================================

text = "python programming language"

print(text.title())
# Python Programming Language


# ============================================================
# 17. swapcase()
# ============================================================

text = "PyThOn"

print(text.swapcase())
# pYtHoN


# ============================================================
# 18. strip()
# ============================================================

text = "   Python   "

print(text.strip())
# Python


# strip() removes whitespace from both ends.


# ============================================================
# 19. lstrip()
# ============================================================

text = "   Python"

print(text.lstrip())
# Python


# Removes whitespace from the left side.


# ============================================================
# 20. rstrip()
# ============================================================

text = "Python   "

print(text.rstrip())
# Python


# Removes whitespace from the right side.


# ============================================================
# 21. replace()
# ============================================================

text = "I love Java"

new_text = text.replace("Java", "Python")

print(new_text)
# I love Python


# replace() returns a new string.
# The original string is not modified.


# ============================================================
# 22. split()
# ============================================================

text = "Python SQL Pandas"

words = text.split()

print(words)
# ['Python', 'SQL', 'Pandas']


# split() converts a string into a list.


# ============================================================
# 23. split() with a Separator
# ============================================================

data = "Python,SQL,Pandas"

skills = data.split(",")

print(skills)
# ['Python', 'SQL', 'Pandas']


# Another example:

date = "2026-08-12"

parts = date.split("-")

print(parts)
# ['2026', '08', '12']


# ============================================================
# 24. join()
# ============================================================

skills = ["Python", "SQL", "Pandas"]

result = ", ".join(skills)

print(result)
# Python, SQL, Pandas


# join() combines elements of an iterable into a string.


# ============================================================
# 25. split() vs join()
# ============================================================

text = "Python,SQL,Pandas"

# String -> List

skills = text.split(",")

print(skills)
# ['Python', 'SQL', 'Pandas']


# List -> String

result = ", ".join(skills)

print(result)
# Python, SQL, Pandas


# ============================================================
# 26. find()
# ============================================================

text = "Python Programming"

print(text.find("Python"))
# 0

print(text.find("Programming"))
# 7

print(text.find("Java"))
# -1


# find() returns -1 if the substring is not found.


# ============================================================
# 27. index()
# ============================================================

text = "Python Programming"

print(text.index("Python"))
# 0


# Difference:

# find() -> returns -1 if not found
# index() -> raises ValueError if not found


# Example:

print(text.find("Java"))
# -1

# print(text.index("Java"))
# ValueError


# ============================================================
# 28. startswith()
# ============================================================

text = "Python Programming"

print(text.startswith("Python"))
# True

print(text.startswith("Java"))
# False


# ============================================================
# 29. endswith()
# ============================================================

filename = "data.csv"

print(filename.endswith(".csv"))
# True

print(filename.endswith(".json"))
# False


# This is useful when working with files.


# ============================================================
# 30. count()
# ============================================================

text = "banana"

print(text.count("a"))
# 3

print(text.count("n"))
# 2


# count() returns the number of occurrences.


# ============================================================
# 31. isalpha()
# ============================================================

text = "Python"

print(text.isalpha())
# True


text = "Python123"

print(text.isalpha())
# False


# isalpha() checks whether all characters are alphabetic.


# ============================================================
# 32. isdigit()
# ============================================================

text = "12345"

print(text.isdigit())
# True


text = "123abc"

print(text.isdigit())
# False


# isdigit() checks whether all characters are digits.


# ============================================================
# 33. isalnum()
# ============================================================

text = "Python123"

print(text.isalnum())
# True


text = "Python 123"

print(text.isalnum())
# False


# isalnum() checks for only letters and numbers.
# Spaces and special characters make it False.


# ============================================================
# 34. isspace()
# ============================================================

text = "   "

print(text.isspace())
# True


text = "Python"

print(text.isspace())
# False


# ============================================================
# 35. islower() and isupper()
# ============================================================

text = "python"

print(text.islower())
# True

text = "PYTHON"

print(text.isupper())
# True


# ============================================================
# 36. f-Strings
# ============================================================

name = "Trupti"
age = 22

message = f"My name is {name} and I am {age} years old."

print(message)
# My name is Trupti and I am 22 years old.


# f-strings are a clean way to insert variables
# into strings.


# ============================================================
# 37. Expressions in f-Strings
# ============================================================

price = 100
quantity = 5

message = f"Total price: {price * quantity}"

print(message)
# Total price: 500


# ============================================================
# 38. Formatting Numbers with f-Strings
# ============================================================

price = 1234.5678

print(f"Price: {price:.2f}")
# Price: 1234.57


# ============================================================
# 39. Escape Characters
# ============================================================

# New line

print("Python\nSQL")


# Tab

print("Python\tSQL")


# Backslash

print("C:\\Users\\Trupti")


# Double quote inside a string

print("She said \"Hello\".")


# Single quote inside a string

print('It\'s Python.')


# ============================================================
# 40. Raw Strings
# ============================================================

# Raw strings treat backslashes as normal characters.

path = r"C:\Users\Trupti\Documents"

print(path)


# Raw strings are useful when working with
# Windows file paths and regular expressions.


# ============================================================
# 41. Comparing Strings
# ============================================================

print("Python" == "Python")
# True

print("Python" == "python")
# False

print("Python" != "Java")
# True


# String comparison is case-sensitive.


# ============================================================
# 42. Case-Insensitive Comparison
# ============================================================

name1 = "Python"
name2 = "python"

print(name1.lower() == name2.lower())
# True


# casefold() can also be used for more robust
# case-insensitive comparisons.

print(name1.casefold() == name2.casefold())
# True


# ============================================================
# 43. Removing Extra Spaces
# ============================================================

name = "   Trupti   "

clean_name = name.strip()

print(clean_name)
# Trupti


# This is very common during data cleaning.


# ============================================================
# 44. Cleaning Text
# ============================================================

text = "  Python Programming  "

cleaned_text = text.strip().lower()

print(cleaned_text)
# python programming


# Multiple string methods can be chained.


# ============================================================
# 45. Cleaning CSV-like Data
# ============================================================

data = " Trupti , Pune , Python "

parts = data.split(",")

cleaned = [item.strip() for item in parts]

print(cleaned)

# ['Trupti', 'Pune', 'Python']


# ============================================================
# 46. Checking File Extensions
# ============================================================

filename = "sales_data.csv"

if filename.endswith(".csv"):
    print("CSV file")

if filename.endswith(".json"):
    print("JSON file")


# Useful when processing files in Data Engineering.


# ============================================================
# 47. Extracting File Name
# ============================================================

path = "data/sales/customer_data.csv"

filename = path.split("/")[-1]

print(filename)
# customer_data.csv


# Note:
# pathlib is better for real file-path handling.
# This example is only for string manipulation.


# ============================================================
# 48. String Formatting with Multiple Values
# ============================================================

name = "Trupti"
role = "Data Engineer"
city = "Pune"

message = f"{name} is working as a {role} in {city}."

print(message)


# ============================================================
# 49. String Length and Whitespace
# ============================================================

text = " Python "

print(len(text))
# 8

print(len(text.strip()))
# 6


# ============================================================
# 50. Strings and Iteration
# ============================================================

text = "Python"

for character in text:
    print(character)


# Output:
# P
# y
# t
# h
# o
# n


# ============================================================
# 51. Counting Characters
# ============================================================

text = "banana"

count = {}

for character in text:
    if character in count:
        count[character] += 1
    else:
        count[character] = 1

print(count)

# {
#     'b': 1,
#     'a': 3,
#     'n': 2
# }


# ============================================================
# 52. String Comprehension-like Processing
# ============================================================

text = "Python"

uppercase_characters = [
    character.upper()
    for character in text
]

print(uppercase_characters)

# ['P', 'Y', 'T', 'H', 'O', 'N']


# ============================================================
# 53. Useful String Methods Summary
# ============================================================

text = "Python Programming"

print(text.lower())
print(text.upper())
print(text.title())
print(text.strip())
print(text.replace("Python", "Java"))
print(text.split())
print(text.find("Python"))
print(text.startswith("Python"))
print(text.endswith("Programming"))
print(text.count("m"))


# ============================================================
# 54. Common String Method Differences
# ============================================================

# strip()
# Removes whitespace from both ends.

# replace()
# Replaces one substring with another.

# split()
# Converts string -> list.

# join()
# Converts iterable elements -> string.

# find()
# Returns position; returns -1 if not found.

# index()
# Returns position; raises ValueError if not found.

# lower()
# Converts characters to lowercase.

# upper()
# Converts characters to uppercase.


# ============================================================
# 55. String vs List
# ============================================================

# String:
# - Ordered
# - Immutable
# - Indexable
# - Sliceable
# - Stores characters/text
#
# List:
# - Ordered
# - Mutable
# - Indexable
# - Sliceable
# - Can store different data types


# Example:

text = "Python"

# text[0] = "J"
# Not allowed because strings are immutable.


skills = ["Python", "SQL"]

skills[0] = "Java"

print(skills)
# ['Java', 'SQL']


# ============================================================
# 56. Data Engineering Use Cases
# ============================================================

# Strings are commonly used for:
#
# - Cleaning text data
# - Processing CSV values
# - File names and extensions
# - API response values
# - Log messages
# - Data validation
# - Parsing dates
# - Extracting information
# - Creating SQL queries
# - Working with JSON text
# - Preparing data before loading into databases


# Example: Cleaning a customer name

customer_name = "   trupti jadhav   "

cleaned_name = customer_name.strip().title()

print(cleaned_name)
# Trupti Jadhav


# Example: Validating email

email = "trupti@example.com"

if "@" in email and "." in email:
    print("Possible valid email")


# ============================================================
# 57. String Processing Example
# ============================================================

data = "  Python, SQL, Pandas, Airflow  "

# Step 1: Remove extra spaces

data = data.strip()

# Step 2: Split into individual values

skills = data.split(",")

# Step 3: Remove spaces around each value

skills = [skill.strip() for skill in skills]

# Step 4: Convert to lowercase

skills = [skill.lower() for skill in skills]

print(skills)

# ['python', 'sql', 'pandas', 'airflow']


# ============================================================
# 58. Time Complexity
# ============================================================

# For strings:

# Access by index       -> O(1)
# Search                -> O(n)
# len()                 -> O(1)
# Concatenation         -> O(n)
# Slicing               -> O(k)
# lower()/upper()       -> O(n)
# replace()             -> O(n)
# split()               -> O(n)
# join()                -> O(n)


# ============================================================
# 59. KEY TAKEAWAYS
# ============================================================

# 1. Strings are ordered sequences of characters.
# 2. Strings are immutable.
# 3. Strings support indexing and slicing.
# 4. Indexing starts from 0.
# 5. Negative indexing starts from -1.
# 6. [::-1] can reverse a string.
# 7. len() returns the number of characters.
# 8. lower() and upper() change letter case.
# 9. strip() removes whitespace from both ends.
# 10. replace() replaces text.
# 11. split() converts a string into a list.
# 12. join() combines iterable elements into a string.
# 13. find() returns -1 when text is not found.
# 14. index() raises ValueError when text is not found.
# 15. startswith() and endswith() are useful for validation.
# 16. f-strings are useful for string formatting.
# 17. Strings are very important for data cleaning.
# 18. Strings are commonly used with CSV, JSON, APIs and logs.
# 19. String operations are frequently used in Data Engineering.