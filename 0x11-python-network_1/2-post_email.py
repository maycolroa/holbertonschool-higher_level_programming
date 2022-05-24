#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""


def main():
    import urllib.request
    from sys import argv

    url = argv[1]
    data = urllib.parse.urlencode({"email": argv[2]})
    data = data.encode("ascii")
    post = urllib.request.Request(url, data)
    with urllib.request.urlopen(post) as response:
        print(response.read().decode("UTF-8"))
if __name__ == "__main__":
    main()
