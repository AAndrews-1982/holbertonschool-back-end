#!/usr/bin/python3

import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://example.com/api/employees"  # Replace with the actual API endpoint URL

    # Get employee information
    employee_url = f"{base_url}/{employee_id}"
    response = requests.get(employee_url)

    if response.status_code != 200:
        print("Failed to fetch employee information.")
        return

    employee_data = response.json()
    employee_name = employee_data["name"]

    # Get employee tasks
    tasks_url = f"{base_url}/{employee_id}/tasks"
    response = requests.get(tasks_url)

    if response.status_code != 200:
        print(f"Failed to fetch tasks for Employee {employee_name}.")
        return

    tasks_data = response.json()
    total_tasks = len(tasks_data)
    completed_tasks = [task for task in tasks_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)

    # Print the employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")

    # Print the titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)

