#!/bin/bash
# Write a Bash script that takes in a URL as an argument, sends a GET
curl -sX GET "$1" -H "X-School-User-Id: 98"
