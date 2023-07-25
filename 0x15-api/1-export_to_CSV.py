#!/usr/bin/python3
"""
Request from API; Return TODO list  given employee id
Export this data to CSV
"""
import sys
import requests
import csv

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = f"{base_url}/{employee_id}/todos"

    response = requests.get(todos_url)

    if response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        sys.exit(1)

    todos = response.json()
    employee_name = todos[0]["name"]
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo["completed"])

    return employee_name, completed_tasks, total_tasks, todos

def save_to_csv(employee_id, employee_name, todos):
    filename = f"{employee_id}.csv"

    with open(filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=",")
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos:
            task_completed_status = "True" if todo["completed"] else "False"
            csv_writer.writerow([employee_id, employee_name, task_completed_status, todo["title"]])

def display_todo_progress(employee_id):
    employee_name, completed_tasks, total_tasks, todos = get_employee_todo_progress(employee_id)

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for title in [todo["title"] for todo in todos if todo["completed"]]:
        print(f"\t{title}")

    save_to_csv(employee_id, employee_name, todos)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    display_todo_progress(employee_id)

