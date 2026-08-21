"""
Python API Integration
======================

An API (Application Programming Interface) allows two
software systems to communicate with each other.

In Data Engineering, APIs are commonly used as a
data source during the Extract stage of an ETL/ELT pipeline.

Typical workflow:

API
 ↓
HTTP Request
 ↓
Response
 ↓
Check Status
 ↓
Read JSON
 ↓
Validate Data
 ↓
Transform Data
 ↓
Store Data
"""


# ============================================================
# 1. What is an API?
# ============================================================

# API = Application Programming Interface
#
# An API allows different applications or systems
# to communicate and exchange data.
#
# Example:
#
# Python Program
#       ↓
#      API
#       ↓
#    Server
#       ↓
#   JSON Response
#       ↓
# Python Program
#
#
# In Data Engineering, APIs are commonly used to
# extract data from external systems.


# ============================================================
# 2. HTTP
# ============================================================

# HTTP = HyperText Transfer Protocol
#
# It is commonly used for communication between
# a client and a server.
#
# Python Program = Client
# API Server    = Server
#
# Client sends a REQUEST.
# Server sends a RESPONSE.


# ============================================================
# 3. HTTP Methods
# ============================================================

# GET
# Retrieve data from an API.

# POST
# Send data to an API, commonly to create a resource.

# PUT
# Update an entire resource.

# PATCH
# Partially update a resource.

# DELETE
# Delete a resource.
#
#
# For your current level, focus mainly on:
#
# GET
# POST


# ============================================================
# 4. requests Library
# ============================================================

# Python commonly uses the requests library
# to communicate with HTTP APIs.

import requests


# Install if required:
#
# pip install requests


# ============================================================
# 5. GET Request
# ============================================================

# GET is generally used to retrieve data.

response = requests.get(
    "https://example.com",
    timeout=10
)

print(response)


# response is a Response object.


# ============================================================
# 6. Status Code
# ============================================================

# The status code tells us what happened
# with our request.

print(response.status_code)


# Important status codes:

# 200 -> Request successful
# 201 -> Resource created
# 400 -> Bad request
# 401 -> Unauthorized
# 403 -> Forbidden
# 404 -> Resource not found
# 429 -> Too many requests
# 500 -> Server error


# You do not need to memorize every status code.
# Understand what the common ones mean.


# ============================================================
# 7. Response Text
# ============================================================

# response.text returns the response body
# as a string.

print(response.text)


# ============================================================
# 8. JSON Response
# ============================================================

# APIs commonly return data in JSON format.
#
# Example JSON:
#
# {
#     "id": 101,
#     "name": "Alice",
#     "role": "Data Engineer"
# }


# Convert JSON response into a Python object:

# data = response.json()

# print(data)


# Usually the result will be a:
#
# dictionary
# or
# list


# Example:

# print(data["name"])


# ============================================================
# 9. Checking for HTTP Errors
# ============================================================

# Instead of manually checking every status code,
# requests provides raise_for_status().

response = requests.get(
    "https://example.com",
    timeout=10
)

response.raise_for_status()


# If the server returns an unsuccessful HTTP status,
# an appropriate exception is raised.


# This is a very useful pattern to remember.


# ============================================================
# 10. Query Parameters
# ============================================================

# Query parameters allow us to send additional
# values with a request.
#
# Example:
#
# ?page=1&limit=100

params = {
    "page": 1,
    "limit": 100
}

response = requests.get(
    "https://example.com/api/data",
    params=params,
    timeout=10
)


# requests automatically builds the query string.


# ============================================================
# 11. Why Use params=?
# ============================================================

# Instead of manually creating:

# url = "https://example.com/api/data?page=1&limit=100"

# Use:

params = {
    "page": 1,
    "limit": 100
}

# requests.get(
#     url,
#     params=params
# )


# This is cleaner and easier to maintain.


# ============================================================
# 12. Headers
# ============================================================

# Headers provide additional information
# about the request.

headers = {
    "Accept": "application/json"
}

response = requests.get(
    "https://example.com/api/data",
    headers=headers,
    timeout=10
)


# Common headers:

# Accept
# What response format the client prefers.

# Content-Type
# Format of the data being sent.


# ============================================================
# 13. POST Request
# ============================================================

# POST is commonly used to send data to an API.

user_data = {
    "name": "Trupti",
    "role": "Data Engineer"
}

response = requests.post(
    "https://example.com/api/users",
    json=user_data,
    timeout=10
)


# json=user_data sends the dictionary
# as a JSON request body.


# ============================================================
# 14. json= vs data=
# ============================================================

# For APIs expecting JSON:

requests.post(
    url,
    json=user_data
)


# data= can be used for form data or other
# body formats depending on the API.
#
# For your level, remember:
#
# json= -> commonly used when sending JSON data.


# ============================================================
# 15. Timeout
# ============================================================

# A timeout prevents a request from waiting
# indefinitely.

response = requests.get(
    "https://example.com",
    timeout=10
)


# timeout=10 means the request will not
# wait indefinitely for a response.


# In real API integration code,
# always consider using a timeout.


# ============================================================
# 16. Error Handling
# ============================================================

# API requests can fail because of:
#
# - Timeout
# - Network problem
# - HTTP error
# - Invalid URL
# - Server problem


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

    print("API request failed")


