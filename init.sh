#!/usr/bin/env bash

# Define color code
declare -r WARNING='\033[0;33m'
declare -r NC='\033[0m'

# install sensors tools
sudo apt install lm-sensors

# Detect the sensors
printf "${WARNING}[WARNING] Setting up the sensors.${NC}\n"
printf "${WARNING}[WARNING] Accept all default if no changes.${NC}\n"
sudo sensors-detect

# Preparing the virtual env
python3 -m venv venv
source venv/bin/activate
pip install pandas

# Run the python script
printf "${WARNING} [WARNING] The recording starts now.${NC}\n"
python ./temprec.py

# Ask to view the data
read -p "Do you want to view the collected data? (y/n)" yn
case $yn in
	[Yy]* )
		less ./cpu_temp_log.csv;;
	[Nn]* )
		printf "exiting ... \n";;
	*)
		printf "exiting ... \n";;
esac
