# Assignment 1 – Mini Project Report
## Console Record-Management Application

**Course:** MCA Semester I – Python Programming & Relational Database
**Student Name:** <your name>
**Roll No / ID:** <your roll number>
**Date:** <submission date>

---

## 1. Objective

To design and develop a fully working, menu-driven console application in
Python that manages records (add, view, search, update, delete), while
demonstrating core Python programming concepts: data types, conditionals,
loops, functions, exception handling, and file I/O.

## 2. Problem Statement

Organizations often need a simple way to store and manage small sets of
records without a full database system. This project implements a
lightweight record-management system that runs entirely in the console and
persists data to a file, so records are not lost when the program closes.

## 3. Tools & Technologies

| Tool/Technology | Purpose |
|---|---|
| Python 3 | Programming language |
| `json` module | File storage format for records |
| `os` module | Checking file existence |
| VS Code | Development environment |
| Git & GitHub | Version control and submission |

## 4. System Design

### 4.1 Data Structure

Each record is represented as a Python dictionary:

```python
{
    "id": 1,
    "name": "Alice Sharma",
    "age": 21,
    "course": "MCA",
    "email": "alice@example.com"
}
```

All records are held in memory as a `list` of such dictionaries while the
program runs, and are serialized to `records.json` on every change.

### 4.2 Module/Function Breakdown

| Function | Responsibility |
|---|---|
| `load_records()` | Reads records from `records.json` at startup |
| `save_records(records)` | Writes the current record list to disk |
| `get_non_empty_input()` | Validates that required text fields aren't blank |
| `get_valid_age()` | Validates that age is a realistic whole number |
| `get_next_id()` | Auto-generates the next sequential record ID |
| `find_record_by_id()` | Looks up a record by ID |
| `add_record()` | Collects input and appends a new record |
| `view_records()` | Displays all records in a table |
| `search_record()` | Searches by ID or partial name |
| `update_record()` | Edits fields of an existing record |
| `delete_record()` | Removes a record after confirmation |
| `display_menu()` | Prints the menu options |
| `main()` | Runs the menu loop and dispatches to the functions above |

### 4.3 Menu Flow

```
1. Add Record        -> add_record()
2. View All Records   -> view_records()
3. Search Record      -> search_record()
4. Update Record      -> update_record()
5. Delete Record      -> delete_record()
6. Exit                -> break out of the main loop
```

## 5. Python Concepts Demonstrated

- **Data Types & Variables:** strings (name, course, email), integers
  (id, age), dictionaries (a record), lists (all records).
- **Conditional Statements:** `if`/`elif`/`else` used for menu dispatch,
  input validation, and search-mode selection.
- **Loops:** a `while True` loop drives the menu until the user exits;
  `for` loops iterate over records for display and search.
- **Functions:** every operation is isolated in its own function with a
  single responsibility, instead of one large script.
- **Exception Handling:** `try`/`except` blocks catch `ValueError` (bad
  numeric input), `json.JSONDecodeError` (corrupted data file),
  `PermissionError` and `OSError` (file access problems), plus a
  top-level catch-all in `main()` so no unexpected error can crash the
  program mid-session.
- **File I/O:** records are read from and written to `records.json`
  using the `json` module, so data persists across runs.
- **Menu-Driven Design:** a single `main()` loop presents a numbered
  menu and routes the user's choice to the matching function.

## 6. Testing

The application was manually tested for the following scenarios:

| Test Case | Expected Result | Result |
|---|---|---|
| Add a record with valid data | Record saved, confirmation shown | Pass |
| Add a record with blank name | Re-prompted until valid input given | Pass |
| Add a record with non-numeric age | Re-prompted until valid number given | Pass |
| View records with no data | "No records found" message | Pass |
| Search by existing ID | Matching record displayed | Pass |
| Search by non-existing ID | "No matching record found" | Pass |
| Search by partial name | All matching records displayed | Pass |
| Update a record, leave fields blank | Existing values retained | Pass |
| Delete a record, confirm with 'y' | Record removed and saved | Pass |
| Delete a record, cancel with 'n' | Record kept, no changes made | Pass |
| Restart the program | Previously saved records reload correctly | Pass |
| Corrupt/missing `records.json` | Program starts with empty list, no crash | Pass |

Screenshots of these test runs are included in the `screenshots/` folder.

## 7. Conclusion

This project successfully implements a menu-driven console application
that integrates data structures, control flow, functions, exception
handling, and file-based persistence into one working program. The
application handles invalid input and file errors gracefully, meeting all
requirements specified in the assignment brief.

## 8. GitHub Repository

Repository link: `<paste your GitHub repository URL here>`
