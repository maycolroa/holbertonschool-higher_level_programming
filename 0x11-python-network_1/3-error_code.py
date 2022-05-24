#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""


def main():
    import urllib.request
    from sys import argv
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode("UTF-8"))

    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.status))


if __name__ == "__main__":
    main()
