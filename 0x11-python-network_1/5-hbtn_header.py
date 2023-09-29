#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL,
displays the value of the variable
X-Request-Id in the response header
"""

if __name__ == "__main__":
    import requests as re
    import sys

    url = sys.argv[1]

    request = re.get(url)
    print(request.headers.get('X-Request-Id'))
