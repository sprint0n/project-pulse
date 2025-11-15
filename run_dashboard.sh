#!/usr/bin/env bash
curl -s "https://ipapi.co/json" -o location.json
echo "Starting Streamlit dashboard..."
streamlit run app.py