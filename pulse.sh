#!/usr/bin/env bash
git log --oneline | wc -l > pulse.txt
curl -s "http://worldclockapi.com/api/json/utc/now" \
  | sed -n 's/.*"currentDateTime":"\([^"]*\)".*/\1\n/p' >> pulse.txt
git ls-files | wc -l >> pulse.txt
git ls-files | sed -n 's/.*\.//p' | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr | awk '{$1=$1}1' >> pulse.txt
cat pulse.txt 