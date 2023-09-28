#!/bin/bash
#  script that takes in a URL as an argument, sends a GET
curl -sH "X-School-User-Id" "$1"
