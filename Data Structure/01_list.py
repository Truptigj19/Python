"""
Python Lists
============

A list is an ordered and mutable collection used to store
multiple values in a single variable.
"""

# ============================================================
# 1. Creating a List
# ============================================================

numbers = [10, 20, 30, 40]
names = ["Alice", "Bob", "Charlie"]
mixed = [10, "Python", 3.14, True]
empty = []

# Lists can contain different data types and duplicate values
data = [10, 20, 10, "Python", 20]

print(numbers)
print(data)


# ============================================================
# 2. Accessing List Elements
# ============================================================

languages = ["Python", "SQL", "Java"]

print(languages[0])      # Python
print(languages[1])      # SQL
print(languages[-1])     # Java


# ============================================================
# 3. Modifying a List
# ============================================================

# Lists are mutable, so elements can be changed.

languages = ["Python", "SQL", "Java"]

languages[2] = "JavaScript"

print(languages)
# ['Python', 'SQL', 'JavaScript']


# ============================================================
# 4. Adding Elements
# ============================================================

# append()
# Adds one element at the end.

skills = ["Python", "SQL"]

skills.append("Git")

print(skills)
# ['Python', 'SQL', 'Git']


# extend()
# Adds multiple elements from another iterable.

skills = ["Python", "SQL"]

skills.extend(["Git", "Docker"])

print(skills)
# ['Python', 'SQL', 'Git', 'Docker']


# insert()
# Adds an element at a specific position.

skills = ["Python", "SQL"]

skills.insert(1, "Pandas")

print(skills)
# ['Python', 'Pandas', 'SQL']


# ============================================================
# 5. append() vs extend()
# ============================================================

# append() adds the entire object as ONE element.

numbers = [1, 2]

numbers.append([3, 4])

print(numbers)
# [1, 2, [3, 4]]


# extend() adds the elements individually.

numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)
# [1, 2, 3, 4]


# ============================================================
# 6. Removing Elements
# ============================================================

# remove()
# Removes the first matching value.

numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)
# [10, 30, 20]


# pop()
# Removes and returns an element using its index.

numbers = [10, 20, 30]

value = numbers.pop(1)

print(value)       # 20
print(numbers)     # [10, 30]


# pop() without an index removes the last element.

numbers = [10, 20, 30]

value = numbers.pop()

print(value)       # 30
print(numbers)     # [10, 20]


# del
# Removes an element or a range.

numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)
# [10, 30, 40]


# ============================================================
# 7. Slicing
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
# [20, 30, 40]

print(numbers[:3])
# [10, 20, 30]

print(numbers[2:])
# [30, 40, 50]

# Syntax:
# list[start:stop:step]

# The stop index is not included.


# Reverse a list using slicing

print(numbers[::-1])
# [50, 40, 30, 20, 10]


# ============================================================
# 8. Useful List Methods
# ============================================================

numbers = [10, 20, 30, 20]

print(numbers.count(20))     # 2
print(numbers.index(30))     # 2
print(len(numbers))          # 4


# sort()
# Sorts the original list.

numbers = [30, 10, 20]

numbers.sort()

print(numbers)
# [10, 20, 30]


# reverse()
# Reverses the original list.

numbers = [10, 20, 30]

numbers.reverse()

print(numbers)
# [30, 20, 10]


# ============================================================
# 9. sort() vs sorted()
# ============================================================

# sort() modifies the original list.

numbers = [30, 10, 20]

numbers.sort()

print(numbers)
# [10, 20, 30]


# sorted() returns a new sorted list.

numbers = [30, 10, 20]

new_numbers = sorted(numbers)

print(numbers)
# [30, 10, 20]

print(new_numbers)
# [10, 20, 30]


# ============================================================
# 10. Iterating Through a List
# ============================================================

skills = ["Python", "SQL", "Pandas"]

for skill in skills:
    print(skill)


# Iterating using indexes

for i in range(len(skills)):
    print(i, skills[i])


# ============================================================
# 11. List Comprehension
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)
# [1, 4, 9, 16, 25]


# List comprehension with a condition

numbers = [1, 2, 3, 4, 5, 6]

even = [x for x in numbers if x % 2 == 0]

print(even)
# [2, 4, 6]


# General syntax:
# [expression for item in iterable if condition]


# ============================================================
# 12. Lists Allow Duplicates
# ============================================================

numbers = [10, 20, 10, 30, 20]

print(numbers)
# [10, 20, 10, 30, 20]


# ============================================================
# 13. List Membership
# ============================================================

skills = ["Python", "SQL", "Pandas"]

print("Python" in skills)
# True

print("Java" not in skills)
# True


# ============================================================
# 14. Aliasing vs Copying
# ============================================================

# Aliasing:
# Both variables refer to the same list.

a = [1, 2, 3]
b = a

b.append(4)

print(a)
# [1, 2, 3, 4]

print(b)
# [1, 2, 3, 4]


# Copying:
# Creates a separate shallow copy.

a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
# [1, 2, 3]

print(b)
# [1, 2, 3, 4]


# Slicing can also create a shallow copy.

b = a[:]


# ============================================================
# 15. List vs Tuple
# ============================================================

# List:
# - Uses []
# - Mutable
# - Can be modified
# - More built-in methods
#
# Tuple:
# - Uses ()
# - Immutable
# - Cannot be modified
# - Fewer built-in methods


# ============================================================
# 16. Time Complexity
# ============================================================

# Access by index       -> O(1)
# Append                -> O(1) amortized
# Search                -> O(n)
# Insert in middle      -> O(n)
# Delete from middle    -> O(n)


# ============================================================
# 17. Data Engineering Use Cases
# ============================================================

# Lists can be used for:
# - Storing column names
# - Holding records temporarily
# - Processing API results
# - Storing file paths
# - Creating values for filtering
# - Iterating through pipeline tasks

columns = ["customer_id", "name", "email", "salary"]

for column in columns:
    print(column)


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. Lists are ordered and mutable.
# 2. Lists allow duplicate values.
# 3. Indexing starts from 0.
# 4. Lists support slicing.
# 5. append() adds one object.
# 6. extend() adds multiple elements.
# 7. remove() removes by value.
# 8. pop() removes by index and returns the value.
# 9. sort() modifies the original list.
# 10. sorted() returns a new sorted list.
# 11. List comprehensions provide concise data transformation.
# 12. Searching an ordinary list takes O(n).