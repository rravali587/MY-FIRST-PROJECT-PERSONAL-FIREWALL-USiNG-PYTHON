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

Python 3.x

Install the required library using:

```bash
pip install psutil

Website URL Checker
1. Project Title
Website URL Checker using Python
2. Project Description
This project is a simple Python program that checks whether a website URL can be connected successfully.
The program asks the user to enter a website URL. It then sends a request to the given address using the Python requests library.
If the website is reachable, the program displays the website response/status. If the URL is invalid, the domain cannot be found, or there is a connection problem, the program displays an appropriate error message.
3. Objective
The main objectives of this project are:
To check whether a website is reachable.
To understand how Python handles HTTP/HTTPS requests.
To learn how to use the requests library.
To handle connection and URL-related errors.
To provide a simple command-line tool for checking website connectivity.
4. Technologies Used
Python 3
Requests library
HTTP/HTTPS
Internet connection
Pydroid 3 / Python environment
5. Requirements
Before running the project, make sure Python 3 is installed.
Install the required library using:
pip install requests
In Pydroid 3, the Requests package can also be installed using the Pip section.
6. How the Program Works
Step 1: The program asks the user to enter a website URL.
Step 2: The entered URL is used to create an HTTP/HTTPS request.
Step 3: Python tries to connect to the website.
Step 4: If the connection is successful, the program receives a response from the website.
Step 5: If the connection fails, the program catches the error and displays an error message instead of stopping unexpectedly.
7. Example Input
Enter website URL: https://google.com
8. Example of a Successful Result
The program may display a successful response/status when the website is reachable.
Example:
Website is reachable. Status Code: 200
A status code of 200 generally indicates that the request was successfully processed.
9. Invalid URL Example
Example input:
Enter website URL: sanjana
If sanjana is not a valid/resolvable hostname, Python may display an error similar to:
NameResolutionError
This means the system could not find an address associated with the entered hostname.
10. Error Handling
The program handles common connection problems such as:
Invalid URL
Website not reachable
DNS/name resolution failure
Connection timeout
Network connection problems
HTTP request errors
Error handling makes the program more reliable and user-friendly.
11. Important Note About URLs
A complete website URL should normally include the protocol.
Correct examples:
https://google.com https://github.com https://example.com
Entering only:
google sanjana
may not work because the program may not be able to identify or resolve the hostname correctly.
12. Features
Simple command-line interface
Easy to use
Checks website connectivity
Uses Python Requests library
Handles connection errors
Displays useful error information
Suitable for beginners learning Python networking
13. Advantages
Very simple implementation
Easy to understand
Helps beginners learn HTTP requests
Saves time when checking basic website connectivity
Demonstrates practical exception handling
14. Limitations
Requires an internet connection.
A website may be temporarily unavailable.
DNS problems can prevent a connection.
A successful connection does not guarantee that every page or feature of the website works correctly.
Some websites may block automated requests.
15. How to Run in Pydroid 3
Open Pydroid 3.
Create a new Python file.
Paste the Python program.
Install the requests package if it is not already installed.
Run the program.
Enter a complete website URL when prompted.
Check the displayed result.
16. Sample Test Cases
Test Case 1: Input: https://google.com
Expected: The program should connect successfully if the internet connection is available.
Test Case 2: Input: https://github.com
Expected: The program should connect successfully if the website is reachable.
Test Case 3: Input: sanjana
Expected: The program may display a name resolution or connection error because the entered value may not be a valid/resolvable website hostname.
17. Conclusion
The Website URL Checker is a beginner-friendly Python project that demonstrates how to send requests to websites and handle network errors.
This project provides practical knowledge of Python's requests library, HTTP/HTTPS communication, URL handling, and exception handling. It can also be extended in the future to check multiple websites, display response times, and generate reports.
18. Future Enhancements
The project can be improved by adding:
Website response-time measurement
Multiple URL checking
Automatic URL validation
Status code descriptions
Website availability reports
Logging of checked URLs
A graphical user interface
Exporting results to CSV or Excel
19. Project Summary
Project Name: Website URL Checker
Language: Python
Library: Requests
Input: Website URL
Output: Website connection/status or error message
Purpose: To check website connectivity and demonstrate basic Python networking and error handling.