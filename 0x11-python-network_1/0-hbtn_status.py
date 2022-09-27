#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
            as response:
        data = response.read()
        print(f"Body response:\n\t- type: {type(data)}")
        print(f"\t- content: {data}")
        print(f"\t- utf8 content: {data.decode('utf-8')}")
