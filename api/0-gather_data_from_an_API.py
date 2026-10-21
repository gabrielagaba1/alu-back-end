#!/usr/bin/python3
"""Gather employee task information from a REST API."""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    try:
        user_response = requests.get(
            "{}/users/{}".format(base_url, employee_id),
            timeout=20
        )
        if user_response.status_code != 200:
            sys.exit(1)

        user = user_response.json()
        if not isinstance(user, dict) or "id" not in user:
            sys.exit(1)

        tasks_response = requests.get(
            "{}/todos".format(base_url),
            params={"userId": employee_id},
            timeout=20
        )
        tasks_response.raise_for_status()
        tasks = tasks_response.json()

        if not isinstance(tasks, list):
            sys.exit(1)

        completed_tasks = [
            task for task in tasks if task.get("completed") is True
        ]

        print(
            "Employee {} is done with tasks({}/{}):".format(
                user["name"], len(completed_tasks), len(tasks)
            )
        )

        for task in completed_tasks:
            print("\t {}".format(task["title"]))

    except (requests.RequestException, ValueError, KeyError) as error:
        print("Error: {}".format(error), file=sys.stderr)
        sys.exit(1)
