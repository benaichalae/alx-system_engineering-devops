#!/usr/bin/python3
"""Exports employee's tasks to a JSON file"""
import json
import requests
from sys import argv


def export_to_json(user_id, username, tasks):
    data = {user_id: [{
        "task": task['title'],
        "completed": task['completed'],
        "username": username
        } for task in tasks]}
    filename = "{}.json".format(user_id)
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
    print("JSON file '{}' has been created.".format(filename))


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
    else:
        employee_id = int(argv[1])

        user_response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                employee_id
                )
            )
        user_data = user_response.json()

        if 'id' not in user_data or 'username' not in user_data:
            print("Invalid user ID.")
        else:
            todo_response = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                    employee_id
                    )
                )
            todo_data = todo_response.json()

            export_to_json(employee_id, user_data['username'], todo_data)
