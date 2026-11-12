# Designing and Building of Bots - Hands-on

A practical Python-based automation learning repository focused on Robotic Process Automation (RPA) and task automation concepts. This project contains a series of hands-on bot scripts covering file handling, Excel processing, web automation, email automation, scheduling, queue-based task assignment, and FTP/file management tasks.

The repository is designed for beginners and intermediate learners who want to understand how bots can mimic repetitive office tasks using Python.

## Table of Contents

- [Overview](#overview)
- [Repository Highlights](#repository-highlights)
- [Included Bots](#included-bots)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [How to Run](#how-to-run)
- [Learning Outcomes](#learning-outcomes)
- [Notes](#notes)
- [License](#license)

## Overview

This repository contains a collection of Python task bots that automate common business processes. Each script demonstrates a realistic automation scenario and is built as a simple, self-contained example for learning.

The examples range from:

- basic task execution and system interactions
- data extraction from Excel and text sources
- web form and webpage data scraping
- email sending and inbox monitoring
- scheduled automation and logging
- queue-based ticket assignment
- FTP file transfers and file renaming
- invoice and report generation

## Repository Highlights

- Beginner-friendly Python scripts
- Hands-on examples for RPA and automation workflows
- Realistic business-process bots for office tasks
- Minimal external dependencies for most examples
- Easy-to-follow interactive menu-driven scripts
- Examples using Excel, text files, web pages, email, and FTP workflows

## Included Bots

The repository includes task-based automation examples grouped by theme:

### 1. Basic Automation Bots

- `1a YOUR FIRST BASIC TASK BOT.py`
  - Simple greeting bot
  - Date/time bot
  - Calculator bot

- `1b BOT TO DISPLAY SYSTEM INFORMATION.py`
  - Displays system details such as OS and environment information

### 2. Data Entry and File Automation

- `2a TASK BOT TO AUTOMATE DATA ENTRY TASKS.py`
  - Automates simple data entry operations

- `2b AUTOMATE DATA ENTRY INTO MULTIPLE TEXT FILES BY READING INPUT FROM A PREDEFINED TEXT SOURCE AND SAVING THE FILES WITH DIFFERENT NAMES.py`
  - Creates multiple files from predefined input data

### 3. Excel Data Extraction and Transfer

- `3a BOT TO AUTOMATE EXTRACTION OF DATA FROM AN EXCEL FILE AND COPIES IT TO ANOTHER APPLICATION..py`
  - Extracts values from Excel and transfers them

- `3b BOT TO EXTRACT SPECIFIC ROWS AND COLUMNS FROM AN EXCEL FILE AND PASTE THE EXTRACTED DATA INTO ANOTHER DOCUMENT SUCH AS A TEXT FILE OR NOTEPAD APPLICATION.py`
  - Filters and copies selected spreadsheet contents

### 4. Web Automation

- `4a BOT TO AUTOMATE THE SUBMISSION OF A SIMPLE WEB FORM.py`
  - Simulates web-form submission workflow

- `4b BOT TO AUTOMATICALLY EXTRACT TABULAR DATA DISPLAYED ON A WEBPAGE AND STORE IT IN A LOCAL FILE.py`
  - Scrapes table data from a webpage and saves it locally

### 5. Email Automation

- `5a AUTOMATE THE PROCESS OF SENDING AN EMAIL USING A BOT.py`
  - Sends email via SMTP

- `5b A BOT TO AUTOMATICALLY READ INCOMING EMAILS AND GENERATE A SUMMARY REPORT SHOWING THE COUNT OF EMAILS RECEIVED PER DAY.py`
  - Reads email data and summarizes counts per day

### 6. Scheduling and Monitoring

- `6a CREATE A BOT TO AUTOMATICALLY LAUNCH A WEBSITE EVERY DAY AT A SPECIFIC TIME.py`
  - Opens a website on a scheduled time

- `6b BOT TO PERFORM A REPETITIVE TASK AT FIXED TIME INTERVALS AND RECORD EACH EXECUTION IN A LOG FILE.py`
  - Runs periodic tasks and logs execution details

### 7. Queue and Ticket Automation

- `7a AUTOMATE THE PROCESS OF ASSIGNING CUSTOMER SUPPORT TICKETS USING QUEUES.py`
  - Assigns support requests using queue logic

- `7b BOT TO PRIORITIZE CUSTOMER SUPPORT TICKETS FROM AN EXCEL FILE AND ASSIGN HIGH-PRIORITY TICKETS TO SENIOR AGENTS USING A QUEUE MECHANISM.py`
  - Prioritizes tickets and distributes them to agents

### 8. Email Inbox Monitoring

- `8a AUTOMATE THE PROCESS OF LOGGING INTO A WEB-BASED EMAIL ACCOUNT, CHECKING FOR NEW MESSAGES, AND LOGGING OUT.py`
  - Simulates login, check, and logout workflow

- `8b BOT TO MONITOR AN EMAIL INBOX PERIODICALLY AND DISPLAY ALERTS WHEN NEW UNREAD EMAILS ARE DETECTED.py`
  - Checks inbox and raises alerts for unread mail

### 9. FTP and File Management

- `9a BOT TO DOWNLOAD FILES FROM AN FTP SERVER AND LOOP THROUGH THEM TO RENAME EACH FILE BASED ON A SPECIFIC PATTERN.py`
  - Downloads and renames FTP files

- `9b BOT TO AUTOMATICALLY MOVE FILES BETWEEN DIRECTORIES ON AN FTP SERVER BASED ON FILE TYPE.py`
  - Organizes files into directories based on type

### 10. Invoice and Business Process Automation

- `10a BOT TO CREATE AND DELIVER INVOICES.py`
  - Creates and sends invoice content

- `10b BOT TO GENERATE INVOICES FOR MULTIPLE CUSTOMERS BY READING CUSTOMER DETAILS FROM AN EXCEL FILE AND SAVING THE INVOICES AUTOMATICALLY.py`
  - Generates invoices automatically from Excel input

## Project Structure

```text
Designing-and-Building-of-Bots---Hands-on/
├── 1a YOUR FIRST BASIC TASK BOT.py
├── 1b BOT TO DISPLAY SYSTEM INFORMATION.py
├── 2a TASK BOT TO AUTOMATE DATA ENTRY TASKS.py
├── 2b AUTOMATE DATA ENTRY INTO MULTIPLE TEXT FILES BY READING INPUT FROM A PREDEFINED TEXT SOURCE AND SAVING THE FILES WITH DIFFERENT NAMES.py
├── 3a BOT TO AUTOMATE EXTRACTION OF DATA FROM AN EXCEL FILE AND COPIES IT TO ANOTHER APPLICATION..py
├── 3b BOT TO EXTRACT SPECIFIC ROWS AND COLUMNS FROM AN EXCEL FILE AND PASTE THE EXTRACTED DATA INTO ANOTHER DOCUMENT SUCH AS A TEXT FILE OR NOTEPAD APPLICATION.py
├── 4a BOT TO AUTOMATE THE SUBMISSION OF A SIMPLE WEB FORM.py
├── 4b BOT TO AUTOMATICALLY EXTRACT TABULAR DATA DISPLAYED ON A WEBPAGE AND STORE IT IN A LOCAL FILE.py
├── 5a AUTOMATE THE PROCESS OF SENDING AN EMAIL USING A BOT.py
├── 5a simulated.py
├── 5b A BOT TO AUTOMATICALLY READ INCOMING EMAILS AND GENERATE A SUMMARY REPORT SHOWING THE COUNT OF EMAILS RECEIVED PER DAY.py
├── 5b simulated.py
├── 6a CREATE A BOT TO AUTOMATICALLY LAUNCH A WEBSITE EVERY DAY AT A SPECIFIC TIME.py
├── 6b BOT TO PERFORM A REPETITIVE TASK AT FIXED TIME INTERVALS AND RECORD EACH EXECUTION IN A LOG FILE.py
├── 7a AUTOMATE THE PROCESS OF ASSIGNING CUSTOMER SUPPORT TICKETS USING QUEUES.py
├── 7b BOT TO PRIORITIZE CUSTOMER SUPPORT TICKETS FROM AN EXCEL FILE AND ASSIGN HIGH-PRIORITY TICKETS TO SENIOR AGENTS USING A QUEUE MECHANISM.py
├── 8a AUTOMATE THE PROCESS OF LOGGING INTO A WEB-BASED EMAIL ACCOUNT, CHECKING FOR NEW MESSAGES, AND LOGGING OUT.py
├── 8a simulated.py
├── 8b BOT TO MONITOR AN EMAIL INBOX PERIODICALLY AND DISPLAY ALERTS WHEN NEW UNREAD EMAILS ARE DETECTED.py
├── 8b simulated.py
├── 9a BOT TO DOWNLOAD FILES FROM AN FTP SERVER AND LOOP THROUGH THEM TO RENAME EACH FILE BASED ON A SPECIFIC PATTERN.py
├── 9a simulated.py
├── 9b BOT TO AUTOMATICALLY MOVE FILES BETWEEN DIRECTORIES ON AN FTP SERVER BASED ON FILE TYPE.py
├── 9b simulated.py
├── 10a BOT TO CREATE AND DELIVER INVOICES.py
├── 10b BOT TO GENERATE INVOICES FOR MULTIPLE CUSTOMERS BY READING CUSTOMER DETAILS FROM AN EXCEL FILE AND SAVING THE INVOICES AUTOMATICALLY.py
├── customers.xlsx
├── data.xlsx
├── tickets.xlsx
├── student_data.xlsx
├── input.txt
├── output.txt
├── web_data.txt
├── email_report.txt
├── unread_email_report.txt
├── assigned_tickets.txt
├── log.txt
├── invoice_Arjun.txt
├── invoice_Harshita.txt
├── invoice_Priya.txt
├── invoice_Rahul.txt
├── fake_email.txt
└── README.md
```

## Prerequisites

Before running the scripts, make sure you have:

- Python 3.8 or later
- A local Python environment
- Access to required packages depending on the task

Common packages used in the examples include:

- `requests`
- `beautifulsoup4`
- `openpyxl`
- `pandas` (for spreadsheet-based automation)
- `smtplib` and standard library modules

Install required packages using:

```bash
pip install requests beautifulsoup4 openpyxl pandas
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/harshitaukv/Designing-and-Building-of-Bots---Hands-on.git
cd Designing-and-Building-of-Bots---Hands-on
```

2. Run any script with Python:

```bash
python "1a YOUR FIRST BASIC TASK BOT.py"
```

3. Follow the interactive prompts shown in the terminal.

Some scripts may require files such as `.xlsx`, `.txt`, or sample email data to be available in the same folder.

## Learning Outcomes

By exploring this repository, you will learn:

- how to design simple task bots in Python
- how to automate repetitive office work
- how to read and write text and Excel data
- how to extract information from websites
- how to send and read emails programmatically
- how to schedule recurring tasks
- how to build queue-based assignment logic
- how to manage file transfers and file organization
- how to approach business automation with modular scripts

## Notes

- This repository is intended for hands-on learning and demonstration.
- Some scripts are simulated examples and may need minor adjustments for real-world systems or credentials.
- For email automation, credentials and app passwords should be handled securely and never hardcoded in production systems.
- Example files included in the repository are meant to support the scripts and help demonstrate automation behavior.

## License

This project is provided for educational and learning purposes. Please use it responsibly and adapt the examples to your own environment and use case.

---

Built for hands-on learning in robotic process automation and Python bot development.
