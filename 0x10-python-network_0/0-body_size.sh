#!/usr/bin/bash
# display size of response body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
