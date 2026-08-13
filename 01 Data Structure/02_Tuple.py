"""
Python Tuples
=============

A tuple is an ordered and immutable collection used to store
multiple values in a single variable.
"""

# ============================================================
# 1. Creating a Tuple
# ============================================================

data = ("Trupti", 22, "Pune")

numbers = (10, 20, 30)
names = ("Alice", "Bob", "Charlie")
mixed = (10, "Python", 3.14, True)
empty = ()

# Tuples can contain different data types and duplicate values.

data = (10, 20, 10, "Python", 20)

print(data)


# ============================================================
# 2. Single-Element Tuple
# ============================================================

# (10) is an integer, not a tuple.

x = (10)

print(type(x))
# <class 'int'>


# A comma is required to create a single-element tuple.

x = (10,)

print(type(x))
# <class 'tuple'>


# ============================================================
# 3. Accessing Tuple Elements
# ============================================================

languages = ("Python", "SQL", "Java")

print(languages[0])      # Python
print(languages[1])      # SQL
print(languages[-1])     # Java


# ============================================================
# 4. Tuple Immutability
# ============================================================

# Tuples are immutable.
# Their elements cannot be changed after creation.

languages = ("Python", "SQL", "Java")

# The following line gives TypeError:
# languages[0] = "C++"


# If data needs to be changed frequently:
# Use a list.


# If data should remain fixed:
# A tuple can be useful.


# ============================================================
# 5. Slicing Tuples
# ============================================================

data = ("Python", "SQL", "Airflow", "Docker")

print(data[1:3])
# ('SQL', 'Airflow')

print(data[:2])
# ('Python', 'SQL')

print(data[::-1])
# ('Docker', 'Airflow', 'SQL', 'Python')


# Syntax:
# tuple[start:stop:step]


# ============================================================
# 6. Tuple Methods
# ============================================================

# Tuples have two main methods:
# count()
# index()


# count()
# Returns the number of times a value occurs.

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
# 3


# index()
# Returns the index of the first occurrence.

numbers = (10, 20, 30, 20)

print(numbers.index(20))
# 1


# ============================================================
# 7. Tuple Unpacking
# ============================================================

employee = ("Trupti", 22, "Data Engineer")

name, age, role = employee

print(name)
print(age)
print(role)


# The number of variables should normally match
# the number of tuple elements.


# ============================================================
# 8. Extended Unpacking
# ============================================================

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
# 10

print(middle)
# [20, 30, 40]

print(last)
# 50


# ============================================================
# 9. Membership Checking
# ============================================================

skills = ("Python", "SQL", "Pandas")

print("Python" in skills)
# True

print("Java" not in skills)
# True


# ============================================================
# 10. Iterating Through a Tuple
# ============================================================

skills = ("Python", "SQL", "Pandas")

for skill in skills:
    print(skill)


# ============================================================
# 11. Tuple Packing
# ============================================================

# Multiple values separated by commas can form a tuple.

data = "Python", "SQL", "Pandas"

print(data)
# ('Python', 'SQL', 'Pandas')

# The comma is what creates the tuple.
# Parentheses are optional in many tuple-packing situations.


# ============================================================
# 12. List vs Tuple
# ============================================================

# List:
# - Uses []
# - Mutable
# - Can be modified
# - More built-in methods
# - Suitable for changing data
#
# Tuple:
# - Uses ()
# - Immutable
# - Cannot be modified
# - Fewer built-in methods
# - Suitable for fixed data


# Example of a list:

skills = ["Python", "SQL"]
skills.append("Pandas")

print(skills)


# Example of a tuple:

coordinates = (18.52, 73.85)

print(coordinates)


# ============================================================
# 13. Tuples in Functions
# ============================================================

# A function can return multiple values using a tuple.

def get_employee():
    return "Trupti", 22, "Data Engineer"


result = get_employee()

print(result)
# ('Trupti', 22, 'Data Engineer')


# The returned tuple can also be unpacked.

name, age, role = get_employee()

print(name)
print(age)
print(role)


# ============================================================
# 14. Tuples in Data Engineering
# ============================================================

# Tuples commonly appear in:
# - Database query results
# - Rows returned from SQL queries
# - zip()
# - Dictionary .items()
# - Functions returning multiple values
# - Fixed configuration or coordinate-like data


# Example of database-style rows:

rows = [
    (101, "Alice", 50000),
    (102, "Bob", 60000),
    (103, "Charlie", 55000)
]

for row in rows:
    print(row)


# Each row can be represented as a tuple.


# ============================================================
# 15. Tuple with Mutable Objects
# ============================================================

# A tuple itself is immutable,
# but it can contain mutable objects such as a list.

data = ("Python", [1, 2, 3])

data[1].append(4)

print(data)
# ('Python', [1, 2, 3, 4])

# The tuple's reference to the list did not change.
# The list itself was modified.


# ============================================================
# 16. Time Complexity
# ============================================================

# Access by index    -> O(1)
# Search             -> O(n)
# count()            -> O(n)
# index()            -> O(n)

# Since tuples are immutable,
# modification operations are not available.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. Tuples are ordered and immutable.
# 2. Tuples allow duplicate values.
# 3. Tuples support indexing and slicing.
# 4. A single-element tuple requires a comma.
# 5. Main tuple methods are count() and index().
# 6. Tuple unpacking assigns values to multiple variables.
# 7. Functions can return multiple values using tuples.
# 8. Tuples commonly appear in database query results.
# 9. Tuples are useful when data should remain unchanged.
# 10. A tuple can contain mutable objects such as lists.