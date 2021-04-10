#!/usr/bin/python3
'''
Write a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
'''

import sys
from urllib import request, parse


if __name__ == '__main__':

    url = sys.argv[1]
    # Data dictionary
    value = {'email': sys.argv[2]}

    data = parse.urlencode(value).encode('ascii')

    # if data != null reference to method POST
    with request.urlopen(url, data=data) as response:
        print(response.read().decode('utf8'))
