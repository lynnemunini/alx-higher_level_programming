#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
echo "$1"
curl -H --data "$1"
