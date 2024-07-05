#!/bin/bash
# Count the number of bytes from fetched contents from the URL passed
curl -s  "${1}" | wc -c
