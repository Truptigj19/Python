"""
============================================================
PANDAS - CATEGORICAL DATA
============================================================

Categorical data is data that contains a limited and fixed
number of possible values.

Examples:

    Department:
        IT
        HR
        Finance
        Marketing

    Gender:
        Male
        Female

    Membership:
        Basic
        Premium
        VIP

    Size:
        Small
        Medium
        Large


------------------------------------------------------------
WHAT IS CATEGORICAL DATA?
------------------------------------------------------------

Categorical data represents values that belong to a specific
set of categories.

For example:

    Department

    IT
    HR
    IT
    Finance
    HR

Here, the possible categories are:

    IT
    HR
    Finance


------------------------------------------------------------
WHY USE CATEGORICAL DATA IN PANDAS?
------------------------------------------------------------

By default, Pandas may store string-based categorical
columns as object/string data.

When a column has a limited number of repeated values,
converting it to the "category" dtype can:

    - Reduce memory usage
    - Improve performance in some operations
    - Clearly represent that the column contains categories
    - Make category-based operations easier


------------------------------------------------------------
OBJECT/STRING VS CATEGORY
------------------------------------------------------------

Example:

    Department
    ----------
    IT
    HR
    IT
    Finance
    HR

Initially it may have dtype:

    object

After conversion:

    category


------------------------------------------------------------
CREATING CATEGORICAL DATA
------------------------------------------------------------

Method 1:

    pd.Series(
        ["IT", "HR", "Finance"],
        dtype="category"
    )


Method 2:

    df["Department"] = df["Department"].astype("category")


------------------------------------------------------------
IMPORTANT CATEGORY ATTRIBUTES AND METHODS
------------------------------------------------------------

    series.dtype

        Shows the data type.


    series.cat.categories

        Returns all available categories.


    series.cat.codes

        Returns the numerical code assigned to each category.


    series.cat.add_categories()

        Adds a new category.


    series.cat.remove_categories()

        Removes a category.


    series.cat.rename_categories()

        Renames existing categories.


    series.cat.set_categories()

        Sets the complete list of categories.


    series.cat.reorder_categories()

        Changes the order of categories.


============================================================
PRACTICE DATASET
============================================================

Scenario:

We have employee information.

Employee     Department    Employment_Type    Performance
Asha         IT            Full-Time          Excellent
Rahul        HR            Full-Time          Good
Neha         IT            Intern             Good
Om           Finance       Full-Time          Average
Priya        HR            Intern             Excellent
Kiran        IT            Full-Time          Good
Sneha        Finance       Intern             Average

We will identify categorical columns and practice
categorical operations.


============================================================
PRACTICE TASKS
============================================================

1. Create the employee DataFrame.

2. Check the data types.

3. Convert Department to categorical data.

4. Convert Employment_Type to categorical data.

5. Convert Performance to categorical data.

6. Display the categories in Department.

7. Display the category codes.

8. Add a new category "Management" to Department.

9. Rename "Full-Time" to "Permanent" in Employment_Type.

10. Check the final data types.

11. Find how many unique departments exist.

12. Display the value counts for Department.


============================================================
SOLUTION
============================================================
"""

import pandas as pd


# ============================================================
# 1. CREATE EMPLOYEE DATASET
# ============================================================

employees = {
    "Employee": [
        "Asha",
        "Rahul",
        "Neha",
        "Om",
        "Priya",
        "Kiran",
        "Sneha"
    ],

    "Department": [
        "IT",
        "HR",
        "IT",
        "Finance",
        "HR",
        "IT",
        "Finance"
    ],

    "Employment_Type": [
        "Full-Time",
        "Full-Time",
        "Intern",
        "Full-Time",
        "Intern",
        "Full-Time",
        "Intern"
    ],

    "Performance": [
        "Excellent",
        "Good",
        "Good",
        "Average",
        "Excellent",
        "Good",
        "Average"
    ]
}

df = pd.DataFrame(employees)

print("Employee DataFrame:")
print(df)


# ============================================================
# 2. CHECK DATA TYPES
# ============================================================

print("\nOriginal Data Types:")
print(df.dtypes)


# ============================================================
# 3. CONVERT DEPARTMENT TO CATEGORY
# ============================================================

df["Department"] = df["Department"].astype("category")

print("\nDepartment Data Type:")
print(df["Department"].dtype)


# ============================================================
# 4. CONVERT EMPLOYMENT TYPE TO CATEGORY
# ============================================================

df["Employment_Type"] = df["Employment_Type"].astype("category")

print("\nEmployment Type Data Type:")
print(df["Employment_Type"].dtype)


# ============================================================
# 5. CONVERT PERFORMANCE TO CATEGORY
# ============================================================

df["Performance"] = df["Performance"].astype("category")

print("\nPerformance Data Type:")
print(df["Performance"].dtype)


# ============================================================
# 6. DISPLAY DEPARTMENT CATEGORIES
# ============================================================

print("\nDepartment Categories:")
print(df["Department"].cat.categories)


# ============================================================
# 7. DISPLAY CATEGORY CODES
# ============================================================

