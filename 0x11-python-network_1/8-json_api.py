#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import requests.exceptions
import sys


if __name__ == "__main__":

    args = sys.argv[1:]
    letter = '' if len(args) == 0 else args[0]
    url = 'http://0.0.0.0:5000/search_user'

    data_post = {'q': letter}
    r = requests.post(url, data=data_post)
    try:
        res_json = r.json()
        if len(res_json) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(res_json.get('id'), res_json.get('name')))
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
