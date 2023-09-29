#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends a POST request to
passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":

    args = sys.argv[1:]

    data_post = {'email': args[1]}
    r = requests.post(args[0], data=data_post)
    print(r.text)
