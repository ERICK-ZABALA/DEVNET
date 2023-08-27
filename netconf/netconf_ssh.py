"""
+ Configure NETCONF CSR1000V 16.6 XE
CLI:

# config t
# hostname csr1000v
# line con 0
# logging synchronous
# exit
# ip domain name cisco.com
# username cisco priv 15 pass cisco
# crypto key generate rsa
# 1024
# ip ssh version 2
# line vty 0 4
# login local 
# transport input ssh
# exit
# interface gi 2
# ip address 172.16.1.6 255.255.255.0
# no shu
# ip route 0.0.0.0 0.0.0.0 172.16.1.1
# do ping 172.16.1.1

# netconf ssh
# netconf-yang
# wr
"""