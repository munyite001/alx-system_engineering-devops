#!/usr/bin/python3
"""
    Get's the data about an employee
    returns their todo list progress
"""
if __name__ == "__main__":
    import requests
    import sys

    id = sys.argv[1]
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    user = user.json()
    name = user.get("name")
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    user_tasks = []
    for task in tasks:
        if task.get("userId") == int(id):
            user_tasks.append(task)

    completeTasks = []
    for task in user_tasks:
        if task.get("completed") is True:
            completeTasks.append(task)
    tasks = f"{len(completeTasks)}/{len(user_tasks)}"
    print(f"Employee {name} is done with tasks({tasks}):")
    for task in completeTasks:
        print(f"\t {task['title']}")
