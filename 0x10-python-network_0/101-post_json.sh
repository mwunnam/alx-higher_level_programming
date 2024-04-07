#!/bin/bash
# Script that will send a JSON file
curl -s -X POST -H "Content-type: application/json"  -d "@$2" "$1"
