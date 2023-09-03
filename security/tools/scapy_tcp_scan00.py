#!/usr/bin/python3
from scapy.all import *
import sys
#destination = "155.248.226.213"
#dport = 22

def tcp_scan(destination, dport):
    ans, unans = sr(IP(dst=destination)/TCP(sport=680,dport=(dport),flags="S"))
    for sending, returned in ans:
        """
        Cuando ves "SA" en la columna de flags de un paquete TCP en Wireshark, 
        significa que los bits SYN (Synchronize) y ACK (Acknowledgment) están 
        establecidos en 1. Esto indica que el paquete es parte del proceso de 
        establecimiento de una conexión TCP y está confirmando la sincronización 
        de números de secuencia (SEQ) y el reconocimiento del número de secuencia 
        del otro extremo.

        """
        if 'SA' in str(returned[TCP].flags):
            return destination + " port " + str(sending[TCP].dport) + " is open. "
        else:
            return destination + " port " + str(sending[TCP].dport) + " is close. "
        
def main():

    destination = sys.argv[1]
    port = int(sys.argv[2])
    scan_result = tcp_scan(destination,port)
    print(scan_result)

if __name__ == "__main__":
    main()

"""
Output:
devnet@PC1 ~/devnet/DEVNET/security/tools :( $ sudo python3 scapy_tcp_scan00.py 155.248.226.213 22
[sudo] password for devnet: 
Begin emission:
Finished sending 1 packets.
.*
Received 2 packets, got 1 answers, remaining 0 packets
155.248.226.213 port 22 is open
"""


