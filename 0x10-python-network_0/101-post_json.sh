#!/bin/bash
# Send a post request passing a JSON file
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "${1}"
