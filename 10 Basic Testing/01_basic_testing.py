"""
Python Basic Testing
====================

Testing means checking whether our code works
as expected.

In Data Engineering, testing is useful for checking:

- Functions
- Data transformations
- Validation logic
- ETL pipeline steps
- Data quality rules

For now, focus on:

1. assert
2. Unit testing concept
3. pytest
4. Simple test functions
5. Testing expected results
6. Testing exceptions
"""


# ============================================================
# 1. What is Testing?
# ============================================================

# Testing means checking whether a program produces
# the expected result.
#
# Example:
#
# Function:
# add(10, 20)
#
# Expected result:
# 30
#
# Testing checks whether:
#
# add(10, 20) == 30


# ============================================================
# 2. Why Testing is Important
# ============================================================

# Without testing:
#
# Code may produce incorrect results
# ↓
# Incorrect data
# ↓
# Incorrect pipeline output
#
#
# Testing helps catch problems early.


# ============================================================
# 3. What is a Unit Test?
# ============================================================

# A unit test checks one small part
# of a program independently.
#
# Usually, a "unit" can be:
#
# - A function
# - A small piece of logic
#
#
# Example:
#
# add()
# validate_email()
# calculate_salary()
#
# Each function can have its own tests.


# ============================================================
# 4. assert
# ============================================================

# assert checks whether a condition is True.

x = 10

assert x == 10


# If the condition is True:
#
# → Nothing happens.
#
#
# If the condition is False:
#
# → AssertionError


# ============================================================
# 5. Simple assert Example
# ============================================================

result = 10 + 20

assert result == 30


# This means:
#
# "I expect result to be 30."


# ============================================================
# 6. assert with Message
# ============================================================

result = 10 + 20

assert result == 30, "Addition result is incorrect"


# If the assertion fails,
# the message helps explain the problem.


# ============================================================
# 7. Testing a Function with assert
# ============================================================

def add(a, b):

    return a + b


result = add(10, 20)

assert result == 30


# The test checks whether the function
# produces the expected output.


# ============================================================
# 8. Another Example
# ============================================================

def multiply(a, b):

    return a * b


assert multiply(5, 4) == 20
assert multiply(10, 2) == 20


# ============================================================
# 9. Testing Different Cases
# ============================================================

def is_even(number):

    return number % 2 == 0


assert is_even(4) is True
assert is_even(10) is True
assert is_even(7) is False


# Testing multiple inputs helps catch
# different types of errors.


# ============================================================
# 10. What Happens When assert Fails?
# ============================================================

def subtract(a, b):

    return a - b


assert subtract(10, 5) == 10


# This will produce:
#
# AssertionError
#
# because:
#
# 10 - 5 = 5
#
# but we expected 10.


# ============================================================
# 11. Basic Unit Test Structure
# ============================================================

# A simple test usually follows:

# Arrange
# ↓
# Prepare input/data
#
# Act
# ↓
# Call the function
#
# Assert
# ↓
# Check expected result


# Example:

def add(a, b):

    return a + b


# Arrange

a = 10
b = 20


# Act

result = add(a, b)


# Assert

assert result == 30


# ============================================================
# 12. What is pytest?
# ============================================================

# pytest is a Python testing framework.
#
# It makes it easier to:
#
# - Write tests
# - Run many tests
# - Find failed tests
# - Organize test files
# - Test exceptions
#
#
# Install:
#
# pip install pytest


# ============================================================
# 13. Basic pytest Test
# ============================================================

# Suppose we have:
#
# calculator.py


def add(a, b):

    return a + b


# Test file:
#
# test_calculator.py


def test_add():

    assert add(2, 3) == 5


# pytest identifies functions beginning with:
#
# test_


# ============================================================
# 14. pytest File Structure
# ============================================================

# A simple project can look like:
#
# project/
#
#     calculator.py
#
#     test_calculator.py
#
#
# Or commonly:
#
# project/
#
#     src/
#         calculator.py
#
#     tests/
#         test_calculator.py


# ============================================================
# 15. Running pytest
# ============================================================

# From the terminal:

# pytest


# pytest automatically discovers
# test files and test functions.


# ============================================================
# 16. Test Function Naming
# ============================================================

# Good:

def test_add():

    assert add(2, 3) == 5


# pytest normally discovers functions
# beginning with:
#
# test_


# Test files commonly use:
#
# test_*.py
#
# or
#
# *_test.py


# ============================================================
# 17. Testing a Data Transformation
# ============================================================

def double_values(numbers):

    return [x * 2 for x in numbers]


def test_double_values():

    result = double_values([1, 2, 3])

    assert result == [2, 4, 6]


# This type of testing is useful for
# data transformation functions.


# ============================================================
# 18. Testing Data Validation
# ============================================================

def is_valid_record(record):

    if record.get("id") is None:

        return False

    if record.get("name") is None:

        return False

    return True


def test_valid_record():

    record = {
        "id": 101,
        "name": "Alice"
    }

    assert is_valid_record(record) is True


def test_invalid_record():

    record = {
        "id": None,
        "name": "Alice"
    }

    assert is_valid_record(record) is False


# ============================================================
# 19. Testing Multiple Conditions
# ============================================================

def calculate_total(price, quantity):

    return price * quantity


def test_calculate_total():

    assert calculate_total(100, 2) == 200
    assert calculate_total(50, 4) == 200
    assert calculate_total(10, 5) == 50


# ============================================================
# 20. Testing Strings
# ============================================================

def clean_name(name):

    return name.strip().title()


def test_clean_name():

    assert clean_name(" alice ") == "Alice"


# ============================================================
# 21. Testing Lists
# ============================================================

def get_even_numbers(numbers):

    return [
        number
        for number in numbers
        if number % 2 == 0
    ]


def test_get_even_numbers():

    result = get_even_numbers(
        [1, 2, 3, 4, 5, 6]
    )

    assert result == [2, 4, 6]


# ============================================================
# 22. Testing Dictionaries
# ============================================================

def create_user(name, age):

    return {
        "name": name,
        "age": age
    }


def test_create_user():

    user = create_user("Alice", 25)

    assert user["name"] == "Alice"
    assert user["age"] == 25


# ============================================================
# 23. Testing None
# ============================================================

def find_user(users, user_id):

    for user in users:

        if user["id"] == user_id:

            return user

    return None


def test_find_missing_user():

    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]

    result = find_user(users, 99)

    assert result is None


# ============================================================
# 24. Testing Exceptions
# ============================================================

# Sometimes we expect a function
# to raise an error for invalid input.


def divide(a, b):

    if b == 0:

        raise ValueError(
            "Cannot divide by zero"
        )

    return a / b


# With pytest, we can test the exception.


# Example:

# import pytest
#
#
# def test_divide_by_zero():
#
#     with pytest.raises(ValueError):
#
#         divide(10, 0)


# ============================================================
# 25. Why Test Exceptions?
# ============================================================

# We should test not only valid input
# but also invalid input.
#
# Example:
#
# Valid:
# divide(10, 2)
#
# Invalid:
# divide(10, 0)
#
#
# A good test suite checks both.


# ============================================================
# 26. Testing Edge Cases
# ============================================================

# Edge cases are unusual or boundary inputs.
#
# Examples:
#
# Empty list
# Zero
# Negative number
# None
# Empty string
# Very large number


def get_first_item(items):

    if not items:

        return None

    return items[0]


def test_empty_list():

    assert get_first_item([]) is None


def test_normal_list():

    assert get_first_item([10, 20]) == 10


# ============================================================
# 27. Testing API-Related Functions
# ============================================================

# In real projects, API calls can also be tested.
#
# However, you usually don't want every test
# to make a real API request.
#
# More advanced concepts include:
#
# - Mocking
# - Fixtures
# - Test clients
#
# You do NOT need to go deeply into these
# at your current fresher level.


# ============================================================
# 28. Testing ETL Functions
# ============================================================

# Example transformation:

def transform_salary(salary):

    return salary * 1.10


def test_transform_salary():

    result = transform_salary(1000)

    assert result == 1100


# In a real Data Engineering project,
# individual transformation functions
# can be tested independently.


# ============================================================
# 29. Testing Record Counts
# ============================================================

def count_records(records):

    return len(records)


def test_count_records():

    records = [
        {"id": 1},
        {"id": 2},
        {"id": 3}
    ]

    assert count_records(records) == 3


# ============================================================
# 30. Testing Data Quality Rules
# ============================================================

def is_valid_salary(salary):

    return salary >= 0


def test_valid_salary():

    assert is_valid_salary(50000) is True


def test_invalid_salary():

    assert is_valid_salary(-100) is False


# ============================================================
# 31. Unit Test vs Integration Test
# ============================================================

# Unit Test
# → Tests one small unit/function independently.
#
#
# Integration Test
# → Checks whether multiple components
#   work correctly together.
#
#
# Example:
#
# Unit:
# test_transform_data()
#
# Integration:
# API → Transform → Database


# For now, focus mainly on unit testing.


# ============================================================
# 32. Testing in Data Engineering
# ============================================================

# Testing can be used for:
#
# - Data transformation functions
# - Validation functions
# - Cleaning functions
# - ETL logic
# - Record-count checks
# - Business rules
# - Utility functions
#
#
# Example:
#
# Extract
#   ↓
# Transform
#   ↓
# Validate
#   ↓
# Load
#
# Each important function can have tests.


# ============================================================
# 33. Common Testing Mistakes
# ============================================================

# Mistake 1:
# Only testing successful inputs.
#
# Better:
# Test valid + invalid + edge cases.


# Mistake 2:
# Testing everything manually.
#
# Better:
# Automate repeated checks with pytest.


# Mistake 3:
# Writing tests that depend on each other.
#
# Better:
# Keep unit tests independent.


# Mistake 4:
# Testing implementation instead of behavior.
#
# Focus on:
#
# "Does the function produce the expected result?"


# ============================================================
# 34. Basic pytest Example
# ============================================================

# calculator.py

def add(a, b):

    return a + b


def subtract(a, b):

    return a - b


# test_calculator.py

def test_add():

    assert add(2, 3) == 5


def test_subtract():

    assert subtract(5, 2) == 3


# Run:

# pytest


# ============================================================
# 35. Basic Testing Workflow
# ============================================================

# Write function
#      ↓
# Write test
#      ↓
# Run pytest
#      ↓
# Test passes?
#
# YES → Continue
#
# NO → Fix code
#      ↓
# Run test again


# ============================================================
# ⭐ FRESHER MUST-KNOW CHEAT SHEET
# ============================================================

# Testing
# → Checking whether code works as expected.
#
# Unit Test
# → Test one small function/unit.
#
# assert
# → Check whether a condition is True.
#
# pytest
# → Popular Python testing framework.
#
# test_*.py
# → Common pytest test file naming.
#
# test_function()
# → Common pytest test function naming.
#
# pytest
# → Run tests from terminal.
#
# Valid input
# → Test expected/normal cases.
#
# Invalid input
# → Test incorrect input.
#
# Edge case
# → Test boundary/unusual cases.
#
# pytest.raises()
# → Test that an expected exception occurs.
#
# Unit Test
# → Individual function.
#
# Integration Test
# → Multiple components working together.
#
#
# Data Engineering:
#
# Extract
#   ↓
# Transform
#   ↓
# Validate
#   ↓
# Load
#
# Test important transformation,
# validation and business-rule functions.