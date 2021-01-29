#!/bin/bash
if [ -e "cache.json" ]; then
    python3 main.py
else 
    ./init_unix.sh
fi 