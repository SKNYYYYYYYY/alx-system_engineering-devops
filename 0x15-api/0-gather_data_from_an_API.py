#!/usr/bin/python3
"""
Fetches user details and tasks from JSONPlaceholder API.
"""


import requests
import sys


def get_data(id):
    """
    Fetches and prints an employee's completed tasks.

    Args:
        id (int): Employee ID.
    """
    url = "https://jsonplaceholder.typicode.com"
    params = {"id": id}
    response = requests.get(f"{url}/users", params=params)
    if response.status_code == 200:
        data = response.json()
    employee = data[0]

# todo details
    todos_response = requests.get(f"{url}/todos", params={"userId": id})
    if todos_response.status_code == 200:
        tasks = todos_response.json()
        done, total = 0, 0
        for dict in tasks:
            total += 1
            if dict['completed']:
                done += 1
    print(f"Employee {employee['name']} is done with tasks({done}/{total}):")
    for dict in tasks:
        if dict["completed"]:
            print("\t", dict["title"])


if __name__ == "__main__":
    args = int(sys.argv[1])
    get_data(args)
