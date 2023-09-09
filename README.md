# ABB Robot Web Server 2

This package provides code to interact with [ABB robot web service](https://developercenter.robotstudio.com/api/RWS?urls.primaryName=Introduction).
Tested and developed for version `3HAC073675-001 Revision:D` with an ABB GoFa robot.

Code updated from [ABB Robot Web Service](https://github.com/prinsWindy/ABB-Robot-Machine-Vision/tree/master/RobotWebServices).

## Build and Test

1. Clone/fork the repo from Github.
2. Install packages with pip: `pip -r requirements.txt`
3. Run `pip install -e .` in the root folder to install rws2 in editable mode (`pip install .` is enough if you do not plan to contribute).

The library should then be installed and you should be able to call it in python with `import rws2`.

## How to use

- The class `RWS` in `RWS2.py` implements the Robot Web Server protocol as specified by ABB. Documentation is in the code.
- The file `main.py` runs a simple console application to interact with the Robot Controller. Run the python file to start.
