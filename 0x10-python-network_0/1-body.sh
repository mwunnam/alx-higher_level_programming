#!/bin/bash
# This is to use GET request to URL and displays body of the response with http
curl -s -w "%{http_code}" -o /dev/null -I "$1"
