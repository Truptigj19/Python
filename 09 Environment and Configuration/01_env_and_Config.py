"""
Python Environment & Configuration
==================================

Configuration means keeping values that may change
between environments outside the main program logic.

Examples:

- API keys
- Passwords
- Database credentials
- API URLs
- File paths
- Environment names

Instead of writing secrets directly in Python code,
we can store them in environment variables.

Typical flow:

Environment Variable
        ↓
     os.getenv()
        ↓
   Python Program
"""


# ============================================================
# 1. What is Configuration?
# ============================================================

# Configuration contains values that control
# how an application or pipeline behaves.
#
# Examples:
#
# API URL
# Database name
# Database username
# API key
# File location
# Environment name
#
# These values may change between:
#
# Development
# Testing
# Production


# ============================================================
# 2. Why Configuration Should Be Separate
# ============================================================

# Bad approach:

API_KEY = "abc123secret"

# The problem:
#
# - Secret is visible in source code
# - Secret may accidentally be pushed to GitHub
# - Different environments require different values
#
#
# Better approach:
#
# Store the value outside the source code
# and read it using an environment variable.


# ============================================================
# 3. Environment Variables
# ============================================================

# An environment variable is a value stored
# outside the Python program.
#
# Example:
#
# API_KEY=abc123secret
#
# Python can read this value using os.getenv().


# ============================================================
# 4. Import os
# ============================================================

import os


# ============================================================
# 5. os.getenv()
# ============================================================

api_key = os.getenv("API_KEY")

print(api_key)


# os.getenv("API_KEY")
#
# means:
#
# "Get the value of the environment variable API_KEY."


# ============================================================
# 6. If the Variable Does Not Exist
# ============================================================

api_key = os.getenv("API_KEY")

print(api_key)


# If API_KEY is not defined,
# os.getenv() returns:
#
# None


# ============================================================
# 7. Default Value
# ============================================================

environment = os.getenv(
    "ENVIRONMENT",
    "development"
)

print(environment)


# If ENVIRONMENT exists:
#
# → its value is returned
#
# If it does not exist:
#
# → "development" is returned


# ============================================================
# 8. Environment Variables for API URLs
# ============================================================

API_URL = os.getenv(
    "API_URL"
)

print(API_URL)


# This allows different environments
# to use different API URLs.


# Example:
#
# Development:
# API_URL=https://dev.example.com
#
# Production:
# API_URL=https://api.example.com


# ============================================================
# 9. Environment Variables for Database
# ============================================================

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# These values can be used when
# connecting to a database.


# ============================================================
# 10. Environment Variables for API Authentication
# ============================================================

API_KEY = os.getenv("API_KEY")


headers = {
    "X-API-Key": API_KEY
}


# The API key is not written directly
# inside the Python source code.


# ============================================================
# 11. Bearer Token
# ============================================================

API_TOKEN = os.getenv("API_TOKEN")


headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}


# Commonly used for authenticated APIs.


# ============================================================
# 12. Why Secrets Should NOT Be Hardcoded
# ============================================================

# NEVER do this:

API_KEY = "my-real-api-key"


# Problems:
#
# 1. Other developers can see it.
#
# 2. It can accidentally be pushed to GitHub.
#
# 3. Someone could use the exposed credential.
#
# 4. Changing the secret requires changing code.
#
# 5. Different environments need different secrets.


# ============================================================
# 13. Better Approach
# ============================================================

API_KEY = os.getenv("API_KEY")


# Now the actual secret is stored
# outside the Python source code.


# ============================================================
# 14. .env File
# ============================================================

# During local development, a .env file
# is commonly used to store environment variables.
#
# Example .env:
#
# API_KEY=your_api_key
# DB_HOST=localhost
# DB_USER=root
# DB_PASSWORD=your_password
# DB_NAME=my_database
#
#
# IMPORTANT:
#
# Do NOT commit the .env file
# if it contains secrets.


# ============================================================
# 15. python-dotenv
# ============================================================

# A common package for loading .env values
# during local development is python-dotenv.
#
# Install:
#
# pip install python-dotenv


# Example:

from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")

print(API_KEY)


# load_dotenv()
#
# loads variables from the .env file
# into the environment for the Python process.


# ============================================================
# 16. Example .env Structure
# ============================================================

# .env
#
# API_KEY=abc123
# API_URL=https://example.com
# DB_HOST=localhost
# DB_USER=root
# DB_PASSWORD=password123


# Python:

load_dotenv()

api_key = os.getenv("API_KEY")
api_url = os.getenv("API_URL")


