"""
Python Date & Time
==================

Python provides the datetime module for working with:

- Dates
- Times
- Date and time together
- Date arithmetic
- Parsing date strings
- Formatting dates
- Comparing dates
- Time differences

Date and time handling is very important in Data Engineering.

Common Data Engineering use cases:

- ETL execution dates
- Pipeline timestamps
- File creation dates
- API timestamps
- Data partitioning
- Filtering data by date
- Finding records between dates
- Calculating processing time
- Scheduling jobs
"""


# ============================================================
# 1. Importing datetime
# ============================================================

import datetime


# The datetime module is part of Python's standard library.

print(datetime.date.today())


# ============================================================
# 2. Using Specific Classes from datetime
# ============================================================

from datetime import date, time, datetime, timedelta


# Instead of:

datetime.date.today()


# We can directly use:

print(date.today())


# ============================================================
# 3. date
# ============================================================

# date represents a calendar date.

today = date.today()

print(today)


# Example output:

# 2026-08-18


# A date contains:

# year
# month
# day


# ============================================================
# 4. Accessing Date Components
# ============================================================

today = date.today()

print(today.year)

print(today.month)

print(today.day)


# ============================================================
# 5. Creating a Date
# ============================================================

from datetime import date


birthday = date(2003, 11, 19)

print(birthday)


# Syntax:

# date(year, month, day)


# ============================================================
# 6. Creating Different Dates
# ============================================================

date1 = date(2025, 1, 1)

date2 = date(2026, 12, 31)

print(date1)

print(date2)


# ============================================================
# 7. datetime
# ============================================================

# datetime represents both date and time.

from datetime import datetime


current_datetime = datetime.now()

print(current_datetime)


# Example:

# 2026-08-18 10:30:45.123456


# ============================================================
# 8. Accessing datetime Components
# ============================================================

current_datetime = datetime.now()

print(current_datetime.year)

print(current_datetime.month)

print(current_datetime.day)

print(current_datetime.hour)

print(current_datetime.minute)

print(current_datetime.second)

print(current_datetime.microsecond)


# ============================================================
# 9. datetime.today()
# ============================================================

current_datetime = datetime.today()

print(current_datetime)


# datetime.today() returns the current local date and time.


# ============================================================
# 10. datetime.now()
# ============================================================

current_datetime = datetime.now()

print(current_datetime)


# datetime.now() also returns the current local date and time.


# In basic Python usage, both can be used to get
# the current local datetime.


# ============================================================
# 11. Creating a datetime
# ============================================================

from datetime import datetime


dt = datetime(
    2026,
    8,
    18,
    10,
    30,
    45
)

print(dt)


# Syntax:

# datetime(
#     year,
#     month,
#     day,
#     hour,
#     minute,
#     second
# )


# ============================================================
# 12. time
# ============================================================

from datetime import time


current_time = time(
    10,
    30,
    45
)

print(current_time)


# time represents only time-related information.


# ============================================================
# 13. Accessing Time Components
# ============================================================

t = time(
    10,
    30,
    45
)

print(t.hour)

print(t.minute)

print(t.second)

print(t.microsecond)


# ============================================================
# 14. Creating a Time with Microseconds
# ============================================================

t = time(
    10,
    30,
    45,
    500000
)

print(t)


# ============================================================
# 15. date vs datetime vs time
# ============================================================

# date:
# Stores only date.

d = date(
    2026,
    8,
    18
)


# time:
# Stores only time.

t = time(
    10,
    30,
    45
)


# datetime:
# Stores date + time.

dt = datetime(
    2026,
    8,
    18,
    10,
    30,
    45
)


print(d)

print(t)

print(dt)


# ============================================================
# 16. Formatting Dates
# ============================================================

# Formatting means converting a date/datetime object
# into a string in a specific format.

today = date.today()

formatted = today.strftime("%d-%m-%Y")

print(formatted)


# Example:

# 18-08-2026


# ============================================================
# 17. Common strftime Codes
# ============================================================

