#!/usr/bin/python3
"""Write a Python script that fetches"""


def main():
    import urllib.request
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("UTF-8")))
if __name__ == "__main__":
    main()
