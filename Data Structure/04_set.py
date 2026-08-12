"""
Python Sets
===========

A set is an unordered, mutable collection of unique elements.

Sets are mainly used when:
- Duplicate values need to be removed
- Fast membership checking is required
- Set operations such as union and intersection are needed
"""

# ============================================================
# 1. Creating a Set
# ============================================================

numbers = {10, 20, 30, 40}

print(numbers)

# Sets automatically remove duplicate values.

numbers = {10, 20, 10, 30, 20}

print(numbers)
# {10, 20, 30}


# A set can contain different data types.

data = {10, "Python", 3.14, True}

print(data)


# ============================================================
# 2. Empty Set
# ============================================================

# {} creates an empty dictionary, NOT an empty set.

empty_dict = {}

print(type(empty_dict))
# <class 'dict'>


# To create an empty set, use set().

empty_set = set()

print(type(empty_set))
# <class 'set'>


# ============================================================
# 3. Sets Are Unordered
# ============================================================

numbers = {10, 20, 30, 40}

print(numbers)

# Sets do not support indexing.

# The following will raise TypeError:
# print(numbers[0])

# Unlike lists and tuples:
# numbers[0]  -> Not supported


# ============================================================
# 4. Sets Do Not Allow Duplicates
# ============================================================

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)
# {10, 20, 30, 40}

# Duplicate values are automatically removed.


# ============================================================
# 5. Creating a Set from a List
# ============================================================

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print(unique_numbers)
# {10, 20, 30, 40}

# This is commonly used to remove duplicate values.


# ============================================================
# 6. Adding Elements
# ============================================================

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
# {10, 20, 30, 40}


# Adding an existing element does nothing.

numbers.add(20)

print(numbers)
# {10, 20, 30, 40}


# ============================================================
# 7. Adding Multiple Elements
# ============================================================

# update() adds multiple elements.

numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)
# {10, 20, 30, 40, 50}


# update() can accept different iterables.

numbers.update((60, 70))

print(numbers)


# ============================================================
# 8. Removing Elements
# ============================================================

# remove()
# Removes a specific element.

numbers = {10, 20, 30, 40}

numbers.remove(30)

print(numbers)
# {10, 20, 40}


# If the element does not exist, remove() raises KeyError.

# numbers.remove(100)
# KeyError


# ============================================================
# 9. discard()
# ============================================================

# discard() also removes an element.

numbers = {10, 20, 30, 40}

numbers.discard(30)

print(numbers)
# {10, 20, 40}


# Difference between remove() and discard():

# remove() -> raises KeyError if element does not exist
# discard() -> does nothing if element does not exist


numbers.discard(100)

print(numbers)
# No error


# ============================================================
# 10. pop()
# ============================================================

# pop() removes and returns an arbitrary element.

numbers = {10, 20, 30, 40}

value = numbers.pop()

print(value)
print(numbers)

# Since sets are unordered, you should NOT depend on
# which element pop() removes.


# ============================================================
# 11. clear()
# ============================================================

numbers = {10, 20, 30}

numbers.clear()

print(numbers)
# set()


# ============================================================
# 12. Membership Checking
# ============================================================

numbers = {10, 20, 30, 40}

print(20 in numbers)
# True

print(50 in numbers)
# False

print(50 not in numbers)
# True


# Membership checking is one of the main reasons
# sets are useful.


# ============================================================
# 13. Iterating Through a Set
# ============================================================

skills = {"Python", "SQL", "Pandas"}

for skill in skills:
    print(skill)

# The order is not guaranteed.


# ============================================================
# 14. Set Union
# ============================================================

# Union combines all unique elements from two sets.

set_a = {1, 2, 3}
set_b = {3, 4, 5}

result = set_a.union(set_b)

print(result)
# {1, 2, 3, 4, 5}


# Union using | operator

result = set_a | set_b

print(result)
# {1, 2, 3, 4, 5}


# ============================================================
# 15. Set Intersection
# ============================================================

# Intersection returns elements common to both sets.

set_a = {1, 2, 3}
set_b = {3, 4, 5}

result = set_a.intersection(set_b)

print(result)
# {3}


# Intersection using & operator

