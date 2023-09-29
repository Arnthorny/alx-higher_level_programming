#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import sys
from urllib.error import HTTPError


if __name__ == "__main__":

    args = sys.argv[1:]

    req = urllib.request.Request(args[0])
    try:
        with urllib.request.urlopen(req) as res:
            html = res.read()
            print(html.decode())
    except HTTPError as e:
        print("Error code: {}".format(e.code))