# %Y -> Four-digit year
# %y -> Two-digit year
# %m -> Month as number
# %d -> Day
# %H -> Hour (24-hour)
# %I -> Hour (12-hour)
# %M -> Minute
# %S -> Second
# %p -> AM/PM
# %A -> Full weekday name
# %a -> Short weekday name
# %B -> Full month name
# %b -> Short month name


# ============================================================
# 18. Formatting Date in Different Ways
# ============================================================

today = date.today()


print(today.strftime("%Y-%m-%d"))

print(today.strftime("%d-%m-%Y"))

print(today.strftime("%d/%m/%Y"))

print(today.strftime("%B %d, %Y"))

print(today.strftime("%A, %d %B %Y"))


# Possible output:

# 2026-08-18
# 18-08-2026
# 18/08/2026
# August 18, 2026
# Tuesday, 18 August 2026


# ============================================================
# 19. Formatting datetime
# ============================================================

now = datetime.now()


formatted = now.strftime(
    "%Y-%m-%d %H:%M:%S"
)

print(formatted)


# Example:

# 2026-08-18 10:30:45


# This format is very common for:
#
# - Logs
# - Databases
# - ETL timestamps
# - Data pipelines


# ============================================================
# 20. 12-Hour vs 24-Hour Format
# ============================================================

now = datetime.now()


print(
    now.strftime("%H:%M:%S")
)


# 24-hour format


print(
    now.strftime("%I:%M:%S %p")
)


# 12-hour format


# ============================================================
# 21. Parsing Dates
# ============================================================

# Parsing means converting a string into a
# date/datetime object.

date_string = "18-08-2026"


parsed_date = datetime.strptime(
    date_string,
    "%d-%m-%Y"
)

print(parsed_date)


# ============================================================
# 22. strptime()
# ============================================================

# strptime means:
#
# string -> datetime


date_string = "2026-08-18"


parsed_date = datetime.strptime(
    date_string,
    "%Y-%m-%d"
)

print(parsed_date)


# ============================================================
# 23. Parsing Different Formats
# ============================================================

date_string = "18/08/2026"


parsed_date = datetime.strptime(
    date_string,
    "%d/%m/%Y"
)

print(parsed_date)


date_string = "August 18, 2026"


parsed_date = datetime.strptime(
    date_string,
    "%B %d, %Y"
)

print(parsed_date)


# ============================================================
# 24. Parsing Date and Time
# ============================================================

date_string = "2026-08-18 10:30:45"


parsed_datetime = datetime.strptime(
    date_string,
    "%Y-%m-%d %H:%M:%S"
)

print(parsed_datetime)


# ============================================================
# 25. strptime vs strftime
# ============================================================

# strptime:
#
# String -> datetime


date_string = "2026-08-18"

dt = datetime.strptime(
    date_string,
    "%Y-%m-%d"
)


# strftime:
#
# datetime -> String


formatted = dt.strftime(
    "%d-%m-%Y"
)

print(formatted)


# Remember:

# strptime = parse
# strftime = format


# ============================================================
# 26. Date Arithmetic
# ============================================================

# Date arithmetic means performing calculations
# with dates.

from datetime import timedelta


today = date.today()

tomorrow = today + timedelta(days=1)

print(today)

print(tomorrow)


# ============================================================
# 27. Adding Days
# ============================================================

today = date.today()


future_date = today + timedelta(days=7)

print(future_date)


# Add 7 days.


# ============================================================
# 28. Subtracting Days
# ============================================================

today = date.today()


previous_date = today - timedelta(days=7)

print(previous_date)


# Subtract 7 days.


# ============================================================
# 29. Adding Weeks
# ============================================================

today = date.today()


future_date = today + timedelta(weeks=2)

print(future_date)


# ============================================================
# 30. Adding Hours
# ============================================================

now = datetime.now()


future_time = now + timedelta(hours=5)

print(future_time)


# ============================================================
# 31. Adding Minutes
# ============================================================

now = datetime.now()


future_time = now + timedelta(minutes=30)