result = set_a & set_b

print(result)
# {3}


# ============================================================
# 16. Set Difference
# ============================================================

# Difference returns elements present in the first set
# but not in the second set.

set_a = {1, 2, 3}
set_b = {3, 4, 5}

result = set_a.difference(set_b)

print(result)
# {1, 2}


# Difference using - operator

result = set_a - set_b

print(result)
# {1, 2}


# Reverse difference

result = set_b - set_a

print(result)
# {4, 5}


# ============================================================
# 17. Symmetric Difference
# ============================================================

# Returns elements that are in either set,
# but NOT in both.

set_a = {1, 2, 3}
set_b = {3, 4, 5}

result = set_a.symmetric_difference(set_b)

print(result)
# {1, 2, 4, 5}


# Symmetric difference using ^ operator

result = set_a ^ set_b

print(result)
# {1, 2, 4, 5}


# ============================================================
# 18. Set Operations Summary
# ============================================================

set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
print(set_a | set_b)
# {1, 2, 3, 4, 5}

# Intersection
print(set_a & set_b)
# {3}

# Difference
print(set_a - set_b)
# {1, 2}

# Symmetric difference
print(set_a ^ set_b)
# {1, 2, 4, 5}


# ============================================================
# 19. Updating Set Using Operations
# ============================================================

set_a = {1, 2, 3}
set_b = {3, 4, 5}

# update() / union update

set_a.update(set_b)

print(set_a)
# {1, 2, 3, 4, 5}


# ============================================================
# 20. intersection_update()
# ============================================================

set_a = {1, 2, 3}
set_b = {2, 3, 4}

set_a.intersection_update(set_b)

print(set_a)
# {2, 3}


# ============================================================
# 21. difference_update()
# ============================================================

set_a = {1, 2, 3}
set_b = {2, 3, 4}

set_a.difference_update(set_b)

print(set_a)
# {1}


# ============================================================
# 22. symmetric_difference_update()
# ============================================================

set_a = {1, 2, 3}
set_b = {2, 3, 4}

set_a.symmetric_difference_update(set_b)

print(set_a)
# {1, 4}


# ============================================================
# 23. Subset
# ============================================================

# A set is a subset if all its elements
# are present in another set.

small = {1, 2}
large = {1, 2, 3, 4}

print(small.issubset(large))
# True


# Using <=

print(small <= large)
# True


# ============================================================
# 24. Superset
# ============================================================

# A set is a superset if it contains all elements
# of another set.

large = {1, 2, 3, 4}
small = {1, 2}

print(large.issuperset(small))
# True


# Using >=

print(large >= small)
# True


# ============================================================
# 25. Disjoint Sets
# ============================================================

# Two sets are disjoint if they have no common elements.

set_a = {1, 2, 3}
set_b = {4, 5, 6}

print(set_a.isdisjoint(set_b))
# True


set_c = {3, 4, 5}

print(set_a.isdisjoint(set_c))
# False


# ============================================================
# 26. Set Comprehension
# ============================================================

# Set comprehension provides a concise way
# to create sets.

numbers = [1, 2, 3, 4, 5]

squares = {
    x ** 2
    for x in numbers
}

print(squares)
# {1, 4, 9, 16, 25}


# With a condition

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {
    x
    for x in numbers
    if x % 2 == 0
}

print(even_numbers)
# {2, 4, 6}


# General syntax:
#
# {expression for item in iterable if condition}


# ============================================================
# 27. Removing Duplicates from a List
# ============================================================

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = list(set(numbers))

print(unique_numbers)

# This removes duplicates.
#
# Important:
# Converting a list to a set does NOT preserve
# the original order.


# ============================================================
# 28. Preserving Order While Removing Duplicates
# ============================================================

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)
# [10, 20, 30, 40]

# This approach removes duplicates while
# preserving insertion order.


# ============================================================
# 29. Set vs List
# ============================================================

# List:
# - Ordered
# - Mutable
# - Allows duplicates
# - Supports indexing
# - Good when order matters
#
# Set:
# - Unordered
# - Mutable
# - Does not allow duplicates
# - Does not support indexing
# - Good for uniqueness and membership checking


