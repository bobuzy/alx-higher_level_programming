#!/bin/bash
# Send POST request to the URL passed
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
