#!/usr/bin/python3

"""
A python Script that uses JSONPlaceholder API to get
information about an employee
and exports TODO list to CSV.
"""


import csv
import requests
import sys


def get_employee_info_and_tasks(employee_id):
    """
    Fetches information about an employee and their tasks from
    JSONPlaceholder API
    """
    api_url = 'https://jsonplaceholder.typicode.com/'

    user_url = '{}users/{}'.format(api_url, employee_id)
    todos_url = '{}todos?userId={}'.format(api_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()

    username = user_data.get('username')

    todos_response = requests.get(todos_url)
    tasks_data = todos_response.json()

    tasks_list = []
    for task in tasks_data:
        tasks_list.append(
            [employee_id, username, task.get('completed'), task.get('title')])

    filename = '{}.csv'.format(employee_id)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(
            employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        for task in tasks_list:
            employee_writer.writerow(task)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    get_employee_info_and_tasks(employee_id)