# RequestException is a general requests-related
# exception.


# ============================================================
# 17. API Authentication
# ============================================================

# Some APIs require authentication before
# allowing access to data.
#
# Common methods:
#
# - API Key
# - Bearer Token
# - Basic Authentication
# - OAuth
#
# For your current level, understand:
#
# API authentication = proving that the client
# is authorized to access the API.


# ============================================================
# 18. API Key
# ============================================================

# Example structure:

api_key = "YOUR_API_KEY"

headers = {
    "X-API-Key": api_key
}


# IMPORTANT:
#
# Never hardcode a real API key in source code.
#
# Bad:
#
# api_key = "real-secret-key"


# ============================================================
# 19. Environment Variable for Secrets
# ============================================================

import os

api_key = os.getenv("API_KEY")

headers = {
    "X-API-Key": api_key
}


# This is safer than storing the secret
# directly in the Python file.


# ============================================================
# 20. Bearer Token
# ============================================================

token = os.getenv("API_TOKEN")

headers = {
    "Authorization": f"Bearer {token}"
}


# The token is normally stored securely,
# rather than directly in source code.


# ============================================================
# 21. Pagination
# ============================================================

# APIs often do not return all records in one response.
#
# Example:
#
# Page 1 -> 100 records
# Page 2 -> 100 records
# Page 3 -> 100 records
#
# This is called pagination.


# A common page-based approach:

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

    # Process data here.

    if not data:
        break

    page += 1


# Exact pagination logic depends on the API.


# ============================================================
# 22. Common Pagination Types
# ============================================================

# Page-based:
#
# page=1
# page=2
# page=3


# Limit + Offset:
#
# limit=100
# offset=0
#
# limit=100
# offset=100
#
# limit=100
# offset=200


# Next URL:
#
# Some APIs return a "next" URL in the response.
#
# The exact method depends on the API.


# ============================================================
# 23. Reusable GET Function
# ============================================================

def get_data(url):

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:

        print(f"API request failed: {error}")

        return None


# Example:
#
# data = get_data(
#     "https://example.com/api/data"
# )


# ============================================================
# 24. GET Function with Parameters
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
# 25. Reusable POST Function
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
# 26. API + Data Engineering
# ============================================================

# A typical Data Engineering workflow:

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
# Validate data
#  ↓
# Transform data
#  ↓
# Save CSV / Parquet
#  ↓
# Load into database / warehouse


# API is therefore commonly used
# during the Extract stage.


# ============================================================
# 27. API + Logging
# ============================================================

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def extract_from_api(url):

    logging.info("API extraction started")

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        logging.info("API extraction successful")

        return data

    except requests.exceptions.RequestException:

        logging.exception("API extraction failed")

        return None


# ============================================================
# 28. Important Security Rule
# ============================================================

# NEVER log or hardcode secrets.

# Do NOT do:

# print(api_key)
#
# logging.info(api_key)
#
# api_key = "real-secret"


# Prefer:

# api_key = os.getenv("API_KEY")


# In production, secret managers may also be used.


# ============================================================
# 29. Common API Problems
# ============================================================

# Timeout
# -> Server takes too long to respond.

# 400
# -> Request is invalid.

# 401
# -> Authentication problem.

# 403
# -> Access is forbidden.

# 404
# -> Resource was not found.

# 429
# -> Too many requests.

# 500
# -> Server-side problem.


# ============================================================
# 30. Important API Checklist
# ============================================================

# When writing API code, remember:

# 1. Use requests
#
# 2. Use GET to retrieve data
#
# 3. Use POST to send/create data
#
# 4. Use params= for query parameters
#
# 5. Use headers= for headers
#
# 6. Use json= when sending JSON data
#
# 7. Use response.status_code to inspect status
#
# 8. Use response.json() to read JSON
#
# 9. Use raise_for_status() to detect HTTP errors
#
# 10. Use timeout= so requests do not wait forever
#
# 11. Handle exceptions
#
# 12. Understand API authentication
#
# 13. Never hardcode secrets
#
# 14. Understand pagination
#
# 15. Validate API data before processing it


# ============================================================
# 31. Quick Revision Table
# ============================================================

# Concept                  Python
#
# HTTP library             requests
#
# GET                      requests.get()
#
# POST                     requests.post()
#
# Status code              response.status_code
#
# Response text            response.text
#
# JSON response            response.json()
#
# Query parameters         params=
#
# Headers                  headers=
#
# JSON request body        json=
#
# HTTP error checking      raise_for_status()
#
# Timeout                  timeout=
#
# Authentication           API key / token
#
# Secret management        os.getenv()
#
# Multiple pages           Pagination
#
# Error handling           try / except


# ============================================================
# ⭐ ONE-MINUTE REVISION
# ============================================================

# API
# → Allows applications to communicate

# GET
# → Retrieve data

# POST
# → Send/create data

# JSON
# → Common API data format

# status_code
# → Tells whether request succeeded/failed

# params=
# → Query parameters

# headers=
# → Additional request information / authentication

# json=
# → Send JSON data

# timeout=
# → Prevent indefinite waiting

# raise_for_status()
# → Raise exception for HTTP errors

# try/except
# → Handle API errors

# Authentication
# → Prove access to the API

# os.getenv()
# → Read secrets from environment variables

# Pagination
# → Retrieve large datasets page by page