#!/bin/bash
# Write a Bash script that takes in a URL as an argument, sends a GET
curl -sX GET "$1" -H "X-HolbertonSchool-User-Id: 98"