# Example:

numbers_list = [10, 20, 10, 30]

numbers_set = {10, 20, 10, 30}

print(numbers_list)
# [10, 20, 10, 30]

print(numbers_set)
# {10, 20, 30}


# ============================================================
# 30. Set vs Tuple
# ============================================================

# Tuple:
# - Ordered
# - Immutable
# - Allows duplicates
# - Supports indexing
#
# Set:
# - Unordered
# - Mutable
# - Does not allow duplicates
# - Does not support indexing


# ============================================================
# 31. Set vs Dictionary
# ============================================================

# Set:
# Stores only unique values.

skills = {"Python", "SQL", "Pandas"}

# Dictionary:
# Stores key-value pairs.

employee = {
    "name": "Trupti",
    "skill": "Python"
}


# ============================================================
# 32. Hashability
# ============================================================

# Set elements must be hashable.

# Immutable types such as:
# int, float, string, tuple
# can generally be set elements.

valid_set = {
    10,
    "Python",
    (1, 2)
}

print(valid_set)


# Lists cannot be set elements because lists are mutable.

# invalid_set = {
#     [1, 2, 3]
# }

# This raises:
# TypeError: unhashable type: 'list'


# ============================================================
# 33. frozenset - Basic Awareness
# ============================================================

# frozenset is an immutable version of a set.

numbers = frozenset([1, 2, 3, 4])

print(numbers)

# You cannot add or remove elements from a frozenset.

# numbers.add(5)
# AttributeError


# ============================================================
# 34. Time Complexity
# ============================================================

# For a normal Python set:

# Add                 -> O(1) average
# Remove              -> O(1) average
# Membership search   -> O(1) average
# Discard             -> O(1) average

# Set operations depend on the size of the sets,
# but are generally efficient for large collections.


# ============================================================
# 35. Data Engineering Use Cases
# ============================================================

# Sets are useful for:
#
# - Removing duplicate records/values
# - Checking whether a value already exists
# - Comparing datasets
# - Finding common values
# - Finding missing values
# - Comparing columns
# - Data validation
# - Finding unique categories


# Example: Unique customer IDs

customer_ids = [
    101, 102, 101, 103, 104, 102
]

unique_customer_ids = set(customer_ids)

print(unique_customer_ids)


# ============================================================
# 36. Comparing Two Datasets
# ============================================================

dataset_a = {"A", "B", "C", "D"}
dataset_b = {"C", "D", "E", "F"}

# Common records

common = dataset_a & dataset_b

print(common)
# {'C', 'D'}


# Records only in dataset A

only_in_a = dataset_a - dataset_b

print(only_in_a)
# {'A', 'B'}


# Records only in dataset B

only_in_b = dataset_b - dataset_a

print(only_in_b)
# {'E', 'F'}


# All unique records

all_records = dataset_a | dataset_b

print(all_records)
# {'A', 'B', 'C', 'D', 'E', 'F'}


# ============================================================
# 37. Data Validation Example
# ============================================================

expected_columns = {
    "id",
    "name",
    "email",
    "salary"
}

actual_columns = {
    "id",
    "name",
    "email"
}

missing_columns = expected_columns - actual_columns

print(missing_columns)
# {'salary'}


# This type of comparison can be useful
# when validating incoming data.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. Sets store unique values.
# 2. Sets are mutable.
# 3. Sets are unordered.
# 4. Sets do not support indexing.
# 5. An empty set is created using set(), not {}.
# 6. add() adds one element.
# 7. update() adds multiple elements.
# 8. remove() raises an error if the element does not exist.
# 9. discard() does not raise an error if the element is missing.
# 10. pop() removes an arbitrary element.
# 11. union() combines unique elements.
# 12. intersection() finds common elements.
# 13. difference() finds elements present in one set only.
# 14. symmetric_difference() finds elements present in either
#     set but not both.
# 15. Sets support subset, superset, and disjoint checks.
# 16. Set comprehension creates sets concisely.
# 17. Sets are very useful for removing duplicates.
# 18. Set membership checking is O(1) on average.
# 19. Set elements must be hashable.
# 20. Sets are useful for data cleaning and validation.