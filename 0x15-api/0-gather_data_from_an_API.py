#!/usr/bin/python3
"""
Fetches user details and tasks from JSONPlaceholder API.
"""


import requests
import sys


if __name__ == "__main__":
    id = int(sys.argv[1])
    """
    Fetches and prints an employee's completed tasks.

    Args:
        id (int): Employee ID.
    """
    url = "https://jsonplaceholder.typicode.com"
    params = {"id": id}
    response = requests.get("{}/users".format(url), params={"id": id})
    if response.status_code == 200:
        data = response.json()
    employee = data[0]

# todo details
    todos_response = requests.get("{}/todos".format(url), params={"userId": id})
    if todos_response.status_code == 200:
        tasks = todos_response.json()
        done, total = 0, 0
        for dict in tasks:
            total += 1
            if dict['completed']:
                done += 1
    print("Employee {} is done with tasks({}/{}):".format(employee['name'], done, total))
    for dict in tasks:
        if dict["completed"]:
            print("\t", dict["title"])
