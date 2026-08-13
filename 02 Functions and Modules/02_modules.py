"""
Python Modules
==============

A module is a Python file (.py) that contains code such as:

- Variables
- Functions
- Classes
- Constants

Modules allow us to organize code into separate files and
reuse that code in other Python programs.

Example:

    my_module.py

can be imported into another Python file and its functions
or variables can be used there.
"""


# ============================================================
# 1. What is a Module?
# ============================================================

# Any Python file with a .py extension can act as a module.

# Example:
#
# calculator.py
#
# def add(a, b):
#     return a + b
#
#
# Then another Python file can import calculator.py.


# ============================================================
# 2. Why Use Modules?
# ============================================================

# Modules help us:
#
# - Organize code
# - Reuse code
# - Avoid writing the same code repeatedly
# - Keep large projects manageable
# - Separate different responsibilities
# - Make code easier to test and maintain
#
# In Data Engineering, modules can be used to separate:
#
# - Data cleaning functions
# - Validation functions
# - File handling functions
# - API functions
# - Database functions
# - Configuration utilities


# ============================================================
# 3. Importing a Module
# ============================================================

# Python provides many built-in modules.

import math


print(math.sqrt(25))
print(math.pi)


# Output:
# 5.0
# 3.141592...


# 'math' is a module.
#
# The dot operator is used to access objects
# inside the module.


# ============================================================
# 4. Using Functions from a Module
# ============================================================

import math


number = 16

result = math.sqrt(number)

print(result)


# General syntax:
#
# module_name.function_name()


# ============================================================
# 5. Importing Multiple Modules
# ============================================================

import math
import random


print(math.sqrt(100))

print(random.randint(1, 10))


# Multiple modules can be imported into the same file.


# ============================================================
# 6. Importing a Specific Function
# ============================================================

from math import sqrt


print(sqrt(25))


# Instead of:

# math.sqrt(25)

# We can directly use:

# sqrt(25)


# ============================================================
# 7. Importing Multiple Functions
# ============================================================

from math import sqrt, floor, ceil


print(sqrt(25))

print(floor(4.8))

print(ceil(4.2))


# Only the required functions are imported.


# ============================================================
# 8. Importing Everything
# ============================================================

# You may see:

# from math import *

# However, this is generally NOT recommended.

# Why?
#
# It can make it difficult to know where a function came from.
#
# Better:

import math

print(math.sqrt(25))


# ============================================================
# 9. Import Aliasing
# ============================================================

import math as m


print(m.sqrt(25))

print(m.pi)


# 'as' gives the module a shorter or custom name.


# ============================================================
# 10. Function Aliasing
# ============================================================

from math import sqrt as square_root


print(square_root(36))


# Here:
#
# sqrt
# becomes
# square_root


# ============================================================
# 11. Common Built-in / Standard Library Modules
# ============================================================

# Some useful Python modules include:
#
# math
# datetime
# os
# pathlib
# json
# csv
# random
# statistics
# logging
#
# These modules are part of Python's standard library.


# ============================================================
# 12. math Module
# ============================================================

import math


print(math.sqrt(49))

print(math.pow(2, 3))

print(math.ceil(4.2))

print(math.floor(4.8))

print(math.pi)


# ============================================================
# 13. random Module
# ============================================================

import random


number = random.randint(1, 100)

print(number)


# Generate a random choice:

names = ["Trupti", "Rahul", "Priya"]

selected_name = random.choice(names)

print(selected_name)


# ============================================================
# 14. datetime Module
# ============================================================

import datetime


today = datetime.date.today()

print(today)


current_time = datetime.datetime.now()

print(current_time)


# Modules such as datetime are very useful in
# Data Engineering for:
#
# - File timestamps
# - ETL execution dates
# - Partition dates
# - Data processing windows


# ============================================================
# 15. os Module
# ============================================================

import os


current_directory = os.getcwd()

print(current_directory)


# os is commonly used for:
#
# - Environment variables
# - File paths
# - Directory operations
# - Operating-system related tasks


# ============================================================
# 16. pathlib Module
# ============================================================

from pathlib import Path


current_path = Path.cwd()

print(current_path)


# pathlib provides an object-oriented way
# to work with files and directories.


# ============================================================
# 17. json Module
# ============================================================

import json


data = {
    "name": "Trupti",
    "role": "Data Engineer"
}


json_data = json.dumps(data)

print(json_data)


# json is commonly used when working with:
#
# - APIs
# - Configuration files
# - JSON datasets
# - Data exchange


# ============================================================
# 18. Importing Your Own Module
# ============================================================

