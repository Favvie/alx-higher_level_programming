#!/bin/bash
# print the allowed methods
curl -sI "$1" | awk '/Allow/ {$1=""; print substr($0, 2)}'
