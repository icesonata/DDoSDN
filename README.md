# DDoSDN
This is a private repository about applying Machine Learning model into DDoS attack detection in SDN. 

# Prerequisite
Install required packages via: ```pip install -r requirements.txt```
*Note that the program is written and tested with Python version 3.x, so does pip.*

# Manual
Start the Ryu controller by running: ```ryu-manager customCtrl.py```\
Start the SDN topology by running: ```python3 topo.py```\
Start the collecting and inspecting program by running: ```source collect.sh```