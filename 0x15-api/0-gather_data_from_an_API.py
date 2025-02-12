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
    total = len([i['title'] for i in tasks])
    done = [i["title"] for i in tasks if i["completed"]]
    len_done = len(done)
    print(f"Employee {employee['name']} is done with tasks({len_done}/{total}):")
    print("\t " + "\n\t ".join(done),)


if __name__ == "__main__":
    id = int(sys.argv[1])
    get_user_details(id)
