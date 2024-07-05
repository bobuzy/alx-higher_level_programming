#!/bin/bash
# Display only status code of the URL passed
curl -s -o /dev/null -w  "%{http_code}" "${1}"
