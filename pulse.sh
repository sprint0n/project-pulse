#!/usr/bin/env bash
git log --oneline | wc -l > pulse.txt
curl -s "http://worldclockapi.com/api/json/utc/now" \
  | sed -n 's/.*"currentDateTime":"\([^"]*\)".*/\1/p' >> pulse.txt
cat pulse.txt 