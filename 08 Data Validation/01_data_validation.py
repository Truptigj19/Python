"""
Python Data Validation
======================

Data validation means checking whether data is:

- Complete
- Correct
- Consistent
- In the expected format
- Suitable for further processing

In Data Engineering, validation is commonly performed
after extracting data and before transforming or loading it.

Typical workflow:

Source
  ↓
Extract
  ↓
Validate
  ↓
Transform
  ↓
Load


Main validation checks:

1. Schema / Column checks
2. Null checks
3. Duplicate checks
4. Record-count checks
5. Datatype checks
6. Business-rule checks
"""


# ============================================================
# 1. What is Data Validation?
# ============================================================

# Data validation means checking whether incoming data
# satisfies the expected conditions before processing it.
#
# Example:
#
# Expected columns:
#
# id
# name
# email
# salary
#
# If the source suddenly sends:
#
# id
# name
# salary
# department
#
# The data structure has changed.
#
# Validation should detect this before the pipeline
# continues.


# ============================================================
# 2. Why Data Validation is Important
# ============================================================

# Without validation, incorrect data can enter:
#
# - Database
# - Data warehouse
# - Data lake
# - Reports
# - Dashboards
# - Machine learning pipelines
#
#
# Validation helps prevent bad data from moving
# further through the pipeline.


# ============================================================
# 3. Schema / Column Checks
# ============================================================

# A schema describes the expected structure of data.
#
# Example expected columns:

expected_columns = [
    "id",
    "name",
    "email",
    "salary"
]


# Example incoming columns:

actual_columns = [
    "id",
    "name",
    "email",
    "salary"
]


if actual_columns == expected_columns:

    print("Column structure is valid")

else:

    print("Column structure is invalid")


# ============================================================
# 4. Check for Missing Columns
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


if missing_columns:

    print(
        f"Missing columns: {missing_columns}"
    )

else:

    print("No required columns are missing")


# ============================================================
# 5. Check for Unexpected Columns
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
    "email",
    "salary",
    "department"
}


unexpected_columns = actual_columns - expected_columns


if unexpected_columns:

    print(
        f"Unexpected columns: {unexpected_columns}"
    )


# ============================================================
# 6. Null Checks
# ============================================================

# A null value means data is missing.
#
# Example:
#
# id      name       salary
# 101     Alice      50000
# 102     Bob        None
#
#
# Some columns may allow null values.
# Some columns may be required.


data = {
    "id": 101,
    "name": "Alice",
    "email": None,
    "salary": 50000
}


if data["email"] is None:

    print("Email is missing")


# Important:
#
# None represents a missing value in Python.
#
# Do not use:
#
# data["email"] == None
#
# Prefer:
#
# data["email"] is None


# ============================================================
# 7. Required Field Check
# ============================================================

required_fields = [
    "id",
    "name",
    "email"
]


record = {
    "id": 101,
    "name": "Alice",
    "email": None
}


for field in required_fields:

    if record.get(field) is None:

        print(
            f"Required field is missing: {field}"
        )


# ============================================================
# 8. Duplicate Checks
# ============================================================

# Duplicate records can cause problems in data pipelines.
#
# Example:
#
# id = 101
# id = 101
#
# If id is supposed to be unique,
# this is a data quality problem.


ids = [101, 102, 103, 101]


if len(ids) != len(set(ids)):

    print("Duplicate IDs found")

else:

    print("No duplicates found")


# ============================================================
# 9. Finding Duplicate Values
# ============================================================

ids = [101, 102, 103, 101, 102]

seen = set()
duplicates = set()


for value in ids:

    if value in seen:

        duplicates.add(value)

    else:

        seen.add(value)


print(duplicates)

# {101, 102}


# ============================================================
# 10. Record Count Checks
# ============================================================

# Record count validation checks whether
# the number of records is within the expected range.


records = [
    {"id": 1},
    {"id": 2},
    {"id": 3}
]


record_count = len(records)

print(record_count)


# Example expected minimum:

minimum_records = 1


if record_count >= minimum_records:

    print("Record count is valid")

else:

    print("Too few records")


# ============================================================
# 11. Record Count Before and After Processing
# ============================================================

# Record counts can be compared between pipeline stages.


input_count = 1000
output_count = 1000


if input_count == output_count:

    print("Record count matched")

else:

    print("Record count mismatch")


# This can help detect accidental data loss.


# ============================================================
# 12. Datatype Checks
# ============================================================

# Sometimes data arrives with an unexpected datatype.
#
# Example:
#
# Expected:
# salary -> integer
#
# Received:
# salary -> string


salary = 50000


if isinstance(salary, int):

    print("Salary datatype is valid")

else:

    print("Invalid salary datatype")


# ============================================================
# 13. Common Datatype Checks
# ============================================================

value = "Alice"

print(isinstance(value, str))


age = 22

print(isinstance(age, int))


salary = 50000.50

print(isinstance(salary, float))


is_active = True

print(isinstance(is_active, bool))


# isinstance() is commonly used to check
# whether a value has the expected datatype.


# ============================================================
# 14. Business Rule Checks
# ============================================================

# Business rules are conditions that should be true
# according to the requirements of the business.


# Example:
#
# Salary cannot be negative.

salary = 50000


if salary >= 0:

    print("Salary is valid")

else:

    print("Invalid salary")


# ============================================================
# 15. More Business Rule Examples
# ============================================================

# Age should be between 18 and 100.

age = 25

if 18 <= age <= 100:

    print("Age is valid")

else:

    print("Invalid age")


# Quantity should be greater than zero.

quantity = 5

if quantity > 0:

    print("Quantity is valid")

else:

    print("Invalid quantity")


# Email should not be empty.

email = "alice@example.com"

if email:

    print("Email is present")

