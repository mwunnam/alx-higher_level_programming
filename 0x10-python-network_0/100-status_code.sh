#!/bin/bash
# This is to make send a request and display only the status code
curl -so /dev/null -w "%{http_code}" "$1"
