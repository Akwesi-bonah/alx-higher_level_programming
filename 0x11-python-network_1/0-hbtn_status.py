#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request as url
if __name__ == "__main__":

    with url.urlopen('https://alx-intranet.hbtn.io/status') as re:
        content = re.read()

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
