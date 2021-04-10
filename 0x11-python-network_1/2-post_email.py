#!/usr/bin/python3
'''
Write a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
'''

import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    try:
        url = sys.argv[1]
        # Data dictionary
        value = {'email': sys.argv[2]}

        data = parse.urlencode(value).encode('utf8')

        # if data != null reference to method POST
        with request.urlopen(url, data) as response:
            print(response.read().decode('utf8'))
        print('Your email is: '.format(sys.argv[2]))
    except:
        pass