print(future_time)


# ============================================================
# 32. Adding Seconds
# ============================================================

now = datetime.now()


future_time = now + timedelta(seconds=60)

print(future_time)


# ============================================================
# 33. Combining timedelta Values
# ============================================================

future = datetime.now() + timedelta(
    days=2,
    hours=5,
    minutes=30
)

print(future)


# ============================================================
# 34. Difference Between Two Dates
# ============================================================

start_date = date(
    2026,
    8,
    1
)

end_date = date(
    2026,
    8,
    18
)


difference = end_date - start_date

print(difference)


# Output:

# 17 days, 0:00:00


# ============================================================
# 35. Getting Number of Days
# ============================================================

difference = end_date - start_date

print(difference.days)


# ============================================================
# 36. Difference Between Two datetimes
# ============================================================

start = datetime(
    2026,
    8,
    18,
    10,
    0,
    0
)

end = datetime(
    2026,
    8,
    18,
    15,
    30,
    0
)


difference = end - start

print(difference)


# ============================================================
# 37. Getting Total Seconds
# ============================================================

difference = end - start

print(difference.total_seconds())


# total_seconds() converts the complete timedelta
# into seconds.


# ============================================================
# 38. Comparing Dates
# ============================================================

date1 = date(
    2026,
    8,
    18
)

date2 = date(
    2026,
    8,
    20
)


print(date1 < date2)

print(date1 > date2)

print(date1 == date2)


# Dates can be compared using:

# <
# >
# <=
# >=
# ==
# !=


# ============================================================
# 39. Checking if a Date is in the Past
# ============================================================

today = date.today()

some_date = date(
    2025,
    1,
    1
)


if some_date < today:

    print("Date is in the past")


# ============================================================
# 40. Checking if a Date is in the Future
# ============================================================

today = date.today()

some_date = date(
    2030,
    1,
    1
)


if some_date > today:

    print("Date is in the future")


# ============================================================
# 41. Converting Date to String
# ============================================================

today = date.today()

date_string = str(today)

print(date_string)

print(type(date_string))


# Output type:

# <class 'str'>


# ============================================================
# 42. Converting String to Date
# ============================================================

date_string = "2026-08-18"


dt = datetime.strptime(
    date_string,
    "%Y-%m-%d"
)


date_object = dt.date()

print(date_object)

print(type(date_object))


# ============================================================
# 43. Extracting Date from datetime
# ============================================================

now = datetime.now()


date_part = now.date()

print(date_part)


# ============================================================
# 44. Extracting Time from datetime
# ============================================================

now = datetime.now()


time_part = now.time()

print(time_part)


# ============================================================
# 45. Combining Date and Time
# ============================================================

from datetime import date, time, datetime


d = date(
    2026,
    8,
    18
)

t = time(
    10,
    30,
    0
)


combined = datetime.combine(
    d,
    t
)

print(combined)


# ============================================================
# 46. Getting Weekday
# ============================================================

today = date.today()


print(today.weekday())


# weekday() returns:

# Monday    -> 0
# Tuesday   -> 1
# Wednesday -> 2
# Thursday  -> 3
# Friday    -> 4
# Saturday  -> 5
# Sunday    -> 6


# ============================================================
# 47. Getting Weekday Name
# ============================================================

today = date.today()


print(today.strftime("%A"))


# Example:

# Tuesday


# ============================================================
# 48. Getting Month Name
# ============================================================

today = date.today()


print(today.strftime("%B"))


# Example:

# August


# ============================================================
# 49. Getting ISO Format
# ============================================================

today = date.today()


print(today.isoformat())


# Example:

# 2026-08-18


# ISO format is commonly used in:
#
# - APIs
# - Databases
# - Data pipelines
# - Logs
# - Data exchange


# ============================================================
# 50. Parsing ISO Date
# ============================================================

date_string = "2026-08-18"


parsed_date = date.fromisoformat(
    date_string
)

print(parsed_date)


# ============================================================
# 51. Parsing ISO datetime
# ============================================================

