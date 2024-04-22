#!/usr/bin/python3
"""
Script that uses JSONPlaceholder API to get information about ALL employees
and exports their TODO lists to a single JSON file
"""

import json
import requests
import sys


def get_all_employees_and_tasks():
    """
    Fetches information about all employees and their tasks from
    JSONPlaceholder API
    """
    api_url = 'https://jsonplaceholder.typicode.com/'

    users_url = '{}users'.format(api_url)
    users_response = requests.get(users_url)
    users_data = users_response.json()

    all_employees_tasks = {}

    for user in users_data:
        name = user.get('username')
        userid = user.get('id')

        todos_url = '{}todos?userId={}'.format(api_url, userid)
        todos_response = requests.get(todos_url)
        tasks_data = todos_response.json()

        tasks_list = []

        for task in tasks_data:
            dict_task = {
                "username": name,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            tasks_list.append(dict_task)

        all_employees_tasks[str(userid)] = tasks_list

    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as json_file:
        json.dump(all_employees_tasks, json_file)


if __name__ == "__main__":
    get_all_employees_and_tasks()
