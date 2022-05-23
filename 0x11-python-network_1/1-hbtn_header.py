#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""

if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    with request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))