# Suppose you have this file:
#
# calculator.py
#
# def add(a, b):
#     return a + b
#
#
# And another file:
#
# main.py
#
# You can write:
#
# import calculator
#
# result = calculator.add(10, 20)
#
# print(result)


# The module must generally be accessible from
# the current project / Python import path.


# ============================================================
# 19. Example: Creating a Simple Utility Module
# ============================================================

# Create a file named:
#
# utility.py
#
# Add:

# def clean_name(name):
#     return name.strip().title()
#
#
# def calculate_average(numbers):
#     return sum(numbers) / len(numbers)


# Then create another file:
#
# main.py


# Import the utility module:

# import utility


# Use its functions:

# print(utility.clean_name("  trupti  "))

# print(utility.calculate_average([10, 20, 30]))


# ============================================================
# 20. Utility Module Structure
# ============================================================

# A simple project can look like:
#
# project/
#
#     main.py
#
#     utility.py
#
#
# utility.py:
#
# def clean_name(name):
#     return name.strip().title()
#
#
# def calculate_average(numbers):
#     return sum(numbers) / len(numbers)
#
#
# main.py:
#
# import utility
#
# print(utility.clean_name(" trupti "))
#
# print(utility.calculate_average([10, 20, 30]))


# ============================================================
# 21. Importing Specific Functions from Your Module
# ============================================================

# If utility.py contains:
#
# def clean_name(name):
#     return name.strip().title()
#
#
# def calculate_average(numbers):
#     return sum(numbers) / len(numbers)


# You can write in main.py:

# from utility import clean_name


# print(clean_name("  trupti  "))


# You only import the function you need.


# ============================================================
# 22. Importing Multiple Functions from Your Module
# ============================================================

# from utility import clean_name, calculate_average
#
#
# print(clean_name("  trupti  "))
#
# print(calculate_average([10, 20, 30]))


# ============================================================
# 23. Aliasing Your Own Module
# ============================================================

# import utility as util
#
#
# print(util.clean_name("  trupti  "))
#
# print(util.calculate_average([10, 20, 30]))


# ============================================================
# 24. Creating a Data Cleaning Utility Module
# ============================================================

# This is a useful Data Engineering example.
#
# File:
#
# data_utils.py
#
#
# def clean_string(value):
#     return value.strip().lower()
#
#
# def clean_name(value):
#     return value.strip().title()
#
#
# def remove_duplicates(values):
#     return list(set(values))


# Then in another file:
#
# from data_utils import clean_string, clean_name
#
#
# name = clean_name("  TRUPTI  ")
#
# city = clean_string("  PUNE  ")
#
#
# print(name)
# print(city)


# ============================================================
# 25. Creating a Validation Utility Module
# ============================================================

# File:
#
# validation_utils.py
#
#
# def check_required_columns(expected, actual):
#
#     return expected.issubset(actual)
#
#
# def check_duplicates(values):
#
#     return len(values) != len(set(values))


# Then:

# from validation_utils import check_required_columns
#
#
# expected = {"id", "name", "email"}
#
# actual = {"id", "name", "email", "salary"}
#
#
# print(
#     check_required_columns(expected, actual)
# )


# ============================================================
# 26. __name__
# ============================================================

# Every Python module has a special variable:

# __name__


# When a Python file is executed directly:

# __name__ == "__main__"


# When the file is imported:

# __name__ contains the module's name.


# ============================================================
# 27. if __name__ == "__main__"
# ============================================================

# Example:

# def add(a, b):
#     return a + b
#
#
# if __name__ == "__main__":
#
#     print(add(10, 20))


# The code inside this block runs when the file
# is executed directly.


# ============================================================
# 28. Why Use __name__ == "__main__"?
# ============================================================

# Suppose calculator.py contains:
#
# def add(a, b):
#     return a + b
#
#
# if __name__ == "__main__":
#     print(add(10, 20))


# If we run:
#
# python calculator.py
#
# the example code executes.
#
#
# But if another file does:
#
# import calculator
#
# the example code inside the main block
# does not execute automatically.


# This allows a file to work both as:
#
# 1. A reusable module
# 2. A directly executable script


# ============================================================
# 29. Complete Utility Module Example
# ============================================================

# Suppose we create:
#
# data_utils.py
#
#
# def clean_name(name):
#     return name.strip().title()
#
#
# def calculate_average(numbers):
#
#     if not numbers:
#         return 0
#
#     return sum(numbers) / len(numbers)
#
#
# def validate_email(email):
#
#     return "@" in email
#
#
# if __name__ == "__main__":
#
#     print(clean_name("  trupti  "))
#
#     print(calculate_average([10, 20, 30]))
#
#     print(validate_email("test@example.com"))


