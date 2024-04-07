#!/bin/bash
# This is to make a request to a server that cause a respose You got me!
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin:HolbertonSchool"
