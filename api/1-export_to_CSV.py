#!/usr/bin/python3
"""Export an employee's TODO tasks to CSV."""

import csv
import json
import sys
import urllib.request


def main():
    """Export all tasks for the given employee."""
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

    with open(str(user_id) + ".csv", "w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([
                user_id,
                employee.get("username"),
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    main()
