#!/bin/bash
# Count the number of bytes from fetched contents
curl -s  "${1}" | wc -c
