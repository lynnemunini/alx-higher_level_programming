#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests
if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    response = requests.post('http://0.0.0.0:5000/search_user', data={"q": q})
    try:
        data = response.json()
        if data:
            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
