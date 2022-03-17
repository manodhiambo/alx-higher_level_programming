#!/bin/bash
#A Script that takes in a URL, sends a POST request to the passed URL
curl -s "$1" -X POST -d 'email=hr@test@gmail.com&subject=I will always be here for PLD'
