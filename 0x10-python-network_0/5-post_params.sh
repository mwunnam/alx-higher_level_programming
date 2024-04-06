#!/bin/bash
# This is to send email with subject using POST
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$!"
