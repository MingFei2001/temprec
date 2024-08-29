#!/usr/bin/env bash

# Define color code
declare -r WARNING='\033[0;33m'
# declare -r ERROR='\033[0;31m'
declare -r NC='\033[0m'

# install sensors tools
sudo apt install lm-sensors

# Detect the sensors
printf "${WARNING} [WARNING] Accept all default if no changes are needed.${NC}\n"
sudo sensors-detect

# Preparing the virtual env
python3 -m venv venv
source venv/bin/activate
pip install pandas

# Run the python script
python ./rectemp.py
less ./cpu_temp_log.csv