# ============================================================
# 17. .gitignore
# ============================================================

# If using Git, add .env to .gitignore.
#
# Example .gitignore:
#
# .env
#
#
# This helps prevent accidentally committing
# the .env file.


# ============================================================
# 18. Configuration vs Secrets
# ============================================================

# Not every configuration value is a secret.
#
# Example configuration:
#
# ENVIRONMENT=development
# API_URL=https://example.com
#
#
# Secrets:
#
# API_KEY
# PASSWORD
# ACCESS_TOKEN
# SECRET_KEY
#
#
# Secrets require special protection.


# ============================================================
# 19. Environment-Based Configuration
# ============================================================

environment = os.getenv(
    "ENVIRONMENT",
    "development"
)


if environment == "development":

    print("Running in development")


elif environment == "production":

    print("Running in production")


# The same code can behave differently
# depending on the environment.


# ============================================================
# 20. Required Environment Variables
# ============================================================

# Sometimes a variable must exist.

api_key = os.getenv("API_KEY")


if not api_key:

    raise ValueError(
        "API_KEY environment variable is required"
    )


# This prevents the application from
# continuing without a required secret.


# ============================================================
# 21. Reusable Configuration
# ============================================================

def get_config():

    return {
        "api_url": os.getenv("API_URL"),
        "api_key": os.getenv("API_KEY"),
        "environment": os.getenv(
            "ENVIRONMENT",
            "development"
        )
    }


config = get_config()

print(config["api_url"])


# Keeping configuration in one place
# makes the application easier to manage.


# ============================================================
# 22. Data Engineering Example
# ============================================================

# Imagine an ETL pipeline:

# API
# ↓
# Extract
# ↓
# Transform
# ↓
# Load into Database
#
#
# The pipeline may need:

API_URL = os.getenv("API_URL")

API_KEY = os.getenv("API_KEY")

DB_HOST = os.getenv("DB_HOST")

DB_USER = os.getenv("DB_USER")

DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_NAME = os.getenv("DB_NAME")


# None of these secrets need to be written
# directly into the Python code.


# ============================================================
# 23. Configuration in Different Environments
# ============================================================

# Development:
#
# API_URL=https://dev-api.example.com
# DB_NAME=dev_database
#
#
# Production:
#
# API_URL=https://api.example.com
# DB_NAME=production_database
#
#
# The Python code can remain the same.
# Only the configuration changes.


# ============================================================
# 24. Common Mistakes
# ============================================================

# Mistake 1:
# Hardcoding API keys.

# Bad:
#
# API_KEY = "abc123"


# Better:
#
# API_KEY = os.getenv("API_KEY")


# ------------------------------------------------------------

# Mistake 2:
# Committing .env to GitHub.

# Better:
#
# Add .env to .gitignore.


# ------------------------------------------------------------

# Mistake 3:
# Assuming environment variables always exist.

# Better:

API_KEY = os.getenv("API_KEY")

if not API_KEY:

    raise ValueError(
        "API_KEY is missing"
    )


# ------------------------------------------------------------

# Mistake 4:
# Printing secrets in logs.

# Bad:

# print(API_KEY)

# Never expose passwords, tokens,
# or API keys in logs.


# ============================================================
# 25. Key Takeaways
# ============================================================

# Configuration
# → Values that control application behavior.
#
# Environment Variable
# → Value stored outside the Python source code.
#
# os.getenv()
# → Reads an environment variable.
#
# .env
# → Common local-development file for environment variables.
#
# python-dotenv
# → Loads .env values during local development.
#
# .gitignore
# → Prevents files such as .env from being committed.
#
# Secrets
# → API keys, passwords, tokens, etc.
#
# Never hardcode secrets.
#
# Never commit secrets to GitHub.
#
# Never print secrets in logs.


# ============================================================
# ⭐ FRESHER MUST-KNOW CHEAT SHEET
# ============================================================

# import os
#
# os.getenv("API_KEY")
# → Read environment variable
#
# os.getenv("ENV", "development")
# → Read variable with default value
#
# .env
# → Store local environment variables
#
# load_dotenv()
# → Load .env variables
#
# .gitignore
# → Keep .env out of Git
#
# API_KEY / PASSWORD / TOKEN
# → Treat as secrets
#
# NEVER hardcode secrets.
#
# NEVER commit secrets to GitHub.
#
# NEVER print secrets in logs.
#
# Data Engineering use:
#
# API credentials
# Database credentials
# API URLs
# Environment-specific configuration