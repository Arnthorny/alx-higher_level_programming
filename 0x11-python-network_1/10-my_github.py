#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    arg = sys.argv[1:]

    url = 'https://api.github.com/users/{}'.format(arg[0])
    auth = HTTPBasicAuth(arg[0], arg[1])

    r = requests.get(url, auth=auth)

    res_json = r.json()

    print(res_json['id'])
