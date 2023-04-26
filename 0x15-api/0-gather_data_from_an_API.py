#!/usr/bin/python3
"""
    Get's the data about an employee
    returns their todo list progress
"""

import requests
import sys

api = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    try:
        id = int(sys.argv[1])
    except:
        print("Invalid argument")
        sys.exit()
    user = requests.get(f'{api}/users/{id}').json()
    name = user.get("name")
    tasks = requests.get(f"{api}/todos").json()
    user_tasks = [filter(lambda t: t.get("userId") == id, tasks)]
    complete = [filter(lambda t: t.get("completed"), user_tasks)]
    tasks = f"{len(complete)}/{len(user_tasks)}"
    print(f"Employee {name} is done with tasks({tasks}):")
    for task in complete:
        print(f"\t {task['title']}")
