#!/bin/bash
# script that takes in a URL, sends a request to that URL,
curl -so /dev/null "$1" -w '%{size_download}\n'
