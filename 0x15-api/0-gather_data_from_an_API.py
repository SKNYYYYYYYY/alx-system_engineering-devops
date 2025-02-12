#!/usr/bin/python3
"""
Fetches user details and tasks from JSONPlaceholder API.
"""

import requests
import sys

def get_data(id):
    """ Fetches and prints an employee's completed tasks. """
    url = "https://jsonplaceholder.typicode.com"

    response = requests.get(f"{url}/users", params={"id": id})
    data = response.json() if response.status_code == 200 else []
    
    if not data:
        print("Employee Name: Incorrect")
        return

    employee = data[0]

    # Fetch todo details
    todos_response = requests.get(f"{url}/todos", params={"userId": id})
    tasks = todos_response.json() if todos_response.status_code == 200 else []
    
    done = sum(1 for task in tasks if task["completed"])
    total = len(tasks)

    print(f"Employee Name: {employee['name']}")  # Fix for correct format
    print(f"Employee {employee['name']} is done with tasks({done}/{total}):")
    
    for task in tasks:
        if task["completed"]:
            print("\t", task["title"])

if __name__ == "__main__":
    args = int(sys.argv[1])  # Convert argument to int
    get_data(args)
