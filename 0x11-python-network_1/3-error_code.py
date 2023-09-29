#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL
displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    from urllib import request as re, error as er

    try:
        url = sys.argv[1]
        with re.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except er.HTTPError as e:
        print("Error code:", e.code)
