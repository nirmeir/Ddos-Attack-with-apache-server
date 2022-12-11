import sys

from scapy.layers.inet import IP, ICMP
from scapy.all import *

f = open("pings_results_p.txt", "a")
counter=0;
flag = True
start_prog=time.time()
while flag:
    start = time.time()
    counter+=1
    print("pinging the target....")
    ip ='192.168.248.138'
    icmp = IP(dst=ip)/ICMP()
    #IP defines the protocol for IP addresses
    #dst is the destination IP address
    #TCP defines the protocol for the ports
    resp = sr1(icmp,timeout=10)
    if resp == None:
        flag=False
        end_prog=time.time()
        total_prog=end_prog-start_prog
        avg=total_prog/counter
        print("This host is down")
        f.write("\n")
        f.write("The server is shutdown")
        f.write("\n")
        f.write("The average time is" + " " + str(avg) + "  " + "Sec")
        f.write("\n")
        f.close()

    else:
        end=time.time()
        print("This host is up")
        total_time=end-start
        f.write("Ping" + " " + str(counter) + " " + "replay")
        f.write("\n")
        f.write("ttl" + " " + str(total_time) + "  " + "Sec")
        f.write("\n")
