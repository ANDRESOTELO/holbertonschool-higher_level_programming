# Python - Network #1

## Fetch Internet Resources Using The urllib Package
urllib.request is a Python module for fetching URLs (Uniform Resource Locators). It offers a very simple interface, in the form of the urlopen function. This is capable of fetching URLs using a variety of different protocols. It also offers a slightly more complex interface for handling common situations - like basic authentication, cookies, proxies and so on. These are provided by objects called handlers and openers.

## Fetching URLs
The simplest way to use urllib.request is as follows:
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()

## Author
Andrés Sotelo - Holberton School Colombia
2021
