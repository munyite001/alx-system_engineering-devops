#!/usr/bin/python3

"""
Retrieves data from https://jsonplaceholder.typicode.com API and exports it
to CSV file using recursion.
"""

import re
import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) == 2 and re.match(r'\d+', sys.argv[1]):
        user_id = int(sys.argv[1])
        user_data = requests.get(
            f"{API_URL}/users/{user_id}"
        ).json()
        todos_data = requests.get(
            f"{API_URL}/todos"
        ).json()
        user_name = user_data.get('username')
        user_todos = list(
            filter(lambda todo: todo.get('userId') == user_id, todos_data)
        )
        with open(f"{user_id}.csv", 'w') as file:
            for todo in user_todos:
                file.write(
                    f'"{user_id}","{user_name}","{todo.get("completed")}",'
                    f'"{todo.get("title")}"\n'
                )
