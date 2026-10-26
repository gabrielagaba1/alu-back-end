#!/usr/bin/python3
"""Export an employee's TODO tasks to JSON."""

import json
import sys
import urllib.request


def main():
    """Export all tasks belonging to the specified employee."""
    user_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen(
        base_url + "/users/" + str(user_id)
    ) as response:
        employee = json.loads(response.read().decode("utf-8"))

    with urllib.request.urlopen(
        base_url + "/todos?userId=" + str(user_id)
    ) as response:
        tasks = json.loads(response.read().decode("utf-8"))

    data = {
        str(user_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee.get("username")
            }
            for task in tasks
        ]
    }

    with open(str(user_id) + ".json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    main()
