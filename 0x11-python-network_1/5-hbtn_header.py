#!/usr/bin/python3
"""sends a request to the URL and displays the value of the variable"""


def main():
    import requests
    from sys import argv
    req = requests.get(argv[1])
    print(req.headers.get("X-Request-Id"))
if __name__ == "__main__":
    main()
