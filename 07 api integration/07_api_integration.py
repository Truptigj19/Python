"""
Python API Integration
======================

An API (Application Programming Interface) allows two
software systems to communicate with each other.

In Data Engineering, APIs are commonly used as a source
of data in the Extract stage of an ETL/ELT pipeline.

Typical workflow:

API
 ↓
Send HTTP request
 ↓
Receive response
 ↓
Check status code
 ↓
Read JSON data
 ↓
Validate data
 ↓
Transform data
 ↓
Store data

Topics covered:

1. What is an API?
2. HTTP basics
3. GET request
4. POST request
5. Query parameters
6. Headers
7. JSON response
8. Status codes
9. raise_for_status()
10. Timeout
11. API authentication
12. Pagination
13. Error handling
14. Practical Data Engineering example
"""

# ============================================================
# 1. What is an API?
# ============================================================

# API stands for:
#
# Application Programming Interface
#
# An API allows applications to communicate with each other.
#
# Example:
#
# Python program
#      ↓
#      API
#      ↓
# Server / Database / Application
#      ↓
# JSON response
#
#
# APIs are commonly used to retrieve data from:
#
# - Websites
# - Applications
# - Databases
# - Cloud services
# - Payment systems
# - Weather services
# - Business applications


# ============================================================
# 2. HTTP
# ============================================================

# HTTP stands for:
#
# HyperText Transfer Protocol
#
# It is commonly used for communication between
# clients and servers.
#
# Python application = Client
# API server = Server
#
#
# Client:
# "Give me this data."
#
# Server:
# "Here is the requested data."


# ============================================================
# 3. Common HTTP Methods
# ============================================================

# GET
# Retrieve data.
#
# POST
# Send/create data.
#
# PUT
# Update an entire resource.
#
# PATCH
# Partially update a resource.
#
# DELETE
# Delete a resource.


# For your current learning, focus mainly on:
#
# GET
# POST


# ============================================================
# 4. requests Library
# ============================================================

# Python commonly uses the requests library
# for making HTTP requests.

import requests


# If requests is not installed:

# pip install requests


# ============================================================
# 5. GET Request
# ============================================================

# GET is used to retrieve data.

response = requests.get(
    "https://example.com"
)


print(response)


# The response object contains information
# returned by the server.


# ============================================================
# 6. Response Status Code
# ============================================================

response = requests.get(
    "https://example.com"
)


print(response.status_code)


# Example:

# 200


# 200 means the request was successful.


# ============================================================
# 7. Common HTTP Status Codes
# ============================================================

# 200
# OK
#
# 201
# Created
#
# 204
# No Content
#
# 400
# Bad Request
#
# 401
# Unauthorized
#
# 403
# Forbidden
#
# 404
# Not Found
#
# 429
# Too Many Requests
#
# 500
# Internal Server Error
#
# 502
# Bad Gateway
#
# 503
# Service Unavailable


# ============================================================
# 8. Reading Response Text
# ============================================================

response = requests.get(
    "https://example.com"
)


print(response.text)


# text returns the response body as a string.


# ============================================================
# 9. JSON Response
# ============================================================

# APIs commonly return JSON.

response = requests.get(
    "https://example.com"
)


# If the API returns JSON:

# data = response.json()

# print(data)


# response.json()
# converts the JSON response into
# a Python object such as a dictionary or list.


# ============================================================
# 10. JSON Response Example
# ============================================================

# Suppose an API returns:
#
# {
#     "id": 101,
#     "name": "Alice",
#     "role": "Data Engineer"
# }
#
#
# Python can access it like:

# data = response.json()

# print(data["name"])


# ============================================================
# 11. Checking Status Code
# ============================================================

response = requests.get(
    "https://example.com"
)


if response.status_code == 200:

    print("Request successful")

else:

    print("Request failed")


# ============================================================
# 12. raise_for_status()
# ============================================================

# requests provides raise_for_status()
# to automatically raise an exception
# for unsuccessful HTTP responses.

response = requests.get(
    "https://example.com"
)


response.raise_for_status()


