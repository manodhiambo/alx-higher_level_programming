#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument
curl -H "Content-Type: application/json" -LsX POST "$1" -d "@$2"