datetime_string = "2026-08-18T10:30:45"


parsed_datetime = datetime.fromisoformat(
    datetime_string
)

print(parsed_datetime)


# ============================================================
# 52. Timestamp
# ============================================================

now = datetime.now()


timestamp = now.timestamp()

print(timestamp)


# A timestamp represents a point in time as
# seconds relative to the Unix epoch.


# ============================================================
# 53. Converting Timestamp to datetime
# ============================================================

timestamp = 0


dt = datetime.fromtimestamp(
    timestamp
)

print(dt)


# ============================================================
# 54. Practical Example - File Processing Date
# ============================================================

today = date.today()


file_name = (
    "sales_"
    + today.strftime("%Y-%m-%d")
    + ".csv"
)


print(file_name)


# Example:

# sales_2026-08-18.csv


# This pattern can be useful when generating
# date-based files.


# ============================================================
# 55. Practical Example - ETL Execution Timestamp
# ============================================================

execution_time = datetime.now()


formatted_time = execution_time.strftime(
    "%Y-%m-%d %H:%M:%S"
)


print("ETL started at:", formatted_time)


# ============================================================
# 56. Practical Example - Data Partition Date
# ============================================================

processing_date = date.today()


year = processing_date.year

month = processing_date.month

day = processing_date.day


print("Year:", year)

print("Month:", month)

print("Day:", day)


# Data warehouses and data lakes often partition
# data using date information.


# ============================================================
# 57. Practical Example - Filter Recent Records
# ============================================================

today = date.today()


record_date = date(
    2026,
    8,
    15
)


difference = today - record_date


if difference.days <= 7:

    print("Record is recent")


# ============================================================
# 58. Practical Example - Check Data Freshness
# ============================================================

last_updated = datetime(
    2026,
    8,
    18,
    8,
    0,
    0
)

current_time = datetime.now()


age = current_time - last_updated


if age.total_seconds() > 3600:

    print("Warning: Data may be stale")

else:

    print("Data is recent")


# This type of logic can be useful for
# checking whether a data source has been updated.


# ============================================================
# 59. Practical Example - Calculate Pipeline Duration
# ============================================================

start_time = datetime.now()


# Some processing would happen here.


end_time = datetime.now()


duration = end_time - start_time


print("Pipeline duration:", duration)


# ============================================================
# 60. Practical Example - Calculate Days Since Registration
# ============================================================

registration_date = date(
    2025,
    8,
    18
)

today = date.today()


days_since_registration = (
    today - registration_date
).days


print(
    "Days since registration:",
    days_since_registration
)


# ============================================================
# 61. Practical Example - Calculate Future Date
# ============================================================

start_date = date.today()


processing_date = (
    start_date + timedelta(days=7)
)


print(
    "Processing date:",
    processing_date
)


# ============================================================
# 62. Practical Example - Date Validation
# ============================================================

def is_date_in_past(date_value):

    return date_value < date.today()


print(
    is_date_in_past(
        date(2025, 1, 1)
    )
)


# ============================================================
# 63. Reusable Date Formatting Function
# ============================================================

def format_date(date_value):

    return date_value.strftime(
        "%Y-%m-%d"
    )


today = date.today()


print(format_date(today))


# ============================================================
# 64. Reusable Date Parsing Function
# ============================================================

def parse_date(date_string):

    return datetime.strptime(
        date_string,
        "%Y-%m-%d"
    ).date()


result = parse_date(
    "2026-08-18"
)


print(result)


# ============================================================
# 65. Handling Invalid Date Strings
# ============================================================

# Invalid date strings can raise ValueError.

date_string = "invalid-date"


# This would raise ValueError:

# parsed_date = datetime.strptime(
#     date_string,
#     "%Y-%m-%d"
# )


# Error handling will be covered in the
# Error Handling section of this roadmap.


# ============================================================
# 66. Important Date Format Codes
# ============================================================

