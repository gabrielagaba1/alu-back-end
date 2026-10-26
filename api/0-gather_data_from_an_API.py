#!/usr/bin/python3
"""Gather an employee's completed TODO tasks from a REST API."""

import json
import sys
import urllib.request


def main():
    """Display an employee's TODO progress."""
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen(
        base_url + "/users/" + str(employee_id)
    ) as response:
        employee = json.loads(response.read().decode("utf-8"))

    with urllib.request.urlopen(
        base_url + "/todos?userId=" + str(employee_id)
    ) as response:
        tasks = json.loads(response.read().decode("utf-8"))

    completed_tasks = [
        task for task in tasks if task.get("completed") is True
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee.get("name"),
            len(completed_tasks),
            len(tasks)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
