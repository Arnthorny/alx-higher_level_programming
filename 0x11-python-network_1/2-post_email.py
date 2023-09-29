#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""

import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":

    args = sys.argv[1:]

    data = {'email': args[1]}
    enc_data = urllib.parse.urlencode(data)
    enc_data = enc_data.encode('utf-8')

    req = urllib.request.Request(args[0], data=enc_data)
    with urllib.request.urlopen(req) as res:
        html = res.read()
        print(html.decode())
