#!/bin/bash
# for i in {1..2}
# do
# ...
# done

grep "nw_src" data/raw > data/flowentries.csv
awk -F "," '{split($4,a,"="); print a[2]","}' data/flowentries.csv > data/packets.csv
awk -F "," '{split($5,b,"="); print b[2]","}' data/flowentries.csv > data/bytes.csv
awk -F "," '{split($10,c,"="); print c[2]","}' data/flowentries.csv > data/ipsrc.csv
awk -F "," '{split($11,d,"=");  split(d[2],e," "); print e[1]","}' data/flowentries.csv > data/ipdst.csv
# python computeTuples.py






# ==============================================================================================================================================
# Ref
# Get all fields (n columns) in awk: https://stackoverflow.com/a/2961711/11806074
# e.g. awk -F "," '{out=""; for(i=2;i<=NF;i++){out=out" "$i" "i}; print out}' data/flowentries.csv 

# ovs-ofctl reference
# add-flow SWITCH FLOW        add flow described by FLOW    e.g. ... add-flow s1 "flow info"
# add-flows SWITCH FILE       add flows from FILE           e.g. ... add-flows s1 flows.txt
