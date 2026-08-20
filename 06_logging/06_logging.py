"""
Python Logging
==============

Logging is used to record information about what a program
is doing while it runs.

In real-world applications and Data Engineering pipelines,
logging is preferred over using print() statements.

Logging helps us:

- Track pipeline execution
- Understand what happened
- Find errors
- Debug problems
- Monitor jobs
- Record warnings
- Keep execution history

Topics covered:

1. What is logging?
2. Why logging is important
3. logging module
4. DEBUG
5. INFO
6. WARNING
7. ERROR
8. CRITICAL
9. Basic log formatting
10. Replacing print()
11. Logging exceptions
12. Practical Data Engineering examples
"""


# ============================================================
# 1. What is Logging?
# ============================================================

# Logging means recording information about
# the execution of a program.

# Example information that can be logged:

# - Program started
# - File found
# - File processed
# - Number of records processed
# - Warning occurred
# - Error occurred
# - Pipeline completed


# ============================================================
# 2. Why Use Logging Instead of print()?
# ============================================================

# print():

print("Pipeline started")


# print() is useful while learning and for simple debugging.

# But in real projects, logging is better because
# it provides different severity levels and timestamps.


# ============================================================
# 3. Import logging
# ============================================================

import logging


# ============================================================
# 4. Basic Logging
# ============================================================

logging.basicConfig(
    level=logging.INFO
)


logging.info("Pipeline started")


# ============================================================
# 5. Logging Levels
# ============================================================

# Python provides different logging levels:

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL


# The levels represent increasing severity.


# ============================================================
# 6. DEBUG
# ============================================================

# DEBUG is used for detailed information
# useful while debugging a program.

logging.debug("Checking input file path")


# DEBUG messages normally won't appear when
# the logging level is INFO.


# ============================================================
# 7. INFO
# ============================================================

# INFO represents normal program execution.

logging.info("File processing started")

logging.info("100 records processed")


# ============================================================
# 8. WARNING
# ============================================================

# WARNING indicates something unexpected
# but the program can continue.

logging.warning(
    "Input file contains missing values"
)


# ============================================================
# 9. ERROR
# ============================================================

# ERROR indicates that something failed.

logging.error(
    "Unable to process input file"
)


# ============================================================
# 10. CRITICAL
# ============================================================

# CRITICAL represents a very serious problem.

logging.critical(
    "Database connection completely failed"
)


# ============================================================
# 11. Logging Levels Order
# ============================================================

# From lowest to highest severity:

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL


# If logging level is INFO:

# INFO
# WARNING
# ERROR
# CRITICAL

# are displayed.

# DEBUG is ignored.


# ============================================================
# 12. Basic Log Formatting
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Example:

logging.info("Data pipeline started")


# The output can look similar to:

# 2026-08-20 22:00:00,000 - INFO - Data pipeline started


# ============================================================
# 13. Meaning of Formatting Fields
# ============================================================

# %(asctime)s
# Time when the log was created

# %(levelname)s
# Logging level

# %(message)s
# Actual log message


# ============================================================
# 14. Logging Variables
# ============================================================

file_name = "sales.csv"

record_count = 1000


logging.info(
    f"Processing file: {file_name}"
)


logging.info(
    f"Records processed: {record_count}"
)


# ============================================================
# 15. Logging Different Levels
# ============================================================

logging.debug("Starting validation")

logging.info("Reading CSV file")

logging.warning("Some records contain null values")

logging.error("Failed to process one record")

logging.critical("Pipeline cannot continue")


# ============================================================
# 16. Replacing print()
# ============================================================

# Instead of:

print("Reading file")


# Prefer:

logging.info("Reading file")


# Instead of:

print("File not found")


# Prefer:

logging.error("File not found")


# Instead of:

print("Missing values found")


# Prefer:

logging.warning("Missing values found")


# ============================================================
# 17. Logging Exceptions
# ============================================================

try:

    result = 10 / 0

except ZeroDivisionError:

    logging.error(
        "Division by zero occurred"
    )


# ============================================================
# 18. logging.exception()
# ============================================================

# logging.exception() is useful inside
# an except block.

try:

    result = 10 / 0

except ZeroDivisionError:

    logging.exception(
        "An error occurred while calculating"
    )


# logging.exception() automatically includes
# exception information and traceback.


# ============================================================
# 19. Logging File Processing
# ============================================================

from pathlib import Path


file_path = Path(
    "data/raw/sales.csv"
)


if file_path.exists():

    logging.info(
        f"Input file found: {file_path}"
    )

else:

    logging.error(
        f"Input file not found: {file_path}"
    )


# ============================================================
# 20. Logging Record Counts
# ============================================================

records = [
    {"id": 1},
    {"id": 2},
    {"id": 3}
]


logging.info(
    f"Records loaded: {len(records)}"
)


# ============================================================
# 21. Logging Warnings
# ============================================================

null_count = 5


if null_count > 0:

    logging.warning(
        f"Found {null_count} null values"
    )


# ============================================================
# 22. Logging Errors
# ============================================================

try:

    number = int("abc")

except ValueError:

    logging.error(
        "Invalid number received"
    )


# ============================================================
# 23. Logging with Error Details
# ============================================================

try:

    number = int("abc")

except ValueError as error:

    logging.error(
        f"Invalid value: {error}"
    )


# ============================================================
# 24. Logging a Simple ETL Pipeline
# ============================================================

logging.info("ETL pipeline started")


logging.info("Checking input file")


logging.info("Reading source data")


logging.info("Validating records")


logging.info("Transforming data")


logging.info("Saving processed data")


logging.info("ETL pipeline completed")


