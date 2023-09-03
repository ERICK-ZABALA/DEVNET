#!/usr/bin/python3
from scapy.all import *
#destination = "155.248.226.213"
#dport = 22

def icmp_ping(destination):
    # regular ICMP ping
    ans, unans = sr(IP(dst=destination)/ICMP())
    return ans
def tcp_ping(destination, dport):
    ans, unans = sr(IP(dst=destination)/TCP(sport=680,dport=(dport),flags="S"))
    return ans
def udp_ping(destination):
    ans, unans = sr(IP(dst=destination)/UDP(dport=0))
    return ans
def answer_summary(ans):
    for send, recv in ans:
        print(recv.sprintf("%IP.src% is alive"))

def main():
    print("*** ICMP Ping ***")
    ans = icmp_ping("155.248.226.213")
    answer_summary(ans)
    print("** TCP Ping **")
    ans = tcp_ping("155.248.226.213", 22)
    answer_summary(ans)
    print("*** UDP Ping ***")
    ans = udp_ping("155.248.226.213")
    answer_summary(ans)

if __name__ == "__main__":
    main()

"""

devnet@PC1 ~/devnet/DEVNET/security/tools $ sudo python3 scapy_ping_collection00.py 
*** ICMP Ping ***
Begin emission:
Finished sending 1 packets.
.*
Received 2 packets, got 1 answers, remaining 0 packets
155.248.226.213 is alive
** TCP Ping **
Begin emission:
Finished sending 1 packets.
*
Received 1 packets, got 1 answers, remaining 0 packets
155.248.226.213 is alive
*** UDP Ping ***
Begin emission:
Finished sending 1 packets.
..........................................................................................................................^C
Received 122 packets, got 0 answers, remaining 1 packets
devnet@PC1 ~/devnet/DEVNET/security/tools $ 

"""