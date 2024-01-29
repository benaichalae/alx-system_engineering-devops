#!/usr/bin/python3
"""
Contains a Python script that, using the JSONplaceholder API,
for a given employee ID, returns all tasks from all employees, in JSON format
"""
import json
import requests
from sys import argv


def fetch_user_data():
    return requests.get('https://jsonplaceholder.typicode.com/users').json()


def fetch_all_tasks():
    return requests.get('https://jsonplaceholder.typicode.com/todos/').json()


def create_employee_tasks_dict(users_data):
    employee_tasks_dict = {}
    username_dict = {}

    for user in users_data:
        employee_id = user.get("id")
        employee_tasks_dict[employee_id] = []
        username_dict[employee_id] = user.get('username')

    return employee_tasks_dict, username_dict


def populate_tasks_dict(employee_tasks_dict, username_dict, all_tasks):
    for task in all_tasks:
        task_details = {}
        employee_id = task.get('userId')
        task_details["task"] = task.get('title')
        task_details["completed"] = task.get('completed')
        task_details["username"] = username_dict.get(employee_id)
        employee_tasks_dict.get(employee_id).append(task_details)


def write_to_json_file(employee_tasks_dict):
    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(employee_tasks_dict, json_file)


if __name__ == '__main__':
    users_data = fetch_user_data()
    all_tasks = fetch_all_tasks()

    employee_tasks_dict, username_dict = create_employee_tasks_dict(users_data)

    populate_tasks_dict(employee_tasks_dict, username_dict, all_tasks)

    write_to_json_file(employee_tasks_dict)
