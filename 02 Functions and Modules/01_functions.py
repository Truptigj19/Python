"""
Python Functions
================

A function is a reusable block of code designed to perform
a specific task.

Functions help us:
- Reuse code
- Avoid repetition
- Organize code
- Improve readability
- Make debugging easier
- Make testing easier

Functions are especially important in Data Engineering because
the same cleaning, validation, transformation, or processing
logic may need to be used multiple times.
"""


# ============================================================
# 1. Creating a Function
# ============================================================

def greet():
    print("Hello, Trupti")


# Calling the function

greet()


# A function is created using the 'def' keyword.

# General syntax:
#
# def function_name():
#     function body


# Important:
# Defining a function does NOT execute it.
# The function executes only when it is called.


# ============================================================
# 2. Function with Parameters
# ============================================================

def greet(name):
    print("Hello", name)


greet("Trupti")
greet("Rahul")


# 'name' is a parameter.
#
# "Trupti" and "Rahul" are arguments.


# ============================================================
# 3. Parameter vs Argument
# ============================================================

def add(a, b):
    return a + b


result = add(10, 20)

print(result)


# a and b
# -> Parameters
#
# 10 and 20
# -> Arguments


# Parameter:
# A variable written in the function definition.
#
# Argument:
# The actual value passed while calling the function.


# ============================================================
# 4. Multiple Parameters
# ============================================================

def employee_info(name, age, role):
    print("Name:", name)
    print("Age:", age)
    print("Role:", role)


employee_info("Trupti", 22, "Data Engineer")


# A function can accept multiple parameters.


# ============================================================
# 5. Return Values
# ============================================================

def add(a, b):
    return a + b


result = add(10, 20)

print(result)


# 'return' sends a value back to the caller.


# ============================================================
# 6. print() vs return
# ============================================================

def add_using_print(a, b):
    print(a + b)


result = add_using_print(10, 20)

print(result)

# Output:
# 30
# None


def add_using_return(a, b):
    return a + b


result = add_using_return(10, 20)

print(result)

# Output:
# 30


# print()
# -> Displays a value.
#
# return
# -> Sends a value back to the caller.
#
# For reusable functions, return is usually more useful
# than printing the result inside the function.


# ============================================================
# 7. Function with No Return
# ============================================================

def greet():
    print("Hello")


result = greet()

print(result)

# Output:
# Hello
# None


# If a function does not explicitly return a value,
# Python returns None.


# ============================================================
# 8. Returning Multiple Values
# ============================================================

def get_employee():
    return "Trupti", 22, "Data Engineer"


result = get_employee()

print(result)

# The returned values are packed into a tuple.


# ============================================================
# 9. Unpacking Returned Values
# ============================================================

def get_employee():
    return "Trupti", 22, "Data Engineer"


name, age, role = get_employee()

print(name)
print(age)
print(role)


# ============================================================
# 10. Returning Early
# ============================================================

def check_number(number):

    if number < 0:
        return "Negative number"

    return "Positive number"


print(check_number(-5))
print(check_number(10))


# 'return' immediately exits the function.


# ============================================================
# 11. Multiple Return Conditions
# ============================================================

def check_age(age):

    if age < 18:
        return "Minor"

    elif age < 60:
        return "Adult"

    else:
        return "Senior"


print(check_age(22))
print(check_age(15))
print(check_age(65))


# ============================================================
# 12. Default Parameters
# ============================================================

def greet(name="User"):
    print("Hello", name)


greet()

greet("Trupti")


# If no argument is provided, the default value is used.


# ============================================================
# 13. Multiple Default Parameters
# ============================================================

def employee(name, role="Data Engineer", city="Pune"):
    print("Name:", name)
    print("Role:", role)
    print("City:", city)


employee("Trupti")

employee(
    "Trupti",
    "Data Analyst",
    "Mumbai"
)


# ============================================================
# 14. Positional Arguments
# ============================================================

def employee(name, role):
    print("Name:", name)
    print("Role:", role)


employee("Trupti", "Data Engineer")


# Arguments are matched according to their position.


# ============================================================
# 15. Keyword Arguments
# ============================================================

def employee(name, role):
    print("Name:", name)
    print("Role:", role)


employee(
    role="Data Engineer",
    name="Trupti"
)


# Keyword arguments explicitly specify parameter names.
#
# Therefore, their order does not matter.


# ============================================================
# 16. Positional vs Keyword Arguments
# ============================================================

# Positional arguments:

employee("Trupti", "Data Engineer")


# Keyword arguments:

employee(
    name="Trupti",
    role="Data Engineer"
)


# Positional arguments depend on order.
#
# Keyword arguments use parameter names.


# ============================================================
# 17. Positional Arguments Before Keyword Arguments
# ============================================================

def employee(name, role, city):
    print(name, role, city)


employee(
    "Trupti",
    role="Data Engineer",
    city="Pune"
)


# Positional arguments should come before keyword arguments.


# ============================================================
# 18. *args
# ============================================================

def add_numbers(*numbers):

    total = 0

    for number in numbers:
        total += number

    return total


print(add_numbers(10, 20))

print(add_numbers(10, 20, 30))

print(add_numbers(10, 20, 30, 40))


# *args allows a function to accept a variable number
# of positional arguments.
#
# Inside the function, args behaves like a tuple.


# ============================================================
# 19. Understanding *args
# ============================================================

def show_values(*values):
    print(values)


show_values(10, 20, 30)

# Output:
# (10, 20, 30)


# ============================================================
# 20. **kwargs
# ============================================================

def employee_info(**details):
    print(details)


employee_info(
    name="Trupti",
    role="Data Engineer",
    city="Pune"
)


# **kwargs allows a function to accept a variable number
# of keyword arguments.
#
# Inside the function, kwargs behaves like a dictionary.


# ============================================================
# 21. Understanding **kwargs
# ============================================================

def show_details(**details):

    print(details)

    print(details["name"])
    print(details["role"])


show_details(
    name="Trupti",
    role="Data Engineer"
)


# ============================================================
# 22. *args vs **kwargs
# ============================================================

def example(*args, **kwargs):

    print("args:", args)
    print("kwargs:", kwargs)


example(
    10,
    20,
    30,
    name="Trupti",
    role="Data Engineer"
)


# *args
# -> Multiple positional arguments
# -> Stored as a tuple
#
# **kwargs
# -> Multiple keyword arguments
# -> Stored as a dictionary


# ============================================================
# 23. Reusable Functions
# ============================================================

def calculate_total(numbers):

    total = 0

    for number in numbers:
        total += number

    return total


print(calculate_total([10, 20, 30]))

print(calculate_total([100, 200, 300]))


# The same function can be reused with different data.


# ============================================================
# 24. Function for Data Cleaning
# ============================================================

def clean_name(name):
    return name.strip().title()


print(clean_name("  trupti  "))

print(clean_name("  rahul  "))

print(clean_name("  PRIYA  "))


# Output:
# Trupti
# Rahul
# Priya


# This type of function is useful when cleaning
# customer or employee data.


# ============================================================
# 25. Function for Removing Duplicates
# ============================================================

def remove_duplicates(values):

    return list(set(values))


numbers = [10, 20, 10, 30, 20]

result = remove_duplicates(numbers)

print(result)


# Note:
# Converting a list to a set removes duplicates.
#
# However, the original order is not guaranteed.


# ============================================================
# 26. Function for Data Validation
# ============================================================

def validate_columns(expected, actual):

    missing = expected - actual

    if missing:
        return False

    return True


expected = {
    "id",
    "name",
    "email"
}

actual = {
    "id",
    "name",
    "email"
}

print(validate_columns(expected, actual))


# ============================================================
# 27. Returning Missing Columns
# ============================================================

def find_missing_columns(expected, actual):

    return expected - actual


expected = {
    "id",
    "name",
    "email",
    "salary"
}

actual = {
    "id",
    "name",
    "email"
}

missing = find_missing_columns(expected, actual)

print("Missing columns:", missing)


# ============================================================
# 28. Local Variables
# ============================================================

def calculate():

    total = 100

    print(total)


calculate()


# 'total' is a local variable.
#
# It belongs to the calculate() function.


# The following would raise an error:
#
# print(total)


# ============================================================
# 29. Global Variables
# ============================================================

name = "Trupti"


def greet():

    print(name)


greet()


# 'name' is a global variable because it was created
# outside the function.


# ============================================================
# 30. Local vs Global Variables
# ============================================================

x = 10


def test():

    y = 20

    print(x)
    print(y)


test()

print(x)

# print(y)
# This would cause an error because y is local
# to the test() function.


# ============================================================
# 31. Avoiding Unnecessary Global Variables
# ============================================================

# Less reusable approach:

tax_rate = 0.18


def calculate_tax(price):

    return price * tax_rate


print(calculate_tax(1000))


# Better approach:

def calculate_tax(price, tax_rate):

    return price * tax_rate


print(calculate_tax(1000, 0.18))

print(calculate_tax(2000, 0.05))


# Passing values as parameters makes functions
# more reusable.


# ============================================================
# 32. Functions Calling Other Functions
# ============================================================

def clean_name(name):

    return name.strip().title()


def create_message(name):

    clean = clean_name(name)

    return f"Customer: {clean}"


print(create_message("  trupti  "))


# One function can call another function.


# ============================================================
# 33. Combining Small Functions
# ============================================================

def clean_text(text):

    return text.strip().lower()


def split_skills(text):

    cleaned_text = clean_text(text)

    return cleaned_text.split(",")


data = " Python, SQL, Pandas "

skills = split_skills(data)

print(skills)


# Small functions can be combined to create
# a larger data-processing workflow.


# ============================================================
# 34. Type Hints
# ============================================================

def add(a: int, b: int) -> int:

    return a + b


print(add(10, 20))


# a: int
# -> Expected type of a
#
# b: int
# -> Expected type of b
#
# -> int
# -> Expected return type
#
# Type hints improve readability and development tools.
# Python does not automatically enforce them at runtime.


# ============================================================
# 35. Function Docstrings
# ============================================================

def calculate_total(numbers):
    """
    Calculate and return the sum of numbers.
    """

    return sum(numbers)


print(calculate_total([10, 20, 30]))

print(calculate_total.__doc__)


# A docstring explains what a function does.


# ============================================================
# 36. Built-in Functions
# ============================================================

numbers = [10, 20, 30, 40]

print(len(numbers))

print(sum(numbers))

print(max(numbers))

print(min(numbers))

print(sorted(numbers))


# These functions are already provided by Python.


# ============================================================
# 37. User-defined Functions
# ============================================================

def calculate_average(numbers):

    return sum(numbers) / len(numbers)


numbers = [10, 20, 30]

print(calculate_average(numbers))


# calculate_average() is a user-defined function.


# ============================================================
# 38. Lambda Functions - Basic Awareness
# ============================================================

square = lambda x: x ** 2

print(square(5))


# Equivalent normal function:

def square_number(x):

    return x ** 2


print(square_number(5))


# Lambda functions are useful for small operations.
#
# They are commonly encountered while working with
# Pandas and functions such as map(), filter(), etc.


# ============================================================
# 39. Functions as Arguments
# ============================================================

def square(x):

    return x ** 2


numbers = [1, 2, 3, 4]

result = list(map(square, numbers))

print(result)


# Output:
# [1, 4, 9, 16]


# A function can be passed as an argument to another function.


# ============================================================
# 40. Data Cleaning Example
# ============================================================

names = [
    " trupti ",
    " rahul ",
    " PRIYA "
]


def clean_name(name):

    return name.strip().title()


cleaned_names = []


for name in names:

    cleaned_names.append(
        clean_name(name)
    )


print(cleaned_names)


# Output:
# ['Trupti', 'Rahul', 'Priya']


# The cleaning function can be reused for every record.


# ============================================================
# 41. Data Engineering - ETL Functions
# ============================================================

def extract_data():

    print("Extracting data...")

    return []


def clean_data(data):

    print("Cleaning data...")

    return data


def validate_data(data):

    print("Validating data...")

    return True


def transform_data(data):

    print("Transforming data...")

    return data


def load_data(data):

    print("Loading data...")


# Simple ETL workflow:

data = extract_data()

data = clean_data(data)

is_valid = validate_data(data)

if is_valid:

    data = transform_data(data)

    load_data(data)


# A real ETL pipeline can be divided into
# multiple reusable functions like this.


# ============================================================
# 42. Function Design - One Clear Responsibility
# ============================================================

# Avoid creating one huge function that performs
# every operation.

# Instead, separate tasks:

def read_data():
    pass


def clean_data(data):
    pass


def validate_data(data):
    pass


def transform_data(data):
    pass


def save_data(data):
    pass


# Each function has one clear responsibility.


# ============================================================
# 43. Function with Empty Input
# ============================================================

def calculate_average(numbers):

    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


print(calculate_average([]))

print(calculate_average([10, 20, 30]))


# Checking the input before processing helps avoid errors.


# ============================================================
# 44. Common Mistake - Forgetting return
# ============================================================

def add(a, b):

    a + b


result = add(10, 20)

print(result)

# Output:
# None


