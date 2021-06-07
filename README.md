# DDoSDN
This is a repository about applying Machine Learning model into DDoS attack detection in Software-defined network. \
Demo video: https://youtu.be/QMnSjwCPHMM

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

# Description
```.result```: represents the classification result from the model, true or false that the system is under DDoS attack. \
```gentraffic.sh```: generates normal traffic. \
```warn.py```: ignore the warning due to deprecation. \
```topo.py```: mininet topology. \
```realtime.csv```: csv file that contains 5 characteristic values. (read more at [Referece](#reference)) \
```inspector```: make a call to the model so as to classify the given characteristic values. \
```customCtrl.py```: custom Ryu controller. \
```computeTuples.py```: compute 5 characteristic from raw data. \
```collect.sh```: collect records in flow tables from openflow switches to process and extract raw data. \

# Dataset
The dataset used in this project is from [DDoS-Detection-SDN](https://github.com/surajiyer3/DDoS-Detection-SDN).

# Note
Note that mitigation method is not available in this project. The mitigate.sh file demonstrates the idea of setting fixed routing for openflow switches.

# Reference
[1] [DDoS-Detection-SDN](https://github.com/surajiyer3/DDoS-Detection-SDN) by William Isaac, Suraj Iyer, Nishank Thakra \
[2] [Ye, J., Cheng, X., Zhu, J., Feng, L. and Song, L., 2018. A DDoS attack detection method based on SVM in software defined network. Security and Communication Networks, 2018.](https://www.hindawi.com/journals/scn/2018/9804061/)