# Then another file can use:
#
# from data_utils import clean_name
# from data_utils import calculate_average
# from data_utils import validate_email
#
#
# print(clean_name("  trupti  "))
#
# print(calculate_average([10, 20, 30]))
#
# print(validate_email("test@example.com"))


# ============================================================
# 30. Modules in Data Engineering
# ============================================================

# In a Data Engineering project, you might organize code like:
#
# data_pipeline/
#
#     main.py
#
#     config.py
#
#     data_utils.py
#
#     validation_utils.py
#
#     api_utils.py
#
#     file_utils.py
#
#     database_utils.py
#
#
# Each module has a specific responsibility.


# Example:
#
# data_utils.py
# -> Data cleaning and transformation
#
# validation_utils.py
# -> Data validation
#
# api_utils.py
# -> API requests
#
# file_utils.py
# -> File handling
#
# database_utils.py
# -> Database operations
#
# config.py
# -> Configuration values


# ============================================================
# 31. Module vs Function
# ============================================================

# Function:
# A reusable block of code that performs a specific task.
#
#
# Module:
# A Python file that can contain functions,
# variables, classes, and other code.


# Example:
#
# data_utils.py
#
#     clean_name()
#     clean_email()
#     remove_duplicates()
#
#
# data_utils.py is the module.
#
# clean_name(), clean_email(), and remove_duplicates()
# are functions inside that module.


# ============================================================
# 32. Module vs Library
# ============================================================

# A module is generally a single Python file.
#
# A package is a collection of related Python modules.
#
# A library is a broader collection of reusable code.
#
#
# For now, remember:
#
# Module
# -> Usually one .py file
#
# Package
# -> Collection of modules
#
# Library
# -> Reusable collection of code


# ============================================================
# 33. Importing a Module Multiple Times
# ============================================================

# Python generally loads a module once during a program's
# execution and reuses the loaded module.
#
# You normally don't need to worry about importing
# the same module multiple times.


# ============================================================
# 34. Common Import Style
# ============================================================

# Recommended:

import math

result = math.sqrt(25)


# Also common:

from pathlib import Path

path = Path("data.csv")


# Avoid unnecessary:

# from math import *


# Explicit imports make code easier to understand.


# ============================================================
# 35. Module Naming
# ============================================================

# Module names should generally:
#
# - Be lowercase
# - Be descriptive
# - Use underscores when needed
# - Avoid spaces
#
#
# Good:
#
# data_utils.py
# file_utils.py
# api_utils.py
# validation_utils.py
#
#
# Avoid:
#
# My File.py
# Data Utility File.py


# ============================================================
# 36. Practical Data Engineering Project Structure
# ============================================================

# Example:
#
# data_pipeline/
#
#     main.py
#
#     data_utils.py
#     validation_utils.py
#     file_utils.py
#     api_utils.py
#
#     data/
#         customers.csv
#         orders.csv
#
#
# main.py can import functions from the utility modules.


# ============================================================
# 37. Example Data Pipeline Using Modules
# ============================================================

# data_utils.py:
#
# def clean_name(name):
#     return name.strip().title()
#
#
# validation_utils.py:
#
# def validate_id(customer_id):
#     return customer_id is not None
#
#
# main.py:
#
# from data_utils import clean_name
# from validation_utils import validate_id
#
#
# name = clean_name("  trupti  ")
#
# valid = validate_id(101)
#
#
# print(name)
# print(valid)


# This separates responsibilities and keeps
# main.py cleaner.


# ============================================================
# 38. Important Module Concepts
# ============================================================

# import module
# -> Imports the complete module.
#
# from module import function
# -> Imports a specific function.
#
# import module as alias
# -> Gives a module a shorter name.
#
# __name__
# -> Special variable containing the module's name.
#
# __main__
# -> Indicates that the file is being executed directly.


# ============================================================
# 39. Key Takeaways
# ============================================================

# 1. A module is a Python file containing reusable code.
#
# 2. Modules help organize large programs.
#
# 3. Use import to import a module.
#
# 4. Use from ... import to import specific objects.
#
# 5. Use as to create an alias.
#
# 6. Python provides many useful standard-library modules.
#
# 7. You can create your own modules.
#
# 8. Utility modules are useful for reusable functions.
#
# 9. __name__ tells us how the module is being used.
#
# 10. if __name__ == "__main__" allows code to run
#     only when the file is executed directly.
#
# 11. Modules help separate responsibilities.
#
# 12. Data Engineering projects commonly use utility
#     modules for cleaning, validation, APIs, files,
#     databases, and configuration.


