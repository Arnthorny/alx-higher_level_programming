#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first argument. curl v7.82.0 has a `--json` option.
curl -s --data @"$2" --header "Content-Type: application/json" "$1"