# %Y
# Four-digit year
#
# %y
# Two-digit year
#
# %m
# Month number
#
# %d
# Day of month
#
# %H
# Hour in 24-hour format
#
# %I
# Hour in 12-hour format
#
# %M
# Minute
#
# %S
# Second
#
# %p
# AM / PM
#
# %A
# Full weekday name
#
# %a
# Short weekday name
#
# %B
# Full month name
#
# %b
# Short month name


# ============================================================
# 67. Common Date Formats
# ============================================================

# YYYY-MM-DD

print(
    date.today().strftime(
        "%Y-%m-%d"
    )
)


# DD-MM-YYYY

print(
    date.today().strftime(
        "%d-%m-%Y"
    )
)


# DD/MM/YYYY

print(
    date.today().strftime(
        "%d/%m/%Y"
    )
)


# ============================================================
# 68. Important Concept:
#    String vs Date Object
# ============================================================

date_string = "2026-08-18"

print(type(date_string))


date_object = datetime.strptime(
    date_string,
    "%Y-%m-%d"
).date()


print(type(date_object))


# String:

# "2026-08-18"


# Date object:

# date(2026, 8, 18)


# A string is text.
#
# A date object can be used for:
#
# - Date arithmetic
# - Comparisons
# - Extracting components
# - Formatting


# ============================================================
# 69. Important Concept:
#    Parsing vs Formatting
# ============================================================

# Parsing:

# String
#   ↓
# datetime object

date_string = "18-08-2026"

dt = datetime.strptime(
    date_string,
    "%d-%m-%Y"
)


# Formatting:

# datetime object
#   ↓
# String

formatted = dt.strftime(
    "%Y-%m-%d"
)

print(formatted)


# Remember:

# strptime = String → datetime
#
# strftime = datetime → String


# ============================================================
# 70. Important Concept:
#    timedelta
# ============================================================

# timedelta represents a duration or difference
# between dates/times.


from datetime import timedelta


one_day = timedelta(days=1)

one_week = timedelta(weeks=1)

two_hours = timedelta(hours=2)


print(one_day)

print(one_week)

print(two_hours)


# ============================================================
# 71. timedelta with datetime
# ============================================================

now = datetime.now()


tomorrow = now + timedelta(days=1)

yesterday = now - timedelta(days=1)


print("Now:", now)

print("Tomorrow:", tomorrow)

print("Yesterday:", yesterday)


# ============================================================
# 72. Date Arithmetic Summary
# ============================================================

today = date.today()


# Add:

future = today + timedelta(days=10)


# Subtract:

past = today - timedelta(days=10)


# Difference:

difference = future - past


print(future)

print(past)

print(difference.days)


# ============================================================
# 73. Date Handling in Data Engineering
# ============================================================

# Date/time operations are commonly used for:
#
# 1. ETL execution timestamps
# 2. Incremental data loading
# 3. Data partitioning
# 4. API timestamps
# 5. File naming
# 6. Data freshness checks
# 7. Filtering recent records
# 8. Pipeline duration
# 9. Logging
# 10. Scheduling


# Example:

def get_processing_date():

    return date.today()


processing_date = get_processing_date()


print(
    "Processing date:",
    processing_date
)


# ============================================================
# 74. Incremental Data Loading Concept
# ============================================================

# Suppose a pipeline processed data up to:

last_processed_date = date(
    2026,
    8,
    17
)


# Today:

today = date.today()


# We may want to process only data after
# the last processed date.


print(
    "Last processed:",
    last_processed_date
)

print(
    "Current date:",
    today
)


# In a real pipeline, this date could be stored
# in a database or metadata table.


# ============================================================
# 75. Date-Based File Naming
# ============================================================

processing_date = date.today()


file_name = (
    f"sales_{processing_date.strftime('%Y%m%d')}.csv"
)


print(file_name)


# Example:

# sales_20260818.csv


# ============================================================
# 76. Date-Based Folder Structure
# ============================================================

processing_date = date.today()


folder_path = (
    f"year={processing_date.year}/"
    f"month={processing_date.month:02d}/"
    f"day={processing_date.day:02d}"
)


