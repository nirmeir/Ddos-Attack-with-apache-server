# Ddos-Attack-with-apache-server

In this project, we aim to simulate and analyze a Distributed Denial of Service (DDoS) attack on a target machine running an Apache server. The project involves three key components: the Attacker, the Target, and the Monitor.

Attacker: The Attacker will consist of two programs, one written in C and the other in Python. The Attacker's role is to generate a DDoS attack by sending a large number of TCP SYN packets to the target machine. This will be done in a loop of 100 iterations, with each iteration sending 10,000 SYN packets, resulting in a total of 1 million packets. The time taken by the Attacker to send a packet will be measured and recorded.

Target: The Target machine will run an Apache server, serving as the victim of the DDoS attack. It will be flooded with SYN packets from the Attacker, which may lead to server overload and potential disruption of normal services.

Monitor: The Monitor's task is to continuously send ping requests to the target server during the attack. This will help monitor the health and responsiveness of the target server under the DDoS attack conditions.

Measurement and Analysis:

The project will generate measurement files capturing various metrics. The measurements include:

Time taken by the Attacker to send a packet (average)
Round-Trip Time (RTT) of ping requests from the Monitor to the target server
Graphical Representation:
The data collected will be visualized using matplotlib graphs. Two graphs, "Syn_pkts_c.png" and "Syn_pkts_p.png," will depict the time required for the Attacker to send a packet for the C and Python attacks, respectively. The x-axis will represent the time taken to send a packet (logarithmic scale), and the y-axis will indicate the number of packets sent.

Report and Interpretation:
A concise report will be prepared summarizing the results of the experiments. The report will include information about the average and standard deviation of the measured metrics. Additionally, the report will offer insights into the observed differences between the C and Python attacks, providing an understanding of their respective impacts on the target server's performance and responsiveness.

It's important to note that while this project aims to simulate a DDoS attack for educational purposes, DDoS attacks are illegal and unethical in real-world scenarios. This project focuses on analyzing the effects of such an attack under controlled conditions to gain insights into server behavior and network performance.
