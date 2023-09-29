#!/usr/bin/python3
"""
script that takes in a URL:
  sends a request to the URL
  displays the value of the X-Request-Id
    found in the header of the response.
"""

if __name__ == "__main__":
    import sys
    from urllib import request as re

    url = sys.argv[1]

    request = re.Request(url)
    with re.urlopen(request) as response:
        print(dict(response.headers).get('X-Request-Id'))
