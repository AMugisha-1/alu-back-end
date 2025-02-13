#!/usr/bin/python3
"""Module to fetch user task completion details"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    # Fetch user information
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Invalid user ID or failed API request.")
        sys.exit(1)

    user_info = user_response.json()
    todos_info = todos_response.json()

    employee_name = user_info.get("name", "Unknown")
    task_completed = [task for task in todos_info if task.get("completed")]

    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    print(
        f"Employee {employee_name} is done with tasks({number_of_done_tasks}/"
        f"{total_number_of_tasks}):"
    )

    for task in task_completed:
        print(f"\t {task['title']}")

