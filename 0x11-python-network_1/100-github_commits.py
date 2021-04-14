#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge
"""


import requests
import sys


if __name__ == "__main__":
    repository = sys.argv[1]
    repo_owner = sys.argv[2]
    req = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(repo_owner, repository))
    json_response = req.json()

    counter = 0

    if json_response:
        for i in range(0, len(json_response)):
            if counter < 10:
                print("{}: {}".format(json_response[i].get("sha"),
                                      json_response[i].get("commit")
                                      .get("author").get("name")))
                counter += 1
