TCP-Layer 4 OSI SEGMENTS 160 bits headers
source destination ports, sequence number,
ack number, control flag, checksum

uses datagrams sockets or ports
host a hot communication
80 http
25 smtp

tcp establish an machine state is necesary to track each connection:
Listen, SYN SENT, SYN RECEIVED, ESTABLISHED, FIN-WAIT, CLOSE-WAIT, CLOSING,
LAST-ACK, TIME-WAIT, CLOSED

handshake SYN, SYNC-ACK, ACK

UDP LAYER 4 - 64 bits headers
Source destination port, length and checksum

lack of releable transmition - video streaming
consider fast DNS based in udp for small latency --- recommended
