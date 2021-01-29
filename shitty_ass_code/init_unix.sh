#!/bin/bash

if [[ $(python3.9 --version) ]]
then
  echo "Guess you have python 3.9"
else
  echo "Installing python 3.9"
  curl https://www.python.org/ftp/python/3.9.1/python-3.9.1-macosx10.9.pkg --output python.pkg
  open python.pkg
fi
pip3 install alpaca_trade_api

echo {} > cache.json
echo 'Starting Gonk Stonks! Good Luck!'
python3 main.py