print(folder_path)


# Example:

# year=2026/month=08/day=18


# This type of partitioning is commonly used
# in data lake / warehouse workflows.


# ============================================================
# 77. Basic Awareness: Time Zones
# ============================================================

# A datetime without timezone information is called
# a naive datetime.

now = datetime.now()

print(now)


# For distributed systems and Data Engineering,
# timezone-aware datetimes are often preferred.


# ============================================================
# 78. timezone-aware datetime - Basic
# ============================================================

from datetime import datetime, timezone


utc_now = datetime.now(
    timezone.utc
)


print(utc_now)


# UTC is commonly used in:
#
# - Distributed systems
# - APIs
# - Cloud platforms
# - Data pipelines
# - Logs


# ============================================================
# 79. Naive vs Aware datetime
# ============================================================

# Naive datetime:
# Does not contain timezone information.

naive = datetime.now()


# Aware datetime:
# Contains timezone information.

aware = datetime.now(
    timezone.utc
)


print(naive)

print(aware)


# For now, understand the concept.
# Detailed timezone handling can be learned later.


# ============================================================
# 80. Important Common Mistakes
# ============================================================

# Mistake 1:
# Treating a date string like a date object.

date_string = "2026-08-18"

# This is a string, not a date object.


# Correct:

date_object = datetime.strptime(
    date_string,
    "%Y-%m-%d"
).date()


# ============================================================

# Mistake 2:
# Using the wrong format while parsing.

date_string = "18-08-2026"


# Correct:

dt = datetime.strptime(
    date_string,
    "%d-%m-%Y"
)


# The format must match the string.


# ============================================================

# Mistake 3:
# Confusing strptime and strftime.

# strptime:
# String → datetime

# strftime:
# datetime → String


# ============================================================

# Mistake 4:
# Forgetting that months start from 1.

date_value = date(
    2026,
    8,
    18
)

# August is month 8.


# ============================================================
# 81. Key Takeaways
# ============================================================

# 1. datetime is Python's main module for date/time handling.
#
# 2. date represents a date.
#
# 3. time represents a time.
#
# 4. datetime represents date + time.
#
# 5. date.today() returns today's date.
#
# 6. datetime.now() returns the current local datetime.
#
# 7. strptime() converts a string into a datetime object.
#
# 8. strftime() converts a datetime object into a string.
#
# 9. timedelta is used for date/time arithmetic.
#
# 10. Dates can be compared using:
#     <, >, <=, >=, ==, !=
#
# 11. Date differences produce a timedelta object.
#
# 12. isoformat() produces an ISO-style date representation.
#
# 13. Date objects are different from date strings.
#
# 14. UTC is commonly used in distributed systems.
#
# 15. Date/time handling is extremely important in
#     Data Engineering.


# ============================================================
# 82. MOST IMPORTANT FUNCTIONS TO REMEMBER
# ============================================================

# date.today()

today = date.today()


# datetime.now()

now = datetime.now()


# datetime.strptime()

dt = datetime.strptime(
    "2026-08-18",
    "%Y-%m-%d"
)


# datetime.strftime()

formatted = dt.strftime(
    "%d-%m-%Y"
)


# timedelta()

tomorrow = today + timedelta(
    days=1
)


# ============================================================
# 83. Quick Revision Table
# ============================================================

# Operation                  Function / Method
#
# Today's date               date.today()
#
# Current datetime           datetime.now()
#
# Create date                date(...)
#
# Create datetime            datetime(...)
#
# Parse string               strptime()
#
# Format datetime            strftime()
#
# Add/subtract time          timedelta()
#
# Convert to ISO             isoformat()
#
# Parse ISO date             date.fromisoformat()
#
# Parse ISO datetime         datetime.fromisoformat()
#
# Get date from datetime     .date()
#
# Get time from datetime     .time()
#
# Get year                   .year
#
# Get month                  .month
#
# Get day                    .day
#
# Get weekday                .weekday()