# ============================================================
# 25. Logging ETL Errors
# ============================================================

try:

    file_path = Path(
        "data/raw/sales.csv"
    )

    if not file_path.exists():

        raise FileNotFoundError(
            "Sales file not found"
        )

except FileNotFoundError:

    logging.exception(
        "ETL pipeline failed"
    )


# ============================================================
# 26. Logging Data Validation
# ============================================================

record_count = 100

expected_count = 100


if record_count == expected_count:

    logging.info(
        "Record count validation passed"
    )

else:

    logging.warning(
        "Record count does not match expectation"
    )


# ============================================================
# 27. Logging Pipeline Stages
# ============================================================

def extract():

    logging.info(
        "Extract stage started"
    )

    logging.info(
        "Extract stage completed"
    )


def transform():

    logging.info(
        "Transform stage started"
    )

    logging.info(
        "Transform stage completed"
    )


def load():

    logging.info(
        "Load stage started"
    )

    logging.info(
        "Load stage completed"
    )


extract()

transform()

load()


# ============================================================
# 28. Logging with Functions
# ============================================================

def process_file(file_name):

    logging.info(
        f"Processing started: {file_name}"
    )

    # Processing logic

    logging.info(
        f"Processing completed: {file_name}"
    )


process_file("sales.csv")


# ============================================================
# 29. Logging File Errors
# ============================================================

def read_file(file_name):

    try:

        with open(
            file_name,
            "r"
        ) as file:

            data = file.read()

            logging.info(
                f"Successfully read {file_name}"
            )

            return data

    except FileNotFoundError:

        logging.error(
            f"File not found: {file_name}"
        )

        return None


read_file("sales.csv")


# ============================================================
# 30. Logging JSON Processing
# ============================================================

import json


def read_json(file_name):

    try:

        with open(
            file_name,
            "r"
        ) as file:

            data = json.load(file)

            logging.info(
                f"JSON loaded successfully: {file_name}"
            )

            return data

    except FileNotFoundError:

        logging.error(
            f"JSON file not found: {file_name}"
        )

    except json.JSONDecodeError:

        logging.error(
            f"Invalid JSON format: {file_name}"
        )

    return None


# ============================================================
# 31. Logging API-Style Processing
# ============================================================

# Later, when working with APIs:

status_code = 200


if status_code == 200:

    logging.info(
        "API request successful"
    )

elif status_code == 404:

    logging.error(
        "API resource not found"
    )

else:

    logging.warning(
        f"Unexpected status code: {status_code}"
    )


# ============================================================
# 32. Logging Important Pipeline Information
# ============================================================

# Good logs should tell us:

# WHAT happened
# WHEN it happened
# HOW serious it was


logging.info(
    "Sales pipeline started"
)


logging.info(
    "Loaded 10,000 records"
)


logging.warning(
    "500 records contain null values"
)


logging.error(
    "Failed to write output file"
)


# ============================================================
# 33. What Should You Log?
# ============================================================

# Useful things to log:

# - Pipeline start/end
# - File names
# - Record counts
# - Validation results
# - Processing stages
# - API status
# - Errors
# - Important warnings


# ============================================================
# 34. What Should You NOT Log?
# ============================================================

# Avoid logging sensitive information such as:

# - Passwords
# - API keys
# - Access tokens
# - Database passwords
# - Personal sensitive data


# Example of what NOT to do:

# logging.info(f"API key: {api_key}")


# ============================================================
# 35. Logging Level Configuration
# ============================================================

logging.basicConfig(
    level=logging.WARNING
)


# With WARNING level, these are shown:

# WARNING
# ERROR
# CRITICAL


# INFO and DEBUG are ignored.


# ============================================================
# 36. Basic Logging Configuration
# ============================================================

# A common basic configuration is:

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )


# ============================================================
# 37. print() vs logging
# ============================================================

# print():

print("Processing started")


# logging:

logging.info("Processing started")


# Logging is preferred for production applications
# and data pipelines because it provides levels,
# timestamps and better control.


# ============================================================
# 38. Data Engineering Example
# ============================================================

def run_pipeline():

    logging.info(
        "Pipeline started"
    )

    try:

        logging.info(
            "Checking source file"
        )

        source = Path(
            "data/raw/sales.csv"
        )

        if not source.exists():

            raise FileNotFoundError(
                "Source file does not exist"
            )

        logging.info(
            "Source file found"
        )

        logging.info(
            "Reading source data"
        )

        # Transformation would happen here.

        logging.info(
            "Transformation completed"
        )

        logging.info(
            "Loading processed data"
        )

        logging.info(
            "Pipeline completed successfully"
        )

    except FileNotFoundError:

        logging.exception(
            "Pipeline failed because source file was missing"
        )


# run_pipeline()


# ============================================================
# 39. Key Takeaways
# ============================================================

# 1. Logging records program execution.
#
# 2. logging is better than print()
#    for production pipelines.
#
# 3. DEBUG is used for detailed debugging information.
#
# 4. INFO is used for normal execution information.
#
# 5. WARNING indicates a potential problem.
#
# 6. ERROR indicates a failure.
#
# 7. CRITICAL indicates a serious failure.
#
# 8. logging.exception() is useful inside except blocks.
#
# 9. Log important pipeline stages.
#
# 10. Don't log passwords, API keys or secrets.
#
# 11. Basic formatting commonly includes:
#
#     timestamp
#     log level
#     message


# ============================================================
# 40. Quick Revision Table
# ============================================================

# Level       Purpose
#
# DEBUG       Detailed debugging information
#
# INFO        Normal program execution
#
# WARNING     Something unexpected happened
#
# ERROR       Operation failed
#
# CRITICAL    Serious failure


