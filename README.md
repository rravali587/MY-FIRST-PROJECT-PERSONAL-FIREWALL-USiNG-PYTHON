 MY-FIRST-PROJECT-PERSONAL-FIREWALL-USiNG-PYTHON
# Personal Firewall Using Python

## 1. Project Overview

Personal Firewall is a Python-based cybersecurity project designed to monitor network connections on a computer or mobile Python environment.

The project provides a simple command-line interface to monitor active network connections and save firewall-related information into a log file.

## 2. Objectives

- Monitor active network connections.
- Display network connection details.
- Save firewall monitoring information in a log file.
- Provide a simple and user-friendly menu.
- Understand the basic working of a firewall using Python.

## 3. Technologies Used

- Python
- Psutil Library
- File Handling
- Command Line Interface (CLI)

## 4. Main Features

### Monitor Network Connections
The program checks active network connections and displays available connection information.

### Save Firewall Log
The monitoring information can be saved into a file named:

`firewall_log.txt`

### Simple Menu

The program provides three options:

1. Monitor Network Connections
2. Save Firewall Log
3. Exit

## 5. How It Works

When the program starts, it displays the Personal Firewall menu.

The user can select an option:

- **Option 1:** Monitor network connections.
- **Option 2:** Save the firewall log.
- **Option 3:** Exit the application.

The `psutil` Python library is used to obtain network connection information.

## 6. Requirements
python.3x


PROJECT 2 WEB APPLICATION VULNERABLITY SCANNER

# Website URL Checker using Python

## Project Description

This project is a simple Python-based Website URL Checker. It checks whether a given website URL is reachable or not by sending an HTTP/HTTPS request using the Python requests library.

The program asks the user to enter a website URL and checks the connection. If the website is reachable, it displays the HTTP status code. If the website cannot be reached, it displays an appropriate error message.

## Features

- Accepts a website URL from the user
- Checks website connectivity
- Displays HTTP status code
- Shows whether the website is reachable
- Handles connection errors
- Simple and easy-to-use Python program

## Technologies Used

- Python
- Requests Library
- Pydroid 3

## Installation

Install the required requests library using:

pip install requests

## How to Run

1. Open Pydroid 3.
2. Open the Python project file.
3. Run the program.
4. Enter a complete website URL.

Example:

https://www.google.com

Expected Output:

Website is reachable!
Status Code: 200

## Error Handling

If an invalid website name is entered, the program displays an error message.

For example:

sanjana

This is not a complete website URL, so the program may show a hostname resolution error.

Use a complete URL such as:

https://www.google.com

instead of:

sanjana

## Test Cases

| Test Case | Input | Expected Result |
|----------|-------|-----------------|
| 1 | https://www.google.com | Website reachable |
| 2 | https://www.youtube.com | Website reachable |
| 3 | sanjana | Invalid/hostname error |
| 4 | https://example.com | Website reachable |

## Project Output

The program displays:

- Entered website URL
- Website connection status
- HTTP response status code
- Error message if the website cannot be reached

## Conclusion

The Website URL Checker using Python is a simple networking project that demonstrates how Python can be used to check website availability. It helps in understanding HTTP requests, response status codes, URL validation, and basic network error handling.
