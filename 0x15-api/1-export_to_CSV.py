#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
Export this data to CSV
"""
import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data['name']
        file_name = f'{employee_id}.csv'

        with open(file_name, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for todo in todos_data:
                writer.writerow(
                    [user_data['id'], user_data['username'], todo['completed'], todo['title']])

        print(
            f'Employee {employee_name} TODO list progress has been exported to {file_name}.')

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
    except (KeyError, IndexError) as e:
        print(f"Error: Invalid employee ID or data format. Please check the employee ID.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
