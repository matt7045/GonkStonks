#!/bin/bash
if [ -e "cache.json" ]; then
    python main.py
else 
    ./init_unix.sh
fi 