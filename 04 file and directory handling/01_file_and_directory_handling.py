"""
Python File & Directory Handling
================================

File handling is used to work with files and folders from Python.

In Data Engineering, file handling is very important because
data is commonly stored in:

- CSV files
- JSON files
- Parquet files
- Text files
- Data directories

This file covers:

1. with open()
2. Reading files
3. Writing files
4. Appending files
5. File modes
6. pathlib
7. File existence
8. Directories
9. CSV
10. JSON
11. Parquet
12. Relative and absolute paths
13. Practical Data Engineering workflows
"""


# ============================================================
# 1. What is File Handling?
# ============================================================

# File handling means using Python to:
#
# - Create files
# - Read files
# - Write files
# - Update files
# - Check files
# - Work with directories
#
# Example:
#
# A Data Engineering pipeline may:
#
# 1. Read sales.csv
# 2. Clean the data
# 3. Save cleaned data
# 4. Store the result as Parquet


# ============================================================
# 2. with open()
# ============================================================

# open() is used to open a file.

# The basic syntax is:

# open(file_path, mode)


# Example:

file = open("example.txt", "r")

file.close()


# However, manually closing files is not recommended
# when working with normal file-processing code.

# Instead, use:

with open("example.txt", "r") as file:

    content = file.read()

    print(content)


# The 'with' statement automatically closes the file
# after the block is finished.


# ============================================================
# 3. Why Use with open()?
# ============================================================

# Without with:

file = open("example.txt", "r")

content = file.read()

file.close()


# With with:

with open("example.txt", "r") as file:

    content = file.read()


# The second approach is safer and cleaner.


# ============================================================
# 4. File Modes
# ============================================================

# Common file modes:

# "r" -> Read
# "w" -> Write
# "a" -> Append
# "x" -> Create a new file


# ============================================================
# 5. Reading a File
# ============================================================

# "r" means read mode.

with open("example.txt", "r") as file:

    content = file.read()

    print(content)


# ============================================================
# 6. read()
# ============================================================

# read() reads the entire file.

with open("example.txt", "r") as file:

    content = file.read()

    print(content)


# ============================================================
# 7. readline()
# ============================================================

# readline() reads one line at a time.

with open("example.txt", "r") as file:

    first_line = file.readline()

    print(first_line)


# We can read another line:

with open("example.txt", "r") as file:

    first_line = file.readline()

    second_line = file.readline()

    print(first_line)

    print(second_line)


# ============================================================
# 8. readlines()
# ============================================================

# readlines() reads all lines and returns them
# as a list.

with open("example.txt", "r") as file:

    lines = file.readlines()

    print(lines)


# Example:

# File:
#
# Python
# SQL
# Pandas
#
# Result:
#
# ['Python\n', 'SQL\n', 'Pandas\n']


# ============================================================
# 9. Iterating Through a File
# ============================================================

# We can directly iterate through a file.

with open("example.txt", "r") as file:

    for line in file:

        print(line.strip())


# strip() removes extra whitespace and newline characters.


# ============================================================
# 10. Writing to a File
# ============================================================

# "w" means write mode.

with open("output.txt", "w") as file:

    file.write("Hello Python")


# If the file does not exist:
#
# Python creates it.


# If the file already exists:
#
# Its previous content is overwritten.


# ============================================================
# 11. Writing Multiple Lines
# ============================================================

with open("skills.txt", "w") as file:

    file.write("Python\n")

    file.write("SQL\n")

    file.write("Pandas\n")

    file.write("Airflow\n")


# ============================================================
# 12. Appending to a File
# ============================================================

# "a" means append mode.

with open("skills.txt", "a") as file:

    file.write("Docker\n")


# Existing content is preserved.

# New content is added at the end.


# ============================================================
# 13. Read vs Write vs Append
# ============================================================

# "r"
# Read existing file.

# "w"
# Write to file.
# Existing content is overwritten.

# "a"
# Add content at the end.

# "x"
# Create a new file.
# Raises an error if the file already exists.


# ============================================================
# 14. Creating a File with x
# ============================================================

# "x" creates a new file.

# with open("new_file.txt", "x") as file:
#
#     file.write("New file")


# If the file already exists, Python raises:

# FileExistsError


# ============================================================
# 15. Reading and Writing
# ============================================================

# "r+" allows reading and writing.

with open("example.txt", "r+") as file:

    content = file.read()

    print(content)


# Be careful with r+ because writing can modify
# existing file content.


# ============================================================
# 16. pathlib
# ============================================================

# pathlib provides an object-oriented way
# to work with file and directory paths.

from pathlib import Path


# Create a Path object:

path = Path("example.txt")

print(path)


# ============================================================
# 17. Path Name
# ============================================================

path = Path("data/sales.csv")

print(path.name)


# Output:

# sales.csv


# ============================================================
# 18. Path Stem
# ============================================================

path = Path("data/sales.csv")

print(path.stem)


# Output:

# sales


# stem means filename without the extension.


# ============================================================
# 19. Path Suffix
# ============================================================

path = Path("data/sales.csv")

print(path.suffix)


# Output:

# .csv


# ============================================================
# 20. Parent Directory
# ============================================================

path = Path("data/sales.csv")

print(path.parent)


# Output:

# data


# ============================================================
# 21. File Existence
# ============================================================

path = Path("data/sales.csv")

print(path.exists())


# exists() returns:

# True
# or
# False


# ============================================================
# 22. Checking if Path is a File
# ============================================================

path = Path("data/sales.csv")

if path.is_file():

    print("This is a file")


# ============================================================
# 23. Checking if Path is a Directory
# ============================================================

path = Path("data")

if path.is_dir():

    print("This is a directory")


# ============================================================
# 24. Creating Directories
# ============================================================

data_folder = Path("data")

data_folder.mkdir(
    exist_ok=True
)


# exist_ok=True means:
#
# If the directory already exists,
# don't raise an error.


# ============================================================
# 25. Creating Nested Directories
# ============================================================

processed_folder = Path(
    "data/processed/2026"
)


processed_folder.mkdir(
    parents=True,
    exist_ok=True
)


# parents=True allows Python to create
# missing parent directories.


# ============================================================
# 26. Listing Directory Contents
# ============================================================

data_folder = Path("data")


if data_folder.exists():

    for item in data_folder.iterdir():

        print(item)


# ============================================================
# 27. Checking Files Inside a Directory
# ============================================================

data_folder = Path("data")


if data_folder.exists():

    for item in data_folder.iterdir():

        if item.is_file():

            print(item)


# ============================================================
# 28. Checking Directories Inside a Directory
# ============================================================

data_folder = Path("data")


if data_folder.exists():

    for item in data_folder.iterdir():

        if item.is_dir():

            print(item)


# ============================================================
# 29. Joining Paths
# ============================================================

data_folder = Path("data")

file_path = data_folder / "sales.csv"

print(file_path)


# Output:

# data/sales.csv


# Using "/" with pathlib is a convenient way
# to build paths.


# ============================================================
# 30. Relative Path
# ============================================================

path = Path("data/sales.csv")


# This is a relative path.

# It is relative to the current working directory.


# ============================================================
# 31. Absolute Path
# ============================================================

path = Path("data/sales.csv")


print(path.absolute())


# This gives an absolute path.


# ============================================================
# 32. Current Working Directory
# ============================================================

from pathlib import Path


current_directory = Path.cwd()

print(current_directory)


# cwd() means:
#
# Current Working Directory


# ============================================================
# 33. Creating a File Using pathlib
# ============================================================

file_path = Path("example.txt")

file_path.write_text(
    "Hello Python"
)


# pathlib can be used for simple file operations.


# ============================================================
# 34. Reading a File Using pathlib
# ============================================================

file_path = Path("example.txt")

content = file_path.read_text()

print(content)


# ============================================================
# 35. CSV Files
# ============================================================

# CSV stands for:
#
# Comma-Separated Values
#
# CSV is commonly used for tabular data.

# Example:
#
# id,name,salary
# 101,Alice,50000
# 102,Bob,60000


# ============================================================
# 36. Reading CSV with csv Module
# ============================================================

import csv


with open(
    "employees.csv",
    "r",
    newline=""
) as file:

    reader = csv.reader(file)

    for row in reader:

        print(row)


# Each row is returned as a list.


# ============================================================
# 37. csv.reader()
# ============================================================

# Example CSV:
#
# id,name,department
# 101,Alice,IT
# 102,Bob,HR


with open(
    "employees.csv",
    "r",
    newline=""
) as file:

    reader = csv.reader(file)

    for row in reader:

        print(row)


# Output:

# ['id', 'name', 'department']
# ['101', 'Alice', 'IT']
# ['102', 'Bob', 'HR']


# ============================================================
# 38. Reading CSV with DictReader
# ============================================================

# DictReader treats the first row as column names.

with open(
    "employees.csv",
    "r",
    newline=""
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        print(row)


# Each row behaves like a dictionary.


# Example:

# {
#     'id': '101',
#     'name': 'Alice',
#     'department': 'IT'
# }


# ============================================================
# 39. Accessing CSV Columns
# ============================================================

with open(
    "employees.csv",
    "r",
    newline=""
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        print(row["name"])

        print(row["department"])


# ============================================================
# 40. Writing CSV
# ============================================================

with open(
    "employees_output.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(
        ["id", "name", "department"]
    )

    writer.writerow(
        [101, "Alice", "IT"]
    )

    writer.writerow(
        [102, "Bob", "HR"]
    )


# ============================================================
# 41. Writing Multiple CSV Rows
# ============================================================

rows = [
    ["id", "name", "salary"],
    [101, "Alice", 50000],
    [102, "Bob", 60000],
    [103, "Charlie", 55000]
]


with open(
    "salary.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerows(rows)


# ============================================================
# 42. DictWriter
# ============================================================

employees = [
    {
        "id": 101,
        "name": "Alice",
        "department": "IT"
    },
    {
        "id": 102,
        "name": "Bob",
        "department": "HR"
    }
]


with open(
    "employees_dict.csv",
    "w",
    newline=""
) as file:

    fieldnames = [
        "id",
        "name",
        "department"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(employees)


# ============================================================
# 43. JSON
# ============================================================

# JSON stands for:
#
# JavaScript Object Notation
#
# JSON is commonly used for:
#
# - APIs
# - Configuration files
# - Data exchange
# - Nested data


# Example JSON:
#
# {
#     "name": "Alice",
#     "age": 25,
#     "skills": ["Python", "SQL"]
# }


# ============================================================
# 44. Python Dictionary vs JSON Object
# ============================================================

# Python dictionary:

employee = {
    "name": "Alice",
    "age": 25
}


# JSON represents similar data as text:

# {
#     "name": "Alice",
#     "age": 25
# }


# Important:
#
# A Python dictionary is a Python object.
#
# JSON is a text/data interchange format.


# ============================================================
# 45. json Module
# ============================================================

import json


# ============================================================
# 46. Reading JSON File
# ============================================================

with open(
    "employee.json",
    "r"
) as file:

    data = json.load(file)

    print(data)


# json.load()
#
# JSON file -> Python object


# ============================================================
# 47. Accessing JSON Data
# ============================================================

with open(
    "employee.json",
    "r"
) as file:

    employee = json.load(file)


print(employee["name"])

print(employee["age"])


# ============================================================
# 48. Writing JSON
# ============================================================

employee = {
    "id": 101,
    "name": "Alice",
    "department": "IT"
}


with open(
    "employee_output.json",
    "w"
) as file:

    json.dump(
        employee,
        file,
        indent=4
    )


# indent=4 makes the JSON easier to read.


# ============================================================
# 49. json.dumps()
# ============================================================

# dumps() converts a Python object into
# a JSON string.

employee = {
    "name": "Alice",
    "age": 25
}


json_string = json.dumps(employee)

print(json_string)

print(type(json_string))


# ============================================================
# 50. json.loads()
# ============================================================

# loads() converts a JSON string into
# a Python object.

json_string = """
{
    "name": "Alice",
    "age": 25
}
"""


employee = json.loads(json_string)

print(employee)

print(employee["name"])


# ============================================================
# 51. load vs loads
# ============================================================

# json.load()
#
# Reads JSON from a file.


# json.loads()
#
# Reads JSON from a string.


# Remember:

# load  -> file
# loads -> string


# ============================================================
# 52. dump vs dumps
# ============================================================

# json.dump()
#
# Writes JSON to a file.


# json.dumps()
#
# Converts Python object into JSON string.


# Remember:

# dump  -> file
# dumps -> string


# ============================================================
# 53. Nested JSON
# ============================================================

employee = {
    "name": "Alice",
    "address": {
        "city": "Pune",
        "country": "India"
    },
    "skills": [
        "Python",
        "SQL",
        "Pandas"
    ]
}


print(employee["address"]["city"])

print(employee["skills"][0])


# Nested JSON is especially important
# when working with APIs.


# ============================================================
# 54. Parquet
# ============================================================

# Parquet is a columnar storage file format.

# It is widely used in Data Engineering
# and Big Data systems.


# Common characteristics:

# - Columnar storage
# - Efficient compression
# - Efficient analytical queries
# - Preserves data types/schema
# - Common in data lakes and warehouses


# ============================================================
# 55. Why Parquet?
# ============================================================

# Consider a dataset with:

# customer_id
# name
# age
# salary
# city


# If we only need salary,
# a columnar format can efficiently work
# with the required column rather than treating
# the data as traditional row-oriented text.


# Parquet is therefore commonly used
# for analytical workloads.


# ============================================================
# 56. Installing pandas and pyarrow
# ============================================================

# To work with Parquet using pandas,
# a suitable Parquet engine such as pyarrow
# is commonly installed.

# Example:

# pip install pandas pyarrow


# ============================================================
# 57. Reading Parquet
# ============================================================

import pandas as pd


# Example:

# df = pd.read_parquet("sales.parquet")

# print(df)


# ============================================================
# 58. Writing Parquet
# ============================================================

# Example:

# df.to_parquet(
#     "sales.parquet",
#     index=False
# )


# index=False prevents the pandas index
# from being stored as an extra column.


# ============================================================
# 59. CSV vs JSON vs Parquet
# ============================================================

# CSV:
#
# Best suited for:
# - Simple tabular data
# - Sharing data
# - Basic data exchange
#
# Advantages:
# - Simple
# - Human-readable
# - Widely supported
#
# Limitations:
# - Does not naturally preserve rich data types
# - Not ideal for nested data
# - Can become inefficient for large analytical workloads


# JSON:
#
# Best suited for:
# - APIs
# - Nested data
# - Configuration
# - Data exchange
#
# Advantages:
# - Supports nested structures
# - Human-readable
# - Common in web APIs
#
# Limitations:
# - Larger file size
# - Less efficient for large tabular analytics


# Parquet:
#
# Best suited for:
# - Data Engineering
# - Data Lakes
# - Analytical workloads
# - Large datasets
#
# Advantages:
# - Columnar
# - Efficient compression
# - Preserves data types
# - Efficient for analytical processing
#
# Limitations:
# - Not as human-readable as CSV/JSON
# - Usually requires tools/libraries to inspect easily


# ============================================================
# 60. Relative vs Absolute Paths
# ============================================================

# Relative path:

path = Path("data/sales.csv")


# Absolute path:

# Example:
#
# C:/Users/Trupti/project/data/sales.csv


# Relative paths are generally more portable
# within a project.


# ============================================================
# 61. Recommended Project Structure
# ============================================================

# A Data Engineering project can have:

# project/
#
# ├── data/
# │   ├── raw/
# │   ├── processed/
# │   └── output/
# │
# ├── src/
# │
# ├── tests/
# │
# └── main.py


# ============================================================
# 62. Checking Input File Before Processing
# ============================================================

input_file = Path(
    "data/raw/sales.csv"
)


if input_file.exists():

    print("Input file exists")

else:

    print("Input file does not exist")


# This is useful before starting
# a data processing task.


# ============================================================
# 63. Creating Input and Output Directories
# ============================================================

raw_folder = Path("data/raw")

processed_folder = Path("data/processed")

output_folder = Path("data/output")


raw_folder.mkdir(
    parents=True,
    exist_ok=True
)

processed_folder.mkdir(
    parents=True,
    exist_ok=True
)

output_folder.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 64. Practical Data Engineering Workflow
# ============================================================

# Basic workflow:

# Raw data
#    ↓
# Read file
#    ↓
# Validate file exists
#    ↓
# Process data
#    ↓
# Save processed data


# Example:

input_file = Path(
    "data/raw/sales.csv"
)

output_file = Path(
    "data/processed/sales.csv"
)


if input_file.exists():

    print("Reading:", input_file)

    # Data processing would happen here.

    print("Saving:", output_file)

else:

    print("Input file not found")


# ============================================================
# 65. Practical Example - Date-Based File Name
# ============================================================

from datetime import date


processing_date = date.today()


file_name = (
    f"sales_"
    f"{processing_date.strftime('%Y%m%d')}"
    f".csv"
)


print(file_name)


# Example:

# sales_20260818.csv


# ============================================================
# 66. Practical Example - Raw to Processed
# ============================================================

raw_folder = Path("data/raw")

processed_folder = Path("data/processed")


raw_folder.mkdir(
    parents=True,
    exist_ok=True
)

processed_folder.mkdir(
    parents=True,
    exist_ok=True
)


input_file = raw_folder / "sales.csv"

output_file = processed_folder / "sales.parquet"


print("Input:", input_file)

print("Output:", output_file)


# ============================================================
# 67. Practical Example - CSV to Parquet
# ============================================================

# This is a common Data Engineering workflow.

# Step 1:
# Read CSV.

# df = pd.read_csv(
#     "data/raw/sales.csv"
# )


# Step 2:
# Perform processing.

# df = df.drop_duplicates()


# Step 3:
# Save as Parquet.

# df.to_parquet(
#     "data/processed/sales.parquet",
#     index=False
# )


# This example connects:
#
# CSV
# +
# pandas
# +
# Parquet


# ============================================================
# 68. Practical Example - JSON to Python
# ============================================================

json_file = Path(
    "data/raw/employee.json"
)


if json_file.exists():

    with open(
        json_file,
        "r"
    ) as file:

        data = json.load(file)

        print(data)


# ============================================================
# 69. Practical Example - List All CSV Files
# ============================================================

data_folder = Path("data")


if data_folder.exists():

    for file in data_folder.iterdir():

        if file.suffix == ".csv":

            print(file)


# ============================================================
# 70. Practical Example - Find All Parquet Files
# ============================================================

data_folder = Path("data")


if data_folder.exists():

    for file in data_folder.iterdir():

        if file.suffix == ".parquet":

            print(file)


# ============================================================
# 71. Basic Path Filtering
# ============================================================

data_folder = Path("data")


if data_folder.exists():

    csv_files = [
        file
        for file in data_folder.iterdir()
        if file.suffix == ".csv"
    ]

    print(csv_files)


# This combines pathlib with
# list comprehension.


# ============================================================
# 72. File Size
# ============================================================

file_path = Path(
    "example.txt"
)


if file_path.exists():

    print(
        file_path.stat().st_size
    )


# st_size gives the file size in bytes.


# ============================================================
# 73. Important pathlib Attributes
# ============================================================

path = Path(
    "data/sales_2026.csv"
)


print(path.name)

print(path.stem)

print(path.suffix)

print(path.parent)


# Output conceptually:

# name   -> sales_2026.csv
# stem   -> sales_2026
# suffix -> .csv
# parent -> data


# ============================================================
# 74. Important pathlib Methods
# ============================================================

path = Path("data/sales.csv")


# Check existence:

path.exists()


# Check file:

path.is_file()


# Check directory:

path.is_dir()


# Get absolute path:

path.absolute()


# Create directory:

path.mkdir(
    parents=True,
    exist_ok=True
)


# List contents:

path.iterdir()


# Read text:

path.read_text()


# Write text:

path.write_text(
    "Hello"
)


# ============================================================
# 75. Common Mistakes
# ============================================================

# Mistake 1:
# Forgetting to close files when not using with.

# Better:

with open("file.txt", "r") as file:

    content = file.read()


# ============================================================

# Mistake 2:
# Using "w" when you actually want to append.

# "w" overwrites existing content.

# "a" adds content at the end.


# ============================================================

# Mistake 3:
# Assuming a file exists.

# Better:

path = Path("data.csv")

if path.exists():

    print("File found")


# ============================================================

# Mistake 4:
# Confusing JSON with Python dictionaries.

# A Python dictionary is an object in Python.

# JSON is a data format.


# ============================================================

# Mistake 5:
# Treating CSV and Parquet as the same thing.

# CSV is text-based and simple.

# Parquet is a columnar storage format
# designed for efficient analytical workloads.


# ============================================================
# 76. Key Takeaways
# ============================================================

# 1. Use with open() for normal file handling.
#
# 2. "r" is for reading.
#
# 3. "w" is for writing and can overwrite.
#
# 4. "a" is for appending.
#
# 5. read() reads the complete file.
#
# 6. readline() reads one line.
#
# 7. readlines() returns lines as a list.
#
# 8. pathlib provides a convenient way
#    to work with paths.
#
# 9. exists() checks whether a path exists.
#
# 10. is_file() checks whether a path is a file.
#
# 11. is_dir() checks whether a path is a directory.
#
# 12. mkdir() creates directories.
#
# 13. iterdir() lists directory contents.
#
# 14. CSV is commonly used for tabular data.
#
# 15. JSON is commonly used for APIs and nested data.
#
# 16. Parquet is commonly used for
#     Data Engineering and analytical workloads.
#
# 17. pathlib makes file paths easier to manage.
#
# 18. Always validate important input files
#     before processing them.


# ============================================================
# 77. Quick Revision Table
# ============================================================

# Operation                    Function / Method
#
# Open file                    open()
#
# Recommended file handling    with open()
#
# Read complete file           read()
#
# Read one line                readline()
#
# Read all lines               readlines()
#
# Write                        write()
#
# Append                       "a"
#
# Check path                   exists()
#
# Check file                   is_file()
#
# Check directory              is_dir()
#
# Create directory             mkdir()
#
# List directory               iterdir()
#
# Current directory            Path.cwd()
#
# File name                   .name
#
# File without extension      .stem
#
# Extension                   .suffix
#
# Parent directory            .parent
#
# Read JSON                    json.load()
#
# Write JSON                   json.dump()
#
# JSON string -> Python        json.loads()
#
# Python -> JSON string        json.dumps()
#
# Read Parquet                 pd.read_parquet()
#
# Write Parquet                df.to_parquet()


# ============================================================
# 78. CSV vs JSON vs Parquet
# ============================================================

# CSV
#
# Use when:
# - Data is tabular
# - Simplicity is important
# - Human readability is useful


# JSON
#
# Use when:
# - Working with APIs
# - Data is nested
# - Data exchange is required


# Parquet
#
# Use when:
# - Working with large datasets
# - Analytical processing is required
# - Efficient storage is important
# - Working in Data Engineering pipelines


# ============================================================
# 79. PRACTICE QUESTIONS
# ============================================================

# Practice 1:
# Create a text file using with open()
# and write 5 lines into it.


# Practice 2:
# Read the complete file using read().


# Practice 3:
# Read the file line-by-line.


# Practice 4:
# Append a new line to the file.


# Practice 5:
# Create a Path object for:
#
# data/sales.csv


# Practice 6:
# Print:
#
# - file name
# - stem
# - suffix
# - parent directory


# Practice 7:
# Check whether:
#
# data/sales.csv
#
# exists.


# Practice 8:
# Check whether a given path
# is a file or directory.


# Practice 9:
# Create:
#
# data/raw
# data/processed
# data/output


# Practice 10:
# List all files inside
# the data directory.


# Practice 11:
# List only CSV files.


# Practice 12:
# Create a CSV file containing:
#
# id
# name
# salary


# Practice 13:
# Read the CSV using csv.reader.


# Practice 14:
# Read the same CSV using DictReader.


# Practice 15:
# Create a JSON file containing:
#
# name
# age
# skills


# Practice 16:
# Read the JSON file using json.load().


# Practice 17:
# Convert a Python dictionary
# into a JSON string using json.dumps().


# Practice 18:
# Convert a JSON string back into
# a Python dictionary using json.loads().


# Practice 19:
# Create a pandas DataFrame
# and save it as Parquet.


# Practice 20:
# Read the Parquet file using pandas.


# Practice 21:
# Explain the difference between:
#
# CSV
# JSON
# Parquet


# Practice 22:
# Build a small workflow:
#
# data/raw/sales.csv
#       ↓
# Read CSV
#       ↓
# Remove duplicate records
#       ↓
# Save:
# data/processed/sales.parquet


# Practice 23:
# Check whether the input file exists
# before processing it.


# Practice 24:
# Create a date-based output filename:
#
# sales_YYYYMMDD.csv


# Practice 25:
# Create this directory structure
# using pathlib:
#
# data/
# ├── raw/
# ├── processed/
# └── output/


# ============================================================
# END OF FILE & DIRECTORY HANDLING
# ============================================================
