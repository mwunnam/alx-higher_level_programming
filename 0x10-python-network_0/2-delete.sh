#!/bin/bash
# A script that sends a DELETE request
curl -s -X DELETE "$1" && echo "I'm a DELETED request"
