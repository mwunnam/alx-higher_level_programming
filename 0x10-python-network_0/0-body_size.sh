#!/bin/bash
# This is to get the content size
curl -s -w "%{size_download}" -o /dev/null "$1"
