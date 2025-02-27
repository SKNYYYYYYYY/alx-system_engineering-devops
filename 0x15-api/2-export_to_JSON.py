#!/usr/bin/python3
"""
Fetches user details and tasks from JSONPlaceholder API.
"""


import json
import requests
import sys


def get_user_details():
    """
    Fetches and prints an employee's completed tasks.
    Args:
        id (int): Employee ID.
    """
    url = "https://jsonplaceholder.typicode.com"
    response = requests.get("{}/users".format(url))
    if response.status_code == 200:
        data = response.json()
    employee = data[0]
    username = employee["username"]
    userId = employee["id"]
    # todo details
    params = {"userId": id}
    todos_response = requests.get(f"{url}/todos",params=params)
    if todos_response.status_code == 200:
        todos = todos_response.json()
        tasks = [{
            "username":username,
            "task":todo["title"],
            "completed":todo["completed"],
		}for todo in todos]
    json_data = {userId: tasks}

    filename = f"{userId}.json"
    with open(filename, "w") as json_file:
        json.dump(json_data, json_file, indent=4)
if __name__ == "__main__":
    id = int(sys.argv[1])
    get_user_details()
