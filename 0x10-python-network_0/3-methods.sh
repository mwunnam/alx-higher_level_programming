#!/bin/bash
# This is to display all the methods accepted
curl -I "$1" | grep -v "Allow:"
