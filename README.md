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

##project-2 Web Applications 

Website URL Checker using Python

Project Description

Website URL Checker is a simple Python-based application that checks whether a website can be reached successfully.

The program accepts a website URL from the user and sends an HTTP/HTTPS request using the Python Requests library. It displays the HTTP status code when a response is received and shows an appropriate error message when a connection problem occurs.

Objectives

- To check whether a website is reachable.
- To understand HTTP and HTTPS requests.
- To learn how to use the Python Requests library.
- To understand basic URL handling.
- To implement exception handling.
- To develop a simple command-line networking tool.

Technologies Used

- Python 3
- Requests library
- HTTP/HTTPS
- Internet connection
- Pydroid 3 / Python environment

Requirements

Python 3 and the Requests library are required.

Install the Requests library using:

pip install requests

Features

- Simple command-line interface
- Accepts website URLs from the user
- Automatically adds "https://" when the protocol is not provided
- Checks website connectivity
- Displays HTTP status codes
- Handles connection errors
- Handles timeout errors
- Handles invalid URL errors

How the Program Works

1. The user enters a website URL.
2. The program checks whether the URL contains "http://" or "https://".
3. If no protocol is provided, "https://" is added automatically.
4. The Requests library sends an HTTP/HTTPS request.
5. The program receives the server response.
6. The HTTP status code is displayed.
7. If an error occurs, an appropriate error message is displayed.

Example

Input

Enter website URL: https://google.com

Output

Website is reachable.
URL: https://google.com
Status Code: 200

A status code of "200" generally indicates that the server successfully processed the request.

Error Handling

The application handles common problems such as:

- Connection timeout
- Connection failure
- Invalid URL
- DNS/name-resolution problems
- Other HTTP request errors

How to Run

Using Pydroid 3

1. Open Pydroid 3.
2. Install the Requests package.
3. Create a new Python file.
4. Save it as "website_checker.py".
5. Paste the project code.
6. Run the program.
7. Enter a complete website URL.

Using Python

Install the required package:

pip install -r requirements.txt

Run the program:

python website_checker.py

Sample Test Cases

Test Case| Input| Expected Result
1| "https://google.com"| HTTP response/status displayed
2| "https://github.com"| HTTP response/status displayed
3| "google.com"| HTTPS added automatically
4| "sanjana.invalid"| Connection/name-resolution error
5| Unresponsive website| Timeout error

Limitations

- An internet connection is required.
- Some websites may block automated requests.
- Temporary server or DNS problems may affect the result.
- A successful response does not guarantee that every page or feature of a website works correctly.

Future Enhancements

The project can be improved by adding:

- Website response-time measurement
- Multiple URL checking
- Automatic URL validation
- Status-code descriptions
- Website availability reports
- Logging of checked URLs
- Graphical user interface
- CSV or Excel report generation
- Website availability history

Conclusion

The Website URL Checker is a beginner-friendly Python project that demonstrates basic networking concepts, HTTP/HTTPS communication, URL handling, the Requests library, and exception handling.

The project provides practical experience in developing a simple command-line networking application and can be extended with additional monitoring and reporting features.

