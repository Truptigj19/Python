"""
Python Error Handling
=====================

Error handling prevents a program from crashing when something
unexpected happens.

Instead of stopping execution, Python can catch the error and
handle it gracefully.

"""


# ============================================================
# 1. What is an Exception?
# ============================================================

# An exception is a runtime error that interrupts
# the normal flow of a program.

# Example:

# print(10 / 0)

# ZeroDivisionError


# ============================================================
# 2. try
# ============================================================

# Code that might fail goes inside try.

try:

    number = 10 / 2

    print(number)

except:

    print("Something went wrong")


# ============================================================
# 3. except
# ============================================================

# except runs only if an error occurs.

try:

    number = 10 / 0

except:

    print("Cannot divide by zero")


# ============================================================
# 4. Catching Specific Exceptions
# ============================================================

try:

    number = 10 / 0

except ZeroDivisionError:

    print("Division by zero is not allowed")


# Always prefer specific exceptions instead of a
# generic except whenever possible.


# ============================================================
# 5. Multiple Exceptions
# ============================================================

try:

    number = int("abc")

except ValueError:

    print("Invalid number")

except ZeroDivisionError:

    print("Cannot divide by zero")


# ============================================================
# 6. else
# ============================================================

# else runs only when NO exception occurs.

try:

    number = int("25")

except ValueError:

    print("Invalid input")

else:

    print("Conversion successful")

    print(number)


# ============================================================
# 7. finally
# ============================================================

# finally always executes.

try:

    file = open("example.txt", "r")

except FileNotFoundError:

    print("File not found")

finally:

    print("Program finished")


# finally is commonly used for cleanup.


# ============================================================
# 8. Complete Structure
# ============================================================

try:

    number = int(input("Enter number: "))

except ValueError:

    print("Please enter digits only")

else:

    print("Valid number:", number)

finally:

    print("Execution completed")


# ============================================================
# 9. Exception Object
# ============================================================

try:

    number = 10 / 0

except ZeroDivisionError as error:

    print(error)


# The actual error message is stored inside 'error'.


# ============================================================
# 10. Common Exceptions
# ============================================================

# ZeroDivisionError
# ValueError
# TypeError
# IndexError
# KeyError
# FileNotFoundError
# AttributeError


# ============================================================
# 11. ZeroDivisionError
# ============================================================

try:

    result = 100 / 0

except ZeroDivisionError:

    print("Cannot divide by zero")


# ============================================================
# 12. ValueError
# ============================================================

try:

    age = int("twenty")

except ValueError:

    print("Age must be a number")


# ============================================================
# 13. TypeError
# ============================================================

try:

    result = "10" + 20

except TypeError:

    print("Cannot add string and integer")


# ============================================================
# 14. IndexError
# ============================================================

numbers = [10, 20, 30]

try:

    print(numbers[5])

except IndexError:

    print("Index does not exist")


# ============================================================
# 15. KeyError
# ============================================================

employee = {
    "name": "Trupti",
    "role": "Data Engineer"
}

try:

    print(employee["salary"])

except KeyError:

    print("Key not found")


# ============================================================
# 16. FileNotFoundError
# ============================================================

try:

    with open("missing.csv", "r") as file:

        print(file.read())

except FileNotFoundError:

    print("Input file does not exist")


# ============================================================
# 17. AttributeError
# ============================================================

text = "Python"

try:

    text.append("SQL")

except AttributeError:

    print("Strings do not have append()")


# ============================================================
# 18. Catching Multiple Errors Together
# ============================================================

try:

    number = int(input("Enter number: "))

    result = 100 / number

except (ValueError, ZeroDivisionError):

    print("Invalid input")


# ============================================================
# 19. Generic Exception
# ============================================================

try:

    number = int("abc")

except Exception as error:

    print("Unexpected error:", error)


# Use generic Exception only as a last resort.


# ============================================================
# 20. Raising Exceptions
# ============================================================

age = -5

if age < 0:

    raise ValueError("Age cannot be negative")


# raise creates an exception manually.


# ============================================================
# 21. Custom Validation
# ============================================================

salary = -1000

if salary < 0:

    raise ValueError("Salary cannot be negative")


# ============================================================
# 22. Custom Exception
# ============================================================

class InvalidSalaryError(Exception):
    pass


salary = -500

if salary < 0:

    raise InvalidSalaryError("Invalid salary amount")


# Basic awareness is enough for interviews.


# ============================================================
# 23. Data Engineering Example
# ============================================================

from pathlib import Path

file_path = Path("data/raw/sales.csv")

try:

    if not file_path.exists():

        raise FileNotFoundError("Sales file missing")

    print("Processing file...")

except FileNotFoundError as error:

    print(error)


# ============================================================
# 24. Safe CSV Reading
# ============================================================

import csv

try:

    with open("employees.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:

            print(row)

except FileNotFoundError:

    print("CSV file not found")


# ============================================================
# 25. Safe JSON Reading
# ============================================================

import json

try:

    with open("employee.json", "r") as file:

        data = json.load(file)

        print(data)

except FileNotFoundError:

    print("JSON file missing")

except json.JSONDecodeError:

    print("Invalid JSON format")


# ============================================================
# 26. Business Rule Validation
# ============================================================

def validate_age(age):

    if age < 18:

        raise ValueError("Employee must be 18+")

    return True


try:

    validate_age(15)

except ValueError as error:

    print(error)


# ============================================================
# 27. ETL Example
# ============================================================

def process_file(file_name):

    try:

        with open(file_name, "r") as file:

            print("Reading file")

            return file.read()

    except FileNotFoundError:

        print("File missing")

        return None


data = process_file("sales.csv")


# ============================================================
# 28. Input Validation Function
# ============================================================

def get_positive_number(value):

    if value <= 0:

        raise ValueError("Number must be positive")

    return value


try:

    print(get_positive_number(-10))

except ValueError as error:

    print(error)


# ============================================================
# 29. Why Error Handling Matters
# ============================================================

# Without error handling:
#
# Pipeline crashes.
#
# With error handling:
#
# Log the issue
# Skip bad records
# Continue processing
# Notify the user


# ============================================================
# 30. Key Takeaways
# ============================================================

# try
# Code that may fail
#
# except
# Handles errors
#
# else
# Runs if no error occurs
#
# finally
# Always executes
#
# raise
# Creates an exception manually
#
# Exception
# Base class for most errors
#
# Prefer specific exceptions over generic Exception.


# ============================================================
# 31. Practice Questions
# ============================================================

# 1. Handle division by zero.
# 2. Catch ValueError when converting input.
# 3. Read a file safely.
# 4. Raise an error for negative salary.
# 5. Create a custom exception for invalid email.
# 6. Build a function that validates CSV file existence.
# 7. Handle both JSONDecodeError and FileNotFoundError.
# 8. Create a safe ETL function using try/except/finally.