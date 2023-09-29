#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests as re

    request = re.get('https://alx-intranet.hbtn.io/status')
    print("Body response")
    print(f'\t - type: {type(request.text)}')
    print(f'\t - content: {request.text}')