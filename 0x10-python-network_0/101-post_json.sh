#!/bin/bash
# Script that will send a JSON file
curl -s -X POST -d @"$2" "$1"
