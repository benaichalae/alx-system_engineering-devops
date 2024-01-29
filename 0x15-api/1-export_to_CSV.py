#!/usr/bin/python3
""" Contains a Python script that,
using the JSONPlaceholder API,
exports TODO list data to a CSV file."""
import csv
import requests
from sys import argv


def export_to_csv(user_id, username, tasks):
    filename = "{}.csv".format(user_id)
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
                )
        for task in tasks:
            csv_writer.writerow(
                    [user_id, username, task['completed'], task['title']]
                    )
    print("CSV file '{}' has been created.".format(filename))


if __name__ == '__main__':
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <user_id>".format(argv[0]))
    else:
        user_id = argv[1]

        user_response = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}'.format(
                    user_id
                    )
                )
        user_data = user_response.json()

        if 'id' not in user_data or 'username' not in user_data:
            print("Invalid user ID.")
        else:
            todo_response = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                    user_id
                    )
                )
            todo_data = todo_response.json()

            export_to_csv(user_id, user_data['username'], todo_data)
