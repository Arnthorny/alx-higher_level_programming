#!/usr/bin/python3
"""
Python script to perform this task

Please list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”

You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)

API Endpoint: /repos/{owner}/{repo}/commits
"""
import requests
import sys

if __name__ == "__main__":

    arg = sys.argv[1:]
    param = {'per_page': 10}
    url = 'https://api.github.com/repos/{}/{}/commits'.format(arg[1], arg[0])

    r = requests.get(url, params=param)
    res_json = r.json()

    for o in res_json:
        print('{}: {}'.format(o.get('sha'),
                              o.get('commit', {})
                              .get('author', {})
                              .get('name')))
