#!/usr/bin/python3
"""
request from api; return todo list for the given employee id
export to csv
"""
import csv
import requests
import sys


if __name__ == "__main__":
    root = "https://jsonplaceholder.typicode.com"

        userid = sys.argv[1]
    user = '{}users/{}'.format(root, userid)
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = '{}todos?userId={}'.format(root, userid)
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        l_task.append([userid,
                       name,
                       task.get('completed'),
                       task.get('title')])

    filename = '{}.csv'.format(userid)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in l_task:
            employee_writer.writerow(task)
