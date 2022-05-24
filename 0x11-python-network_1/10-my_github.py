#!/usr/bin/python3
"""that takes in a letter and sends a POST request to"""


def main():
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"
    req = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2])).json()
    print(req.get("id"))
if __name__ == "__main__":
    main()
