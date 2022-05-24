#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""


def main():
    import requests
    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
if __name__ == "__main__":
    main()
