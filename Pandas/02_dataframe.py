'''
A DataFrame is a two-dimensional, labeled data structure in Pandas.
'''
import pandas as pd

# 1. DataFrame using Dictionary of Lists

employees = {
    "Employee": ["Asha", "Rahul", "Neha", "Om", "Priya"],
    "Department": ["IT", "HR", "IT", "Finance", "Marketing"],
    "Salary": [65000, 48000, 72000, 58000, 52000],
    "Experience": [2, 3, 4, 2, 1]
}

df1 = pd.DataFrame(employees)

print("DataFrame using Dictionary of Lists:")
print(df1)

