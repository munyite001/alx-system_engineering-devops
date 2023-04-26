#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
"""
import requests
import sys


api = "https://jsonplaceholder.typicode.com"
"""json place holder REST API """

if __name__ == '__main__':
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        employee = requests.get(f'{api}/users/{id}').json()
        name = employee.get('name')

        tasks = requests.get(f'{api}/todos').json()
        empTasks = list(filter(lambda x: x.get('userId') == id, tasks))

        complete = list(filter(lambda x: x.get('completed'), empTasks))

        numC = len(complete)
        numT = len(empTasks)
        print(f'Employee {name} is done with tasks({numC}/{numT}):')

        for task in complete:
            print(f'\t {task.get("title")}')
