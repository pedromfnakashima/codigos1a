# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 08:07:59 2020

@author: pedro-salj

https://realpython.com/api-integration-in-python/
"""

#pip install requests


import requests

resp = requests.get('https://todolist.example.com/tasks/')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))






















































