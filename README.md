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

