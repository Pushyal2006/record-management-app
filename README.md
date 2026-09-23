# Console Record-Management Application

**Course:** MCA Semester I – Python Programming & Relational Database
**Assignment:** Assignment 1 – Mini Project

## Project Description

A menu-driven, console-based Record-Management Application built in Python.

The application allows users to add, view, search, update, and delete student records such as ID, Name, Age, Course, and Email.

All records are stored in a local JSON file (`records.json`) so that the data persists between program runs.

## Features

* Menu-driven console interface
* Add a new student record with input validation
* View all student records in a formatted table
* Search records by ID or partial name
* Update existing student records
* Delete student records with confirmation
* Automatically save and load data using a JSON file
* Exception handling for invalid input and file-related errors
* Simple and user-friendly console interface

## Technologies / Concepts Used

* Python 3
* Variables and data types
* Lists and dictionaries
* Conditional statements
* `for` and `while` loops
* Functions
* Exception handling
* File handling
* JSON module
* Menu-driven application design

## Project Structure

```text
record-management-app/
├── record_management_app.py
├── records.json
├── README.md
├── Assignment1_Report.md
└── screenshots/
```

### File Description

* `record_management_app.py` – Main Python application
* `records.json` – Stores student records
* `README.md` – Project documentation
* `Assignment1_Report.md` – Assignment report
* `screenshots/` – Screenshots of the application

## How to Run the Application

### Step 1: Check Python Installation

Make sure Python 3 is installed on your computer.

```bash
python --version
```

or

```bash
python3 --version
```

### Step 2: Open the Project in VS Code

Open the project folder in Visual Studio Code.

### Step 3: Run the Application

Open the VS Code terminal and run:

```bash
python record_management_app.py
```

If your system uses `python3`, run:

```bash
python3 record_management_app.py
```

### Step 4: Use the Menu

The application will display a menu with the following options:

```text
==============================
   RECORD MANAGEMENT SYSTEM
==============================
1. Add Record
2. View All Records
3. Search Record
4. Update Record
5. Delete Record
6. Exit
==============================
```

Select the required option by entering a number from **1 to 6**.

## Sample Input / Output

```text
==============================
   RECORD MANAGEMENT SYSTEM
==============================
1. Add Record
2. View All Records
3. Search Record
4. Update Record
5. Delete Record
6. Exit
==============================
Enter your choice (1-6): 1

--- Add New Record ---
Enter name: Alice Sharma
Enter age: 21
Enter course: MCA
Enter email: alice@example.com

Record added successfully with ID 1.
```

### View Records

```text
--- All Records ---

ID   Name                Age   Course              Email
----------------------------------------------------------------
1    Alice Sharma        21    MCA                 alice@example.com
```

## Data Storage

The application stores records in the `records.json` file.

The JSON file is automatically created when required, and records are loaded when the application starts.

## Error Handling

The application handles common errors such as:

* Invalid user input
* Invalid age or ID values
* Missing data file
* Corrupted JSON data
* File permission errors

## Author

**Name:** Pushyal Poojari

**Course:** MCA Semester I

**Subject:** Python Programming & Relational Database

**Assignment:** Assignment 1 – Mini Project