# If the response indicates an HTTP error,
# an exception is raised.


# ============================================================
# 13. Why Use raise_for_status()?
# ============================================================

# Instead of manually checking every status:

response = requests.get(
    "https://example.com"
)

if response.status_code != 200:

    print("Request failed")


# We can use:

response = requests.get(
    "https://example.com"
)

response.raise_for_status()


# This is cleaner and commonly used
# in API integration code.


# ============================================================
# 14. GET with Timeout
# ============================================================

# A timeout prevents a request from waiting
# indefinitely.

response = requests.get(
    "https://example.com",
    timeout=10
)


# timeout=10 means:
#
# Wait up to approximately 10 seconds
# according to the request's timeout behavior.


# Always consider using a timeout
# in production API requests.


# ============================================================
# 15. API Error Handling
# ============================================================

try:

    response = requests.get(
        "https://example.com",
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    print(data)

except requests.exceptions.Timeout:

    print("API request timed out")

except requests.exceptions.HTTPError:

    print("HTTP error occurred")

except requests.exceptions.RequestException:

    print("Request failed")


# RequestException is a base exception
# for many requests-related errors.


# ============================================================
# 16. Query Parameters
# ============================================================

# Query parameters are values sent as part
# of the URL request.
#
# Example:
#
# ?page=1&limit=10
#
#
# Instead of manually creating the URL,
# requests allows params=.


params = {
    "page": 1,
    "limit": 10
}


response = requests.get(
    "https://example.com/api/data",
    params=params
)


# requests builds the query string for you.


# ============================================================
# 17. Multiple Query Parameters
# ============================================================

params = {
    "country": "India",
    "city": "Pune",
    "limit": 100
}


response = requests.get(
    "https://example.com/api/users",
    params=params
)


# Conceptually the request becomes:
#
# /api/users?country=India&city=Pune&limit=100


# ============================================================
# 18. Why Use params?
# ============================================================

# Avoid manually building URLs like:

# url = (
#     "https://example.com/api/users"
#     "?country=India&city=Pune"
# )


# Prefer:

params = {
    "country": "India",
    "city": "Pune"
}

# requests.get(url, params=params)


# This is cleaner and safer.


# ============================================================
# 19. Headers
# ============================================================

# HTTP headers provide additional information
# about the request.

headers = {
    "Accept": "application/json"
}


response = requests.get(
    "https://example.com/api/data",
    headers=headers
)


# ============================================================
# 20. Common Headers
# ============================================================

# Accept
# Tells the server what response format
# the client prefers.


# Content-Type
# Describes the format of data being sent.


headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


# ============================================================
# 21. POST Request
# ============================================================

# POST is commonly used to send data
# to a server.

data = {
    "name": "Trupti",
    "role": "Data Engineer"
}


response = requests.post(
    "https://example.com/api/users",
    json=data
)


# json=data automatically sends the Python
# dictionary as JSON.


# ============================================================
# 22. POST with Headers
# ============================================================

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


data = {
    "name": "Alice",
    "role": "Data Engineer"
}


response = requests.post(
    "https://example.com/api/users",
    headers=headers,
    json=data
)


# ============================================================
# 23. POST Response
# ============================================================

response = requests.post(
    "https://example.com/api/users",
    json=data
)


print(response.status_code)


# A successful creation commonly returns:

# 201


# ============================================================
# 24. json= vs data=
# ============================================================

# For APIs expecting JSON,
# json= is usually convenient.

data = {
    "name": "Alice"
}


# requests.post(
#     url,
#     json=data
# )


# data= is used for form data or other
# request body formats depending on the API.


# ============================================================
# 25. API Authentication
# ============================================================

# Many APIs require authentication.

# Common authentication methods include:

# - API key
# - Bearer token
# - Basic authentication
# - OAuth


# ============================================================
# 26. API Key in Header
# ============================================================

# Example structure:

api_key = "YOUR_API_KEY"


headers = {
    "X-API-Key": api_key
}


# response = requests.get(
#     url,
#     headers=headers
# )


# Never hardcode real API keys
# in source code.


# ============================================================
# 27. Bearer Token
# ============================================================

token = "YOUR_ACCESS_TOKEN"


headers = {
    "Authorization": f"Bearer {token}"
}


# response = requests.get(
#     url,
#     headers=headers
# )


# The token should normally come from
# an environment variable or secret manager.


# ============================================================
# 28. Authentication with Environment Variables
# ============================================================

import os


api_key = os.getenv(
    "API_KEY"
)


headers = {
    "X-API-Key": api_key
}


# This is better than writing the secret
# directly inside the code.


# ============================================================
# 29. Pagination
# ============================================================

# APIs often don't return all records at once.

# Example:
#
# Page 1 → 100 records
# Page 2 → 100 records
# Page 3 → 100 records
#
# This is called pagination.


# ============================================================
# 30. Page-Based Pagination
# ============================================================

page = 1

while True:

    params = {
        "page": page,
        "limit": 100
    }

    response = requests.get(
        "https://example.com/api/data",
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    print(
        f"Processing page {page}"
    )

    # Example stopping condition:

    if not data:

        break

    page += 1


# The exact pagination logic depends
# on the API.


# ============================================================
# 31. Limit and Offset Pagination
# ============================================================

# Another common approach:

limit = 100

offset = 0


while True:

    params = {
        "limit": limit,
        "offset": offset
    }

    # response = requests.get(
    #     url,
    #     params=params
    # )

    # data = response.json()

    # Process data here.

    # if len(data) < limit:
    #     break

    offset += limit


# ============================================================
# 32. Pagination with next URL
# ============================================================

# Some APIs return something like:

# {
#     "data": [...],
#     "next": "https://example.com/api/data?page=2"
# }


# Then we can continue using the next URL.

next_url = "https://example.com/api/data?page=1"


while next_url:

    response = requests.get(
        next_url,
        timeout=10
    )

    response.raise_for_status()

    result = response.json()

    # Process result["data"]

    # next_url = result.get("next")


# Exact implementation depends
# on the API response structure.


# ============================================================
# 33. Complete GET Example
# ============================================================

def get_data(url):

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data

    except requests.exceptions.Timeout:

        print("Request timed out")

    except requests.exceptions.HTTPError:

        print("HTTP error occurred")

    except requests.exceptions.RequestException:

        print("Request failed")

    return None


# Example:

# data = get_data(
#     "https://example.com/api/data"
# )


# ============================================================
# 34. GET with Parameters
# ============================================================

def get_users(url, page, limit):

    params = {
        "page": page,
        "limit": limit
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


# ============================================================
# 35. POST Function
# ============================================================

def create_user(url, user_data):

    response = requests.post(
        url,
        json=user_data,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


# ============================================================
# 36. API Data Extraction
# ============================================================

def extract_api_data(url):

    logging_started = False

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data

    except requests.exceptions.RequestException as error:

        print(
            f"API request failed: {error}"
        )

        return None


# ============================================================
# 37. API + JSON + File
# ============================================================

import json


def fetch_and_save_json(
    url,
    output_file
):

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        with open(
            output_file,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        print(
            "API data saved successfully"
        )

    except requests.exceptions.RequestException as error:

        print(
            f"API request failed: {error}"
        )


# ============================================================
# 38. Data Engineering API Workflow
# ============================================================

# A typical API extraction pipeline:

# API
#  ↓
# GET request
#  ↓
# Authentication
#  ↓
# Query parameters
#  ↓
# Pagination
#  ↓
# JSON response
#  ↓
# Validate response
#  ↓
# Transform data
#  ↓
# Save CSV / Parquet
#
#
# This is an important real-world pattern.


# ============================================================
# 39. API Response Validation
# ============================================================

response = requests.get(
    "https://example.com/api/data",
    timeout=10
)


if response.status_code == 200:

    data = response.json()

    print("Data received")

else:

    print(
        f"Request failed: {response.status_code}"
    )


# ============================================================
# 40. API + pathlib
# ============================================================

from pathlib import Path


output_folder = Path(
    "data/raw"
)


output_folder.mkdir(
    parents=True,
    exist_ok=True
)


output_file = (
    output_folder / "api_data.json"
)


# API data could then be saved
# to output_file.


# ============================================================
# 41. API + Logging
# ============================================================

import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def extract_from_api(url):

    logging.info(
        "API extraction started"
    )

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        logging.info(
            "API extraction completed"
        )

        return data

    except requests.exceptions.RequestException:

        logging.exception(
            "API extraction failed"
        )

        return None


# ============================================================
# 42. API + Error Handling + Logging
# ============================================================

def fetch_data(url):

    logging.info(
        f"Requesting data from API: {url}"
    )

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        logging.info(
            "API request successful"
        )

        return data

    except requests.exceptions.Timeout:

        logging.error(
            "API request timed out"
        )

    except requests.exceptions.HTTPError:

        logging.exception(
            "API returned an HTTP error"
        )

    except requests.exceptions.RequestException:

        logging.exception(
            "API request failed"
        )

    return None


# ============================================================
# 43. Important Security Rule
# ============================================================

# NEVER write secrets directly in code.

# Bad:

# api_key = "abc123secret"


# Better:

# api_key = os.getenv("API_KEY")


# Even better in production:
#
# Use a secret manager or secure environment
# configuration provided by your infrastructure.


# ============================================================
# 44. Common API Problems
# ============================================================

# Timeout
# Server takes too long to respond.


# 400
# Invalid request.


# 401
# Authentication problem.


# 403
# Access is forbidden.


# 404
# Resource doesn't exist.


# 429
# Too many requests.


# 500
# Server-side error.


# ============================================================
# 45. What to Check After an API Request
# ============================================================

# 1. Did the request succeed?
#
# response.raise_for_status()
#
# 2. Is the response JSON?
#
# response.json()
#
# 3. Does the expected data exist?
#
# data.get(...)
#
# 4. Are there more pages?
#
# Pagination
#
# 5. Did the request finish within the timeout?


# ============================================================
# 46. Common Mistakes
# ============================================================

# Mistake 1:
# No timeout.

# Better:

# requests.get(
#     url,
#     timeout=10
# )


# Mistake 2:
# Not checking HTTP errors.

# Better:

# response.raise_for_status()


# Mistake 3:
# Hardcoding API keys.

# Better:

# os.getenv("API_KEY")


# Mistake 4:
# Assuming all APIs return the same JSON structure.

# Always inspect and validate the response.


# Mistake 5:
# Ignoring pagination.

# Large APIs often return only part of the data.


# ============================================================
# 47. Key Takeaways
# ============================================================

# 1. APIs allow applications to communicate.
#
# 2. HTTP is commonly used for API communication.
#
# 3. GET is generally used to retrieve data.
#
# 4. POST is generally used to send/create data.
#
# 5. Query parameters are sent using params=.
#
# 6. Headers provide additional request information.
#
# 7. APIs commonly return JSON.
#
# 8. response.json() converts JSON response data
#    into Python objects.
#
# 9. status_code tells us the HTTP response status.
#
# 10. raise_for_status() raises an exception
#     for unsuccessful HTTP responses.
#
# 11. timeout prevents requests from waiting
#     indefinitely.
#
# 12. Authentication can use API keys or tokens.
#
# 13. Never hardcode secrets.
#
# 14. Pagination is required when an API returns
#     data in multiple pages.
#
# 15. APIs are commonly used in the Extract
#     stage of Data Engineering pipelines.


# ============================================================
# 48. Quick Revision Table
# ============================================================

# Concept                    Python
#
# HTTP library               requests
#
# GET                        requests.get()
#
# POST                       requests.post()
#
# Status code                response.status_code
#
# Response text              response.text
#
# JSON response              response.json()
#
# Query parameters           params=
#
# Headers                    headers=
#
# JSON request body          json=
#
# HTTP error checking        raise_for_status()
#
# Timeout                    timeout=
#
# API key                    Authentication
#
# Pagination                 page / limit / offset / next


