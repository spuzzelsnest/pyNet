#!/bin/bash

mkdir -p logs

sudo python3 discover.py
python3 dbConnect.py
sudo python3 detect.py
