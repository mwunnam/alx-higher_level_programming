#!/bin/bash
# This is to display all the methods accepted
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
