#!/bin/bash
# A Script that takes in a URL as an argument, sends a GET request to the URL
curl -LsX GET "$1" -H "X-School-User-Id: 98"
