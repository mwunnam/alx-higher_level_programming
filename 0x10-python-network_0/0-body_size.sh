#!/bin/bash
# This is to get the content size
echo "$(curl -s -w "%{size_download}" -o /dev/null "$1")"
