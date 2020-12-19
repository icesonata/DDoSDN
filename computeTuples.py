import numpy as np
import csv

# Standard deviation of packets
packets_csv = np.genfromtxt('data/packets.csv', delimiter=",")
dt_packets = packets_csv[:,0]
stdev_packets = np.std(dt_packets) 

# Standard deviation of bytes
bytes_csv = np.genfromtxt('data/bytes.csv', delimiter=",")
dt_bytes = bytes_csv[:,0]
stdev_bytes = np.std(dt_bytes)

# Number of source IPs
n_ip = np.prod(dt_bytes.shape)      # Get number of different source IPs
num_src_ip = n_ip / 3               # Get number of IPs for every second by multiple interval - 3s

# Number of Flow entries
num_fl = n_ip / 3

# Number of interactive flow entries