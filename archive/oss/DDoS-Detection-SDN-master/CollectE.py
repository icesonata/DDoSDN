import numpy as np
import csv


#Standard Deviation of Packets
packetcsv = np.genfromtxt('jaxpackets.csv', delimiter=",")
packets = packetcsv[:,0]
stdevpack = np.std(packets)

#Standard Deviation of Bytes
bytecsv = np.genfromtxt('jaxbytes.csv', delimiter=",")
bytes = bytecsv[:,0]
stdevbyte = np.std(bytes)

#Number of Source IPs
nbiptemp = np.prod(bytecsv.shape)
nbip = nbiptemp/3

#Number of Flow Entries
nbfl = nbiptemp/3

#Number of Interactive Flow Entries
with open('jaxipsrc.csv', 'r') as t1, open('jaxipdst.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('intflow.csv', 'w') as outFile:
    for line in fileone:
        if line not in filetwo:
            outFile.write(line) 
with open('intflow.csv') as intflow:
	reader = csv.reader(intflow, delimiter = ",")
	data = list(reader)
	row_count_nonint = len(data)

interflowtemp = nbiptemp-row_count_nonint
interflow = float(interflowtemp)/nbiptemp

#Labeling the data as normal
#label = 1

#Creating headers
randvar1 = "SSIP"
randvar2 = "Stdevpack"
randvar3 = "Stdevbyte"
randvar4 = "NbFlow"
randvar5 = "NbIntFlow"

header = []
header = [randvar1,randvar2,randvar3,randvar4,randvar5]

#Creating Training Data For Normal Traffic
smart = []
smart = [nbip,stdevpack,stdevbyte,nbfl,interflow]

with open('Live.csv', 'w') as datafile:
	writer = csv.writer(datafile, delimiter=",")
	writer.writerow(header)
	writer.writerow(smart)

datafile.close()
