# Project made by: Dana Zorohov 207817529, Nir Meir 313229106

"""
----DDOS Project----
This script is monitoring the target.
It sending ping packets to the target and calculates the time of responding.
"""

# IMPORTS
from scapy.all import *
import socket
import time


# The time records file
f = open("pings_results_p.txt", "a")

# Counter for each packet
counter = 0

# True-server is alive
flag = True
# Target's address and port
host = '192.168.248.138'
port = 80

# Start time of the monitoring
total_time_prog = 0



# While True - while the server is alive
while flag:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
     # start time of sending this specific packet
    start = time.time()
    # packet's counter
    counter += 1
    print("pinging the target....")

    # creating socket
    # sending ping to the host
    try:
        # trying to connect to the host with specific port
        # if succeeded - host is up
        sock.connect((host, port))
        # end time of sending this specific packet
        end = time.time()
        print("This host is up")

        # total sending time of the packet
        total_time = end - start
        f.write("Ping" + " " + str(counter) + " " + "replay")
        f.write("\n")
        f.write("ttl" + " " + str(total_time) + "  " + "Sec")
        f.write("\n")
        total_time_prog += total_time
        time.sleep(5)


    except:
        # host is down
        flag = False
        # average time of the connection
        avg = total_time_prog / counter
        print("This host is down")
        f.write("\n")
        f.write("The server is shutdown")
        f.write("\n")
        f.write("The average time is" + " " + str(avg) + "  " + "Sec")
        f.write("\n")
        f.close()
        sock.close()

        if(counter==300):
            flag = False
            # average time of the connection
            avg = total_time_prog / counter
            f.write("\n")
            f.write("The average time is" + " " + str(avg) + "  " + "Sec")
            f.write("\n")
            f.close()
            sock.close()



