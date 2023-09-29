#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found
in the header of the response.
"""

import urllib.request
import sys


if __name__ == "__main__":

    args = sys.argv[1:]

    req = urllib.request.Request(args[0])
    with urllib.request.urlopen(req) as res:
        hdr_dict = res.info()
        print(hdr_dict['X-Request-Id'])
