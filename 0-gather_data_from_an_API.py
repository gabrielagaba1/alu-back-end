#!/usr/bin/python3
"""Gather an employee's completed TODO tasks from an API."""

import json
import sys
import urllib.request


def main():
    """Print an employee's TODO progress."""
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen(
        url + "/users/" + str(employee_id)
    ) as response:
        employee = json.loads(response.read().decode("utf-8"))

    with urllib.request.urlopen(
        url + "/todos?userId=" + str(employee_id)
    ) as response:
        tasks = json.loads(response.read().decode("utf-8"))

    completed = [task for task in tasks if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(tasks)))

    for task in completed:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
