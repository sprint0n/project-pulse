#!/usr/bin/env bash
for i in {1..3}; do
    curl -s "http://worldclockapi.com/api/json/utc/now" \
  | sed -n 's/.*"currentDateTime":"\([^"]*\)".*/\1\n/p' >> pulse_history.log
    git log --oneline | wc -l >> pulse_history.log
    git ls-files | wc -l >> pulse_history.log
    echo >> pulse_history.log
    sleep 10
done


