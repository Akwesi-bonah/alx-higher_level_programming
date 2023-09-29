#!/usr/bin/python3
"""
cript that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request as url
if __name__ == "__main__":

    with url.urlopen('https://alx-intranet.hbtn.io/status') as re:
        content = re.read()

        print("Body response:")
        print(f'\t - type: {type(content)}')
        print(f'\t - content: {content}')
        print(f'\t - utf-8 content: {content.decode("utf-8")}')
