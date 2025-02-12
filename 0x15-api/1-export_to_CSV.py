#!/usr/bin/python3
"""
Fetches user details and tasks from JSONPlaceholder API.
"""


import requests
import sys


def get_user_details(id):
    """
    Fetches and prints an employee's completed tasks.
    Args:
        id (int): Employee ID.
    """
    url = "https://jsonplaceholder.typicode.com"
    response = requests.get("{}/users".format(url), params={"id": id})
    if response.status_code == 200:
        data = response.json()
    employee = data[0]
    # todo details
    todos_response = requests.get(
        "{}/todos".format(url),
        params={
            "userId": id})
    if todos_response.status_code == 200:
        tasks = todos_response.json()
    for dict in tasks:
        csv = []
        for item, value in dict.items():
            if item == "userId":
                csv.append(value)
            if item == "completed":
                csv.append(value)
            if item == "title":
                csv.append(value)
        csv.insert(1, employee["username"])
        csv[2], csv[3] = csv[3], csv[2]
        formatted = ",".join(f'"{item}"' for item in csv)
        filename = str(id) + ".csv"
        with open(filename, "a") as f:
            f.write(formatted)
            f.write("\n")


if __name__ == "__main__":
    id = int(sys.argv[1])
    get_user_details(id)
