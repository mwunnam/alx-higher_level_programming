#!/bin/bash
# This is to use GET request to URL and displays body of the response with http
resp=$(curl -s -w "%{http_code}" "$1") && [ "$resp" == "200" ] && echo "$resp"
