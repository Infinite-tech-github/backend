#!/usr/bin/env bash

# Run Uvicorn with auto-reload
python3 -m uvicorn app:app --reload

# Pause the script by prompting the user to press Enter
read -p "Press Enter to continue..."