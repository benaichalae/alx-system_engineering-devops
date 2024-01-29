#!/usr/bin/python3
"""Gathers data from an API"""
import requests
from sys import argv


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
        employee_name = user_data.get('name')

        todo_response = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                    employee_id
                    )
                )
        todo_data = todo_response.json()

        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task['completed'])

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, completed_tasks, total_tasks
            ))
        for task in todo_data:
            if task['completed']:
                print("\t {}".format(task['title']))
