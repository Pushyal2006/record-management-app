import json
import os

FILE_NAME = "records.json"


def load_records():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data
            return []

    except (json.JSONDecodeError, OSError):
        print("Could not read the records file.")
        return []


def save_records(records):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(records, file, indent=4)
        return True

    except OSError:
        print("Could not save the records.")
        return False


def get_next_id(records):
    if len(records) == 0:
        return 1

    return max(record["id"] for record in records) + 1


def add_record(records):
    print("\n--- Add New Record ---")

    name = input("Enter name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    while True:
        try:
            age = int(input("Enter age: "))

            if age <= 0 or age > 120:
                print("Please enter a valid age.")
                continue

            break

        except ValueError:
            print("Please enter age as a number.")

    course = input("Enter course: ").strip()
    email = input("Enter email: ").strip()

    if course == "" or email == "":
        print("Course and email cannot be empty.")
        return

    record = {
        "id": get_next_id(records),
        "name": name,
        "age": age,
        "course": course,
        "email": email
    }

    records.append(record)

    if save_records(records):
        print("Record added successfully.")
        print("Record ID:", record["id"])
    else:
        records.pop()


def view_records(records):
    print("\n--- All Records ---")

    if len(records) == 0:
        print("No records found.")
        return

    print("-" * 80)
    print(f"{'ID':<5}{'Name':<20}{'Age':<8}{'Course':<20}{'Email':<25}")
    print("-" * 80)

    for record in records:
        print(
            f"{record['id']:<5}"
            f"{record['name']:<20}"
            f"{record['age']:<8}"
            f"{record['course']:<20}"
            f"{record['email']:<25}"
        )

    print("-" * 80)


def search_record(records):
    print("\n--- Search Record ---")
    print("1. Search by ID")
    print("2. Search by Name")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        try:
            record_id = int(input("Enter ID: "))

        except ValueError:
            print("ID must be a number.")
            return

        found = False

        for record in records:
            if record["id"] == record_id:
                print("\nRecord Found")
                print("ID:", record["id"])
                print("Name:", record["name"])
                print("Age:", record["age"])
                print("Course:", record["course"])
                print("Email:", record["email"])
                found = True
                break

        if not found:
            print("No record found.")

    elif choice == "2":
        name = input("Enter name to search: ").strip().lower()

        found = False

        for record in records:
            if name in record["name"].lower():
                print("\nID:", record["id"])
                print("Name:", record["name"])
                print("Age:", record["age"])
                print("Course:", record["course"])
                print("Email:", record["email"])
                print("-" * 30)
                found = True

        if not found:
            print("No matching record found.")

    else:
        print("Invalid choice.")


def update_record(records):
    print("\n--- Update Record ---")

    try:
        record_id = int(input("Enter ID of the record to update: "))

    except ValueError:
        print("ID must be a number.")
        return

    record = None

    for item in records:
        if item["id"] == record_id:
            record = item
            break

    if record is None:
        print("Record not found.")
        return

    print("\nLeave any field blank if you don't want to change it.")

    name = input(f"Name [{record['name']}]: ").strip()
    age = input(f"Age [{record['age']}]: ").strip()
    course = input(f"Course [{record['course']}]: ").strip()
    email = input(f"Email [{record['email']}]: ").strip()

    if name:
        record["name"] = name

    if age:
        try:
            new_age = int(age)

            if new_age > 0 and new_age <= 120:
                record["age"] = new_age
            else:
                print("Invalid age. Old age value kept.")

        except ValueError:
            print("Invalid age. Old age value kept.")

    if course:
        record["course"] = course

    if email:
        record["email"] = email

    if save_records(records):
        print("Record updated successfully.")


def delete_record(records):
    print("\n--- Delete Record ---")

    try:
        record_id = int(input("Enter ID of the record to delete: "))

    except ValueError:
        print("ID must be a number.")
        return

    record = None

    for item in records:
        if item["id"] == record_id:
            record = item
            break

    if record is None:
        print("Record not found.")
        return

    print("Record:", record["name"])

    confirm = input("Are you sure you want to delete this record? (y/n): ")

    if confirm.lower() != "y":
        print("Deletion cancelled.")
        return

    records.remove(record)

    if save_records(records):
        print("Record deleted successfully.")
    else:
        records.append(record)


def show_menu():
    print("\n==============================")
    print("   RECORD MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Record")
    print("2. View All Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")
    print("==============================")


def main():
    records = load_records()

    while True:
        show_menu()

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_record(records)

        elif choice == "2":
            view_records(records)

        elif choice == "3":
            search_record(records)

        elif choice == "4":
            update_record(records)

        elif choice == "5":
            delete_record(records)

        elif choice == "6":
            print("Thank you for using Record Management System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()