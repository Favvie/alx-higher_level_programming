#!/bin/bash
# bash script
curl -sI -o /dev/null -w "%{http_code}" "$1"
