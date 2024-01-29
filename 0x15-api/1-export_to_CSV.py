#!/usr/bin/python3
""" Contains a python script that, using the JSONplaceholder"""
import csv
import requests
from sys import argv


def export_to_csv(employee_id, user_data, todo_data):
    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
                )

        for task in todo_data:
            csv_writer.writerow(
                    [employee_id, user_data['id'], user_data['username'],
                        str(task['completed']), task['title']]
                    )

    print("CSV file '{}' has been created.".format(filename))


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
    else:
        employee_id = argv[1]

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

            export_to_csv(employee_id, user_data, todo_data)
