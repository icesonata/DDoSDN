# DDoSDN
This is a private repository about applying Machine Learning model into DDoS attack detection in SDN. 

# Prerequisite
Install required packages via: ```pip3 install -r requirements.txt```\
*Note that the program is written and tested with Python version 3.x, so does pip.*

# Manual
Create a virtual environment via Python: ```python3 -m venv venv```.\
After that, install all requirements as described in [Prerequisite](#prerequisite).\
Next run each one below in different shell respectively.\
Start the Ryu controller by running: ```ryu-manager customCtrl.py```\
Start the SDN topology by running: ```python3 topo.py```\
Start the collecting and inspecting program by running: ```source collect.sh```

# Note
Note that mitigation method is not available in this project.