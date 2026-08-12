"""
Python Dictionaries
===================

A dictionary is an ordered and mutable collection that stores
data in key-value pairs.

Example:
    {"name": "Trupti", "age": 22}
"""

# ============================================================
# 1. Creating a Dictionary
# ============================================================

student = {
    "name": "Trupti",
    "age": 22,
    "city": "Pune"
}

print(student)

# Empty dictionary
empty_dict = {}

# Dictionary with different data types
mixed = {
    "name": "Trupti",
    "age": 22,
    "cgpa": 9.5,
    "is_student": True
}

print(mixed)


# ============================================================
# 2. Dictionary Keys and Values
# ============================================================

# A dictionary stores data as:
# key : value

student = {
    "name": "Trupti",
    "age": 22,
    "city": "Pune"
}

# Keys must be unique.
# If the same key is used again, the latest value replaces it.

data = {
    "name": "Trupti",
    "name": "Alice"
}

print(data)
# {'name': 'Alice'}


# ============================================================
# 3. Accessing Dictionary Values
# ============================================================

student = {
    "name": "Trupti",
    "age": 22,
    "city": "Pune"
}

# Access using []

print(student["name"])
# Trupti

print(student["age"])
# 22


# ============================================================
# 4. [] vs get()
# ============================================================

# Using [] when the key does not exist gives KeyError.

# print(student["country"])
# KeyError


# get() returns None if the key does not exist.

print(student.get("country"))
# None


# get() can also provide a default value.

print(student.get("country", "India"))
# India


# [] is useful when the key MUST exist.
# get() is safer when the key may be missing.


# ============================================================
# 5. Adding New Values
# ============================================================

student = {
    "name": "Trupti",
    "age": 22
}

# Add a new key-value pair

student["city"] = "Pune"

print(student)
# {'name': 'Trupti', 'age': 22, 'city': 'Pune'}


# ============================================================
# 6. Updating Existing Values
# ============================================================

student = {
    "name": "Trupti",
    "age": 22
}

student["age"] = 23

print(student)
# {'name': 'Trupti', 'age': 23}


# The same syntax can add a key or update a key.

# New key:
student["city"] = "Pune"

# Existing key:
student["age"] = 23


# ============================================================
# 7. update()
# ============================================================

# update() can add or update multiple values.

student = {
    "name": "Trupti",
    "age": 22
}

student.update({
    "age": 23,
    "city": "Pune"
})

print(student)
# {'name': 'Trupti', 'age': 23, 'city': 'Pune'}


# update() can also be used with keyword arguments.

student.update(age=24)

print(student)


# ============================================================
# 8. Removing Elements
# ============================================================

# pop()
# Removes a specific key and returns its value.

student = {
    "name": "Trupti",
    "age": 22,
    "city": "Pune"
}

age = student.pop("age")

print(age)
# 22

print(student)
# {'name': 'Trupti', 'city': 'Pune'}


# popitem()
# Removes and returns the last inserted key-value pair.

student = {
    "name": "Trupti",
    "age": 22,
    "city": "Pune"
}

item = student.popitem()

print(item)
# ('city', 'Pune')

print(student)


# del
# Deletes a specific key.

student = {
    "name": "Trupti",
    "age": 22
}

del student["age"]

print(student)
# {'name': 'Trupti'}


# clear()
# Removes all key-value pairs.

student.clear()

print(student)
# {}


# ============================================================
# 9. Removing Elements - Comparison
# ============================================================

# pop(key)
# Removes a specific key and returns its value.

# popitem()
# Removes the last inserted key-value pair.

# del
# Deletes a specific key.

# clear()
# Removes all elements.


# ============================================================
# 10. Checking if a Key Exists
# ============================================================

student = {
    "name": "Trupti",
    "age": 22,
    "city": "Pune"
}

print("name" in student)
# True

print("country" in student)
# False

print("country" not in student)
# True


# Important:
# "name" in student checks KEYS, not values.


# ============================================================
# 11. keys()
# ============================================================

student = {
    "name": "Trupti",
    "age": 22,
    "city": "Pune"
}

print(student.keys())

# Returns all dictionary keys.


# ============================================================
# 12. values()
# ============================================================

print(student.values())

# Returns all dictionary values.


# ============================================================
# 13. items()
# ============================================================

print(student.items())

# Returns key-value pairs as tuples.


# ============================================================
# 14. Iterating Through Dictionary Keys
# ============================================================

student = {
    "name": "Trupti",
    "age": 22,
    "city": "Pune"
}

for key in student:
    print(key)


# ============================================================
# 15. Iterating Through Dictionary Values
# ============================================================

for value in student.values():
    print(value)


# ============================================================
# 16. Iterating Through Key-Value Pairs
# ============================================================

for key, value in student.items():
    print(key, value)

# This is one of the most commonly used dictionary loops.


# ============================================================
# 17. Nested Dictionaries
# ============================================================

# A dictionary can contain another dictionary.

students = {
    "student1": {
        "name": "Trupti",
        "age": 22
    },
    "student2": {
        "name": "Alice",
        "age": 21
    }
}

print(students)


# Accessing nested values

print(students["student1"]["name"])
# Trupti

print(students["student2"]["age"])
# 21


# ============================================================
# 18. Dictionary Containing Lists
# ============================================================

employee = {
    "name": "Trupti",
    "skills": ["Python", "SQL", "Pandas"],
    "projects": ["ETL", "API"]
}

print(employee["skills"])

print(employee["skills"][0])
# Python


# ============================================================
# 19. Dictionary Comprehension
# ============================================================

# Dictionary comprehension provides a concise way
# to create dictionaries.

numbers = [1, 2, 3, 4, 5]

squares = {
    x: x ** 2
    for x in numbers
}

print(squares)

# {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16,
#     5: 25
# }


# ============================================================
# 20. Dictionary Comprehension with Condition
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    x: x ** 2
    for x in numbers
    if x % 2 == 0
}

print(even_squares)

# {
#     2: 4,
#     4: 16,
#     6: 36
# }


# General syntax:
#
# {key: value for item in iterable if condition}


# ============================================================
# 21. Creating Dictionary Using zip()
# ============================================================

keys = ["name", "age", "city"]
values = ["Trupti", 22, "Pune"]

student = dict(zip(keys, values))

print(student)

# {
#     'name': 'Trupti',
#     'age': 22,
#     'city': 'Pune'
# }


# zip() combines corresponding elements
# from two or more iterables.


# ============================================================
# 22. Creating Dictionary from a List
# ============================================================

numbers = [1, 2, 3, 4]

square_dict = {}

for number in numbers:
    square_dict[number] = number ** 2

print(square_dict)


# The same thing using dictionary comprehension:

square_dict = {
    number: number ** 2
    for number in numbers
}

print(square_dict)


# ============================================================
# 23. setdefault()
# ============================================================

# setdefault() adds a key only if it does not already exist.

data = {}

data.setdefault("name", "Trupti")

print(data)
# {'name': 'Trupti'}


# If the key already exists, its value is not replaced.

data.setdefault("name", "Alice")

print(data)
# {'name': 'Trupti'}


# ============================================================
# 24. Dictionary Length
# ============================================================

student = {
    "name": "Trupti",
    "age": 22,
    "city": "Pune"
}

print(len(student))
# 3


# len() returns the number of key-value pairs.


# ============================================================
# 25. Dictionary with JSON-like Data
# ============================================================

# JSON data is commonly represented as dictionaries
# when working with Python.

employee = {
    "id": 101,
    "name": "Trupti",
    "salary": 50000
}

print(employee["name"])
# Trupti

print(employee["salary"])
# 50000


# ============================================================
# 26. Multiple Records
# ============================================================

# Multiple records can be stored as a list of dictionaries.

employees = [
    {
        "id": 101,
        "name": "Trupti",
        "salary": 50000
    },
    {
        "id": 102,
        "name": "Alice",
        "salary": 60000
    },
    {
        "id": 103,
        "name": "Bob",
        "salary": 55000
    }
]

for employee in employees:
    print(employee["name"], employee["salary"])


# This structure is very common when working with
# API responses and JSON data.


# ============================================================
# 27. Dictionary with Mutable Objects
# ============================================================

# Dictionary values can be mutable objects such as lists.

employee = {
    "name": "Trupti",
    "skills": ["Python", "SQL"]
}

employee["skills"].append("Pandas")

print(employee)

# {
#     'name': 'Trupti',
#     'skills': ['Python', 'SQL', 'Pandas']
# }


# ============================================================
# 28. Dictionary vs List vs Tuple vs Set
# ============================================================

# List:
# - Uses []
# - Ordered
# - Mutable
# - Allows duplicates
# - Used for collections of items
#
# Tuple:
# - Uses ()
# - Ordered
# - Immutable
# - Allows duplicates
# - Used for fixed data
#
# Dictionary:
# - Uses {}
# - Stores key-value pairs
# - Mutable
# - Keys must be unique
# - Used for structured key-value data
#
# Set:
# - Uses {}
# - Stores unique values
# - Mutable
# - Does not support duplicate values
# - Used when uniqueness is important


# ============================================================
# 29. Time Complexity
# ============================================================

# For a normal Python dictionary:

# Access by key       -> O(1) average
# Insert               -> O(1) average
# Update               -> O(1) average
# Delete               -> O(1) average
# Search by key        -> O(1) average

# Searching for a value can take O(n).


# ============================================================
# 30. Data Engineering Use Cases
# ============================================================

# Dictionaries are commonly used for:

# - JSON data
# - API responses
# - Configuration data
# - Records
# - Mapping column names to values
# - Temporary data transformation
# - Database records
# - Data validation
# - Grouping and counting data


# Example: API/JSON-style record

employee = {
    "id": 101,
    "name": "Trupti",
    "department": "Data Engineering",
    "salary": 50000
}

print(employee["department"])


# Example: Multiple API records

employees = [
    {
        "id": 101,
        "name": "Trupti"
    },
    {
        "id": 102,
        "name": "Alice"
    }
]

for employee in employees:
    print(employee["name"])


# ============================================================
# 31. Dictionary for Counting
# ============================================================

# Dictionaries can be used to count occurrences.

numbers = [1, 2, 2, 3, 3, 3]

count = {}

for number in numbers:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

print(count)

# {
#     1: 1,
#     2: 2,
#     3: 3
# }


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. Dictionaries store data in key-value pairs.
# 2. Dictionaries are mutable.
# 3. Dictionary keys must be unique.
# 4. Values can be duplicated.
# 5. [] accesses a value but raises KeyError for missing keys.
# 6. get() safely accesses a key that may not exist.
# 7. update() can add or update multiple values.
# 8. pop() removes a specific key.
# 9. popitem() removes the last inserted pair.
# 10. keys() returns keys.
# 11. values() returns values.
# 12. items() returns key-value pairs.
# 13. items() is useful for looping through key-value pairs.
# 14. Dictionaries can contain lists and other dictionaries.
# 15. Dictionary comprehension creates dictionaries concisely.
# 16. zip() can combine two lists into a dictionary.
# 17. Dictionaries are very important when working with JSON and APIs.
# 18. Dictionary key access is O(1) on average.