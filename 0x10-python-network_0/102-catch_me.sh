#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me that causes the server to respond
curl -sL 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin:You got me!"