else:

    print("Email is missing")


# ============================================================
# 16. Combining Multiple Checks
# ============================================================

record = {
    "id": 101,
    "name": "Alice",
    "age": 25,
    "salary": 50000
}


# Check required fields.

required_fields = [
    "id",
    "name",
    "age",
    "salary"
]


for field in required_fields:

    if record.get(field) is None:

        print(
            f"Missing field: {field}"
        )


# Check datatype.

if not isinstance(record["id"], int):

    print("Invalid ID datatype")


if not isinstance(record["name"], str):

    print("Invalid name datatype")


# Check business rule.

if record["age"] < 18:

    print("Invalid age")


if record["salary"] < 0:

    print("Invalid salary")


# ============================================================
# 17. Validation Function
# ============================================================

# Validation logic can be placed inside
# reusable functions.


def validate_record(record):

    if record.get("id") is None:

        return False

    if record.get("name") is None:

        return False

    if not isinstance(record["id"], int):

        return False

    if not isinstance(record["name"], str):

        return False

    return True


record = {
    "id": 101,
    "name": "Alice"
}


if validate_record(record):

    print("Record is valid")

else:

    print("Record is invalid")


# ============================================================
# 18. Validation with Multiple Errors
# ============================================================

# Instead of stopping at the first error,
# we can collect validation errors.


def validate_record(record):

    errors = []

    if record.get("id") is None:

        errors.append("Missing id")

    if record.get("name") is None:

        errors.append("Missing name")

    if "id" in record and not isinstance(
        record["id"],
        int
    ):

        errors.append("id must be an integer")

    if "name" in record and not isinstance(
        record["name"],
        str
    ):

        errors.append("name must be a string")

    return errors


record = {
    "id": "101",
    "name": None
}


errors = validate_record(record)

print(errors)


# ============================================================
# 19. Validation Before Processing
# ============================================================

# A common Data Engineering pattern is:
#
# Extract
#   ↓
# Validate
#   ↓
# Transform
#   ↓
# Load


records = [
    {
        "id": 101,
        "name": "Alice"
    },
    {
        "id": 102,
        "name": "Bob"
    }
]


for record in records:

    if validate_record(record):

        print("Process record")

    else:

        print("Reject record")


# ============================================================
# 20. Validation + Logging
# ============================================================

import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def validate_data(record):

    if record.get("id") is None:

        logging.error(
            "Record has missing ID"
        )

        return False

    if record.get("name") is None:

        logging.error(
            "Record has missing name"
        )

        return False

    logging.info(
        "Record validation successful"
    )

    return True


# ============================================================
# 21. Validation of API Data
# ============================================================

# Data received from an API should not be blindly trusted.
#
# Example:
#
# API
# ↓
# JSON
# ↓
# Python dictionary
# ↓
# Validation
# ↓
# Transformation


api_record = {
    "id": 101,
    "name": "Alice",
    "salary": 50000
}


if "id" not in api_record:

    print("ID column missing")


if "name" not in api_record:

    print("Name column missing")


if not isinstance(
    api_record.get("id"),
    int
):

    print("Invalid ID datatype")


if api_record.get("salary", 0) < 0:

    print("Invalid salary")


# ============================================================
# 22. Validation Checklist
# ============================================================

# Before processing data, ask:
#
# 1. Are all required columns present?
#
# 2. Are there unexpected columns?
#
# 3. Are required values missing?
#
# 4. Are there duplicate records?
#
# 5. Is the record count reasonable?
#
# 6. Are datatypes correct?
#
# 7. Do business rules pass?
#
#
# These are the core checks you should remember.


# ============================================================
# 23. What Happens When Validation Fails?
# ============================================================

# Depending on the pipeline, invalid data can be:
#
# - Rejected
# - Logged
# - Sent to a separate error/quarantine file
# - Corrected
# - Ignored if the field is optional
# - Cause the pipeline to stop
#
#
# The correct action depends on the business requirement.


# ============================================================
# 24. Data Validation in a Real Pipeline
# ============================================================

# Example:

# API
#  ↓
# Extract JSON
#  ↓
# Check schema
#  ↓
# Check nulls
#  ↓
# Check duplicates
#  ↓
# Check datatypes
#  ↓
# Check record count
#  ↓
# Check business rules
#  ↓
# Transform
#  ↓
# Save Parquet
#  ↓
# Load Database


# ============================================================
# 25. Important Difference
# ============================================================

# Schema check
# → Is the structure correct?
#
# Null check
# → Is required data missing?
#
# Duplicate check
# → Are records repeated?
#
# Record-count check
# → Did we receive/process the expected amount of data?
#
# Datatype check
# → Is the value the expected Python/data type?
#
# Business-rule check
# → Does the value make sense according to business rules?


# ============================================================
# 26. Key Takeaways
# ============================================================

# Data validation = Checking data quality before processing.
#
# Schema check
# → Check expected columns/structure.
#
# Null check
# → Check missing required values.
#
# Duplicate check
# → Check repeated records/IDs.
#
# Record count check
# → Check expected number of records.
#
# Datatype check
# → Check expected data types.
#
# Business rule check
# → Check business-specific conditions.
#
# Validation should happen before important
# transformation or loading steps.
#
# Invalid data should be handled according to
# the pipeline/business requirement.


# ============================================================
# ⭐ FRESHER MUST-KNOW CHEAT SHEET
# ============================================================

# Schema
# → Are the expected columns present?
#
# Null
# → Are required values missing?
#
# Duplicate
# → Are records repeated?
#
# Record Count
# → Did we receive the expected number of records?
#
# Datatype
# → Is the value the correct type?
#
# Business Rule
# → Does the value satisfy the business requirement?
#
# Validation
# → Check data BEFORE processing/loading it.