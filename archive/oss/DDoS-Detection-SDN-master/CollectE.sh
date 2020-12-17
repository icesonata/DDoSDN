#!/bin/bash
for i in {1..2000}
do
sudo ovs-ofctl dump-flows s1 > jax1
grep "nw_src" jax1 > jax2.csv
awk -F "," '{split($4,a,"="); print a[2]","}' jax2.csv > jaxpackets.csv
awk -F "," '{split($5,d,"="); print d[2]","}' jax2.csv > jaxbytes.csv
awk -F "," '{split($14,b,"="); print b[2]","}' jax2.csv > jaxipsrc.csv
awk -F "," '{split($15,c,"="); print c[2]","}' jax2.csv > jaxipdst.csv
python CollectE.py
sudo ovs-ofctl del-flows s1
echo $i
python Inspect.py
r=$(awk '{print $0;}' Result.txt)
if [ $r -eq 1 ]; then
echo "network is under attack!!"
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.2,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.3,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.4,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.5,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.6,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.7,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.8,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.9,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.10,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.11,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.12,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.13,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.14,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.15,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.16,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.17,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.18,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.19,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.20,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.21,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_dst=10.0.0.1,priority=50000,actions=drop
fi
sleep 3
done