# Correct:

def add(a, b):

    return a + b


result = add(10, 20)

print(result)

# Output:
# 30


# ============================================================
# 45. Common Mistake - Returning Too Early
# ============================================================

def get_first_number(numbers):

    for number in numbers:

        return number


print(get_first_number([10, 20, 30]))


# Output:
# 10
#
# return immediately exits the function.
#
# Therefore, the loop stops after the first iteration.


# ============================================================
# 46. Mutable Default Arguments - Basic Awareness
# ============================================================

# Avoid:

# def add_item(item, items=[]):
#
#     items.append(item)
#
#     return items


# The default list can be reused between function calls.


# Better:

def add_item(item, items=None):

    if items is None:

        items = []

    items.append(item)

    return items


print(add_item("Python"))

print(add_item("SQL"))


# ============================================================
# 47. Function Checklist
# ============================================================

# When creating a reusable function, ask:
#
# 1. What should this function do?
# 2. What inputs does it need?
# 3. What should it return?
# 4. Can I reuse it?
# 5. Does it perform one clear task?
# 6. What happens with invalid input?


# Example:

def calculate_average(numbers):

    if not numbers:

        return 0

    return sum(numbers) / len(numbers)


print(calculate_average([10, 20, 30]))


# ============================================================
# 48. Functions in Data Engineering
# ============================================================

# Functions are commonly used for:
#
# - Data cleaning
# - Data validation
# - Data transformation
# - ETL pipelines
# - API processing
# - File processing
# - Removing duplicates
# - Checking missing values
# - Schema validation
# - Formatting data
# - Database operations


# Example:

def clean_customer_name(name):

    return name.strip().title()


def validate_customer_id(customer_id):

    return customer_id is not None


def transform_salary(salary):

    return float(salary)


customer_name = clean_customer_name("  trupti  ")

customer_id_valid = validate_customer_id(101)

salary = transform_salary("50000")

print(customer_name)
print(customer_id_valid)
print(salary)


# ============================================================
# 49. Function Complexity
# ============================================================

# The time complexity of a function depends on
# the operations performed inside it.


def get_first(numbers):

    return numbers[0]


# List indexing:
# O(1)


def find_number(numbers, target):

    for number in numbers:

        if number == target:

            return True

    return False


# Searching a list:
# O(n)


# ============================================================
# 50. Important Function Concepts Summary
# ============================================================

# Function:
# Reusable block of code.
#
# def:
# Used to define a function.
#
# Parameter:
# Variable in function definition.
#
# Argument:
# Actual value passed to the function.
#
# return:
# Sends a value back to the caller.
#
# Default parameter:
# Parameter with a predefined value.
#
# Positional argument:
# Argument matched according to position.
#
# Keyword argument:
# Argument passed using parameter name.
#
# *args:
# Multiple positional arguments.
# Stored as a tuple.
#
# **kwargs:
# Multiple keyword arguments.
# Stored as a dictionary.
#
# Local variable:
# Variable created inside a function.
#
# Global variable:
# Variable created outside a function.
#
# Type hint:
# Indicates expected input/output types.
#
# Docstring:
# Description of a function.
#
# Lambda:
# Small anonymous function.


# ============================================================
# 51. KEY TAKEAWAYS
# ============================================================

# 1. Functions are reusable blocks of code.
#
# 2. Functions are created using def.
#
# 3. Parameters are variables in the function definition.
#
# 4. Arguments are actual values passed during the function call.
#
# 5. return sends a value back to the caller.
#
# 6. print() displays a value but does not return it.
#
# 7. Functions can return multiple values as a tuple.
#
# 8. Default parameters provide fallback values.
#
# 9. Positional arguments depend on order.
#
# 10. Keyword arguments use parameter names.
#
# 11. *args accepts multiple positional arguments.
#
# 12. **kwargs accepts multiple keyword arguments.
#
# 13. Local variables belong to the function.
#
# 14. Global variables are defined outside functions.
#
# 15. Avoid unnecessary global variables.
#
# 16. Good functions should perform one clear task.
#
# 17. Reusable functions are important in ETL pipelines.
#
# 18. Type hints improve readability.
#
# 19. Docstrings explain the purpose of a function.
#
# 20. Lambda functions are useful for small operations.
#
# 21. Functions can call other functions.
#
# 22. Functions can be passed as arguments to other functions.
#
# 23. Always think:
#
#     Input → Processing → Return
#
# This is a useful mental model when designing functions.


