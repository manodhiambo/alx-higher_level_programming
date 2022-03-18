#!/usr/bin/python3
""" Program that fetches an URL """
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        body_page = response.read()
        body_decoded = body_page.decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(body_page)))
        print("\t- content: {}".format(body_page))
        print("\t- utf8 content: {}".format(body_decoded))
