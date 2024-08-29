# TempRec
> Temperature Recorder

This project is a simple CPU temperature logging tool for Linux systems. It records the CPU temperature at regular intervals and provides options to view the collected data.

## Features
- Logs CPU temperature at specified intervals
- Saves data in CSV format
- Easy to set up and use

## Prerequisites
- Python 3.6 or higher
- Debian-based Linux operating system

## Initialization
1. Clone this repository:
```bash
git clone https://github.com/MingFei2001/temprec.git
cd temprec
```

2. Run the init script
```bash
bash init.sh
```
This script will:
- Install necessary tools
- Set up sensors
- Prepare the virtual environment
- Install required Python packages
- Start the first recording

## Usage
1. To start logging CPU temperature:
```bash
python3 ./temprec.py
```
2. The script will run and log temperatures. Press Ctrl+C to stop logging.
3. After stopping, you'll be prompted if you want to view the collected data.
4. To exit the virtual environment
```bash
# enter the following in the terminal
deactivate
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
