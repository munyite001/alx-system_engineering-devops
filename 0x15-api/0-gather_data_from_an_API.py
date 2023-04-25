#!/usr/bin/python3
"""
    Get's the data about an employee
    returns their todo list progress
"""
import requests
import sys

id = sys.argv[1]
user = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}').json()
name = user["name"]
tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
user_tasks = [task for task in tasks if int(task["userId"]) == int(id)]
completeTasks = [task for task in user_tasks if task["completed"]]
tasks = f"{len(completeTasks)}/{len(user_tasks)}"
print(f"Employee {name} is done with tasks({tasks}):")
for task in completeTasks:
    print(f"\t {task['title']}")
