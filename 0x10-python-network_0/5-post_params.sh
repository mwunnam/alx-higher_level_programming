#!/bin/bash
# This is to send email with subject using POST
curl -X POST -s -H "email: test@gmail.com" -H "subject: I will always be here for PLD" "$!"
