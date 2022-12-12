# Project made by: Dana Zorohov 207817529, Nir Meir 313229106

"""
----DDOS Project----
This script is monitoring the target.
It sending ping packets to the target and calculates the time of responding.
"""

# IMPORTS
from scapy.layers.inet import IP, ICMP
from scapy.all import *
import socket


# The time records file
f = open("pings_results_p.txt", "a")

# Counter for each icmp packet
counter = 0

# True-server is alive
flag = True
host='192.168.248.138'
port= 80

# Start time of the monitoring
start_prog = time.time()

# While True - while the server is alive

while flag:
    start = time.time()
    counter+=1
    print("pinging the target....")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # presumably
    sock.settimeout(5)
    try:
        sock.connect((host, port))
        end = time.time()
        print("This host is up")
        total_time = end - start
        f.write("Ping" + " " + str(counter) + " " + "replay")
        f.write("\n")
        f.write("ttl" + " " + str(total_time) + "  " + "Sec")
        f.write("\n")
    except:
        flag = False
        end_prog = time.time()
        total_prog = end_prog - start_prog
        avg = total_prog / counter
        print("This host is down")
        f.write("\n")
        f.write("The server is shutdown")
        f.write("\n")
        f.write("The average time is" + " " + str(avg) + "  " + "Sec")
        f.write("\n")
        f.close()
    else:
        sock.close()



    # ip ='192.168.248.138'
    # icmp = IP(dst=ip)/ICMP()
    # #IP defines the protocol for IP addresses
    # #dst is the destination IP address
    # #TCP defines the protocol for the ports
    # resp = sr1(icmp,timeout=10)
    # if resp == None:
    #     flag=False
    #     end_prog=time.time()
    #     total_prog=end_prog-start_prog
    #     avg=total_prog/counter
    #     print("This host is down")
    #     f.write("\n")
    #     f.write("The server is shutdown")
    #     f.write("\n")
    #     f.write("The average time is" + " " + str(avg) + "  " + "Sec")
    #     f.write("\n")
    #     f.close()
    #
    # else:
    #     end=time.time()
    #     print("This host is up")
    #     total_time=end-start
    #     f.write("Ping" + " " + str(counter) + " " + "replay")
    #     f.write("\n")
    #     f.write("ttl" + " " + str(total_time) + "  " + "Sec")
    #     f.write("\n")