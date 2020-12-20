#!/bin/bash
for i in {1..2000}
do
sudo ovs-ofctl dump-flows s1 > data/raw
grep "nw_src" data/raw > data/flowentries.csv
awk -F "," '{split($4,a,"="); print a[2]","}' data/flowentries.csv > data/packets.csv
awk -F "," '{split($5,b,"="); print b[2]","}' data/flowentries.csv > data/bytes.csv
awk -F "," '{out=""; for(i=2;i<=NF;i++){out=out" "$i}; print out}' data/flowentries.csv | awk -F " " '{split($11,d,"="); print d[2]","}' > data/ipsrc.csv
awk -F "," '{out=""; for(i=2;i<=NF;i++){out=out" "$i}; print out}' data/flowentries.csv | awk -F " " '{split($12,d,"="); print d[2]","}' > data/ipdst.csv
python3 computeTuples.py
echo "Inspection no. $i"
python3 inspector.py
state=$(awk '{print $0;}' .result)
if [ $state -eq 1 ];
then
echo "Network is under attack!"
echo "Reseting flow tables..."
# 
default_flow=$(sudo ovs-ofctl dump-flows s1 | tail -n 1)    # Get action:CONTROLLER:<port_num>
sudo ovs-ofctl del-flows s1
sudo ovs-ofctl add-flow s1 "$default_flow"
fi
sleep 3
done



# ==============================================================================================================================================
# Ref
# Get all fields (n columns) in awk: https://stackoverflow.com/a/2961711/11806074
# e.g. awk -F "," '{out=""; for(i=2;i<=NF;i++){out=out" "$i" "i}; print out}' data/flowentries.csv 

# ovs-ofctl reference
# add-flow SWITCH FLOW        add flow described by FLOW    e.g. ... add-flow s1 "flow info"
# add-flows SWITCH FILE       add flows from FILE           e.g. ... add-flows s1 flows.txt

# example of multiple commands in awk, these commands below extract ip_src and ip_dst from flow entries
# awk -F "," '{split($10,c,"="); print c[2]","}' data/flowentries.csv > data/ipsrc.csv
# awk -F "," '{split($11,d,"=");  split(d[2],e," "); print e[1]","}' data/flowentries.csv > data/ipdst.csv