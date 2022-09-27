#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests
if __name__ == "__main__":
    params = {'q': ""}
    if len(sys.argv) != 1:
        params["q"] = sys.argv[1]

    response = requests.get('http://0.0.0.0:5000/search_user', params=params)
    try:
        data = response.json()
        if data:
            print(f"{data.get('id')}, {data.get('name')}")
        else:
            print('No result')
    except:
        print('Not a valid JSON')
