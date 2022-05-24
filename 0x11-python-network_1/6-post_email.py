#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""


def main():
    import requests
    from sys import argv
    req = requests.post(argv[1], {"email": argv[2]})
    print(req.text)
if __name__ == "__main__":
    main()
