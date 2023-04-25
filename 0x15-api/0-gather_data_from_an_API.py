#!/usr/bin/python3
"""
    Get's the data about an employee
    returns their todo list progress
"""
import requests, sys

user = requests.get(f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}').json()
name = user["name"]
tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
user_tasks = [task for task in tasks if int(task["userId"]) == int(sys.argv[1])]
completeTasks = [task for task in user_tasks if task["completed"]]
print(f"Employee {name} is done with tasks({len(completeTasks)}/{len(user_tasks)}):")
for task in completeTasks:
    print(f"\t{task['title']}")
