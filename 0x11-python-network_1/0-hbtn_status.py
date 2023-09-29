#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as res:
        html = res.read()

        print('Body response:')
        print('    - type: {}'.format(type(html)))
        print('    - content: {}'.format(html))
        print('    - utf8 content: {}'.format(html.decode()))
