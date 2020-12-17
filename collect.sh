#!/bin/bash
for i in {1..2000}
do
sudo ovs-ofctl dump-flows s1 > ??
done