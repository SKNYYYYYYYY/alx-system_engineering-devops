#!/usr/bin/python3
import requests
import json


def get_data(id):
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
        done_tasks, total_tasks = 0, 0
        for dict in tasks:
            total_tasks += 1
            if dict['completed']:
                done_tasks += 1
    print(
        f"Employee {
            employee['name']} is done with tasks({done_tasks}/{total_tasks}):")
    for dict in tasks:
        if dict["completed"]:
            print("    ", dict["title"])


if __name__ == "__main__":
    get_data(2)
