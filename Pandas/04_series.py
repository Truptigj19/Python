"""
============================================================
PANDAS - SERIES
============================================================

A Series is a one-dimensional labeled data structure in
Pandas.

Think of a Series as a single column of a DataFrame.

Example:

    Employee
    --------
    Asha
    Rahul
    Neha

A Series contains:
    - Values
    - Index
    - Data type


------------------------------------------------------------
WHY USE SERIES?
------------------------------------------------------------

Series are useful when working with a single column or
one-dimensional data.

Common uses:
    - Storing a single column
    - Performing calculations
    - Filtering values
    - Statistical operations
    - Vectorized operations


------------------------------------------------------------
WAYS TO CREATE A SERIES
------------------------------------------------------------

1. From a list

    pd.Series([10, 20, 30])


2. From a dictionary

    pd.Series({
        "A": 10,
        "B": 20,
        "C": 30
    })


3. With a custom index

    pd.Series(
        [10, 20, 30],
        index=["A", "B", "C"]
    )


------------------------------------------------------------
SERIES VS DATAFRAME
------------------------------------------------------------

Series:
    - One-dimensional
    - Represents a single column
    - Has an index and values

DataFrame:
    - Two-dimensional
    - Contains rows and columns
    - Can contain multiple Series


Example:

    DataFrame
        |
        |-- Name      -> Series
        |-- Salary    -> Series
        |-- City      -> Series


------------------------------------------------------------
IMPORTANT SERIES OPERATIONS
------------------------------------------------------------

    series.max()       -> Maximum value
    series.min()       -> Minimum value
    series.mean()      -> Average
    series.sum()       -> Sum
    series.count()     -> Number of non-null values
    series.unique()    -> Unique values
    series.nunique()   -> Number of unique values
    series.dtype       -> Data type
    series.index       -> Index
    series.values      -> Values


------------------------------------------------------------
VECTORISED OPERATIONS
------------------------------------------------------------

Pandas allows operations to be performed on all values
without explicitly using a loop.

Example:

    salary + 5000

adds 5000 to every salary.

Similarly:

    salary * 2
    salary / 2
    salary - 1000


============================================================
PRACTICE
============================================================

Scenario:
We have employee salary data.

Employee     Salary
Asha         65000
Rahul        48000
Neha         72000
Om           58000
Priya        52000

Tasks:

1. Create a Series using a list.
2. Create a Series with custom employee IDs.
3. Create a Series using a dictionary.
4. Access the salary of EMP003.
5. Find the maximum salary.
6. Find the minimum salary.
7. Calculate the average salary.
8. Add 5000 to every salary.
9. Check the data type.
10. Find the total salary.


============================================================
SOLUTION
============================================================
"""

import pandas as pd


# ============================================================
# 1. CREATE SERIES USING A LIST
# ============================================================

salaries = [65000, 48000, 72000, 58000, 52000]

salary_series = pd.Series(salaries)

print("Series using List:")
print(salary_series)


# ============================================================
# 2. CREATE SERIES WITH CUSTOM INDEX
# ============================================================

employee_ids = [
    "EMP001",
    "EMP002",
    "EMP003",
    "EMP004",
    "EMP005"
]

salary_series = pd.Series(
    salaries,
    index=employee_ids
)

print("\nSeries with Custom Index:")
print(salary_series)


# ============================================================
# 3. CREATE SERIES USING DICTIONARY
# ============================================================

salary_dict = {
    "EMP001": 65000,
    "EMP002": 48000,
    "EMP003": 72000,
    "EMP004": 58000,
    "EMP005": 52000
}

salary_series_dict = pd.Series(salary_dict)

print("\nSeries using Dictionary:")
print(salary_series_dict)


# ============================================================
# 4. ACCESS SALARY OF EMP003
# ============================================================

print("\nSalary of EMP003:")
print(salary_series["EMP003"])


# ============================================================
# 5. MAXIMUM SALARY
# ============================================================

print("\nMaximum Salary:")
print(salary_series.max())


# ============================================================
# 6. MINIMUM SALARY
# ============================================================

print("\nMinimum Salary:")
print(salary_series.min())


# ============================================================
# 7. AVERAGE SALARY
# ============================================================

print("\nAverage Salary:")
print(salary_series.mean())


# ============================================================
# 8. ADD 5000 TO EVERY SALARY
# ============================================================

updated_salary = salary_series + 5000

print("\nUpdated Salaries:")
print(updated_salary)


# ============================================================
# 9. CHECK DATA TYPE
# ============================================================

print("\nData Type:")
print(salary_series.dtype)


# ============================================================
# 10. TOTAL SALARY
# ============================================================

print("\nTotal Salary:")
print(salary_series.sum())


# ============================================================
# IMPORTANT EXAMPLES
# ============================================================

print("\nVectorized Operations:")

print("\nSalary * 2:")
print(salary_series * 2)

print("\nSalary - 1000:")
print(salary_series - 1000)


"""
============================================================
INTERVIEW QUESTIONS
============================================================

Q1. What is a Pandas Series?

Answer:
A Series is a one-dimensional labeled data structure in
Pandas that can store data along with an index.


Q2. What is the difference between Series and DataFrame?

Answer:
A Series is one-dimensional, while a DataFrame is
two-dimensional and consists of rows and columns.


Q3. Can a Series have a custom index?

Answer:
Yes.

Example:

    pd.Series(
        [10, 20, 30],
        index=["A", "B", "C"]
    )


Q4. How can you access a value using its index?

Answer:

    series["EMP003"]


Q5. What does series.mean() do?

Answer:
It returns the average of the numerical values in the Series.


Q6. What is vectorization in Pandas?

Answer:
Vectorization allows operations to be performed on an entire
Series or column without explicitly writing a loop.


Example:

    salary_series + 5000


============================================================
DATA ENGINEERING CONNECTION
============================================================

Series operations are frequently used during data
transformation and cleaning.

For example:

    df["Salary"] + 5000

can transform an entire column at once.

Other common transformations include:

    df["Salary"] * 1.10
    df["Quantity"] * df["Price"]
    df["Name"].str.upper()

These types of operations are commonly used in
ETL/ELT pipelines.


============================================================
KEY TAKEAWAYS
============================================================

Remember:

    Series       -> 1D
    DataFrame    -> 2D

    max()        -> Maximum
    min()        -> Minimum
    mean()       -> Average
    sum()        -> Total
    dtype        -> Data type
    index        -> Labels
    values       -> Actual values

Most importantly:

    DataFrame column -> Series

Example:

    df["Salary"]

returns a Series.


============================================================
END OF TOPIC
============================================================
"""