#!/usr/bin/python3
"""Export all employees' TODO tasks to JSON."""

import json
import urllib.request


def main():
    """Export every employee's tasks."""
    url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen(url + "/users") as response:
        employees = json.loads(response.read().decode("utf-8"))

    with urllib.request.urlopen(url + "/todos") as response:
        tasks = json.loads(response.read().decode("utf-8"))

    data = {}
    usernames = {}

    for employee in employees:
        usernames[employee.get("id")] = employee.get("username")
        data[str(employee.get("id"))] = []

    for task in tasks:
        user_id = task.get("userId")
        data[str(user_id)].append({
            "username": usernames.get(user_id),
            "task": task.get("title"),
            "completed": task.get("completed")
        })

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    main()
