
root@eve-cloud:/home/devnet_code# iptables -t nat -A PREROUTING -p tcp --dport 922 -j DNAT --to 192.168.1.10:22
root@eve-cloud:/home/devnet_code# iptables -L -nv  -t nat 

http://34.125.235.12/
CLI: ssh devnet@34.125.235.12 -p 922