print("\nDepartment Category Codes:")
print(df["Department"].cat.codes)


# ============================================================
# 8. ADD NEW CATEGORY
# ============================================================

df["Department"] = df["Department"].cat.add_categories(
    ["Management"]
)

print("\nCategories After Adding Management:")
print(df["Department"].cat.categories)


# ============================================================
# 9. RENAME CATEGORY
# ============================================================

df["Employment_Type"] = (
    df["Employment_Type"]
    .cat.rename_categories({
        "Full-Time": "Permanent"
    })
)

print("\nEmployment Type After Renaming:")
print(df["Employment_Type"])


# ============================================================
# 10. CHECK FINAL DATA TYPES
# ============================================================

print("\nFinal Data Types:")
print(df.dtypes)


# ============================================================
# 11. NUMBER OF UNIQUE DEPARTMENTS
# ============================================================

print("\nNumber of Unique Departments:")
print(df["Department"].nunique())


# ============================================================
# 12. VALUE COUNTS
# ============================================================

print("\nDepartment Value Counts:")
print(df["Department"].value_counts())


"""
============================================================
IMPORTANT CATEGORY OPERATIONS
============================================================

Convert to category:

    df["Department"] = df["Department"].astype("category")


Get categories:

    df["Department"].cat.categories


Get category codes:

    df["Department"].cat.codes


Add category:

    df["Department"].cat.add_categories(["Management"])


Rename categories:

    df["Department"].cat.rename_categories({
        "IT": "Information Technology"
    })


Remove categories:

    df["Department"].cat.remove_categories([
        "Finance"
    ])


Set categories:

    df["Department"].cat.set_categories([
        "IT",
        "HR",
        "Finance",
        "Marketing"
    ])


============================================================
IMPORTANT CONCEPT - CATEGORY CODES
============================================================

Pandas internally represents categories using codes.

For example:

    Category
    --------
    Finance
    HR
    IT

may internally have codes such as:

    Finance  -> 0
    HR       -> 1
    IT       -> 2

You can see the codes using:

    df["Department"].cat.codes

The exact numerical codes depend on the category ordering.


============================================================
ORDERED CATEGORICAL DATA
============================================================

Some categorical data has a natural order.

Example:

    Low < Medium < High

or:

    Bronze < Silver < Gold

For such data, we can create an ordered categorical column.

Example:

    priority = pd.Categorical(
        ["High", "Low", "Medium"],
        categories=["Low", "Medium", "High"],
        ordered=True
    )


Now Pandas understands:

    Low < Medium < High


This is useful when sorting or comparing ordered categories.


============================================================
EXAMPLE OF ORDERED CATEGORIES
============================================================
"""

priority = pd.Categorical(
    ["High", "Low", "Medium", "High", "Low"],
    categories=["Low", "Medium", "High"],
    ordered=True
)

priority_series = pd.Series(priority)

print("\nOrdered Priority:")
print(priority_series)

print("\nSorted Priority:")
print(priority_series.sort_values())


"""
============================================================
CATEGORICAL DATA - INTERVIEW QUESTIONS
============================================================

Q1. What is categorical data in Pandas?

Answer:

Categorical data represents values that belong to a limited
and predefined set of categories.

Examples include department, gender, product type, and
membership level.


------------------------------------------------------------

Q2. Why would you convert a column to category dtype?

Answer:

Categorical dtype can reduce memory usage when a column has
a limited number of repeated values. It also explicitly
represents the data as categorical.


------------------------------------------------------------

Q3. How do you convert a column to categorical?

Answer:

    df["Department"] = df["Department"].astype("category")


------------------------------------------------------------

Q4. How do you see the categories?

Answer:

    df["Department"].cat.categories


------------------------------------------------------------

Q5. How do you get category codes?

Answer:

    df["Department"].cat.codes


------------------------------------------------------------

Q6. What is ordered categorical data?

Answer:

Ordered categorical data is categorical data where the
categories have a meaningful order.

Example:

    Low < Medium < High


------------------------------------------------------------

Q7. Difference between object/string and category?

Answer:

Object/string generally stores the actual text values,
whereas category stores a fixed set of categories and
internally represents values using category codes.


============================================================
DATA ENGINEERING CONNECTION
============================================================

Categorical data is common in real-world datasets.

Examples:

    Customer Type
    Product Category
    Region
    Department
    Order Status
    Payment Method
    Membership Level

For example, an order dataset might contain:

    Order_Status

    Pending
    Shipped
    Delivered
    Cancelled

Since the same values repeat across many rows, converting
this column to category can be useful.

Categorical data is especially useful when working with
large datasets where memory efficiency matters.


============================================================
KEY TAKEAWAYS
============================================================

Remember:

    category
        ↓
    Limited set of repeated values

    astype("category")
        ↓
    Convert column to categorical dtype

    .cat.categories
        ↓
    Get categories

    .cat.codes
        ↓
    Get numerical category codes

    .cat.add_categories()
        ↓
    Add categories

    .cat.rename_categories()
        ↓
    Rename categories

    ordered=True
        ↓
    Create ordered categorical data


============================================================
END OF TOPIC
============================================================
"""
