# Configuration Nexus 9000

feature nxapi
username cisco priv 15 pass cisco
network-operator
username cisco role network-admin
username cisco passphrase lifetime 99999 warntime 14 gracetime 3

configure terminal
nxapi http port 80
nxapi sandbox

# Configuration Host Python - API

python -m venv nx
pip install ncclient

# Sandbox Nexus 9000

Nexus 9000: sbx-nxos-mgmt.cisco.com
SSH Port: 22
NETCONF Port: 830
NXAPI Ports: 80 (http) & 443 (HTTPS)
RESTCONF Port : 443 (HTTPS)
Credentials:
Username: admin
Password: Admin_1234!

# CISCO ACI and CISCO APIC-EM

ACI = Focus on data center operations --- works over ACI API flow over REST Model using Http (support devices cisco only) 
APIC-EM = focuses on enterprise modules

# CISCO MERAKI CONTROLLER



Hello World:
There are various examples in the Sandbox Repository on GitHub that you can explore and use with this Sandbox.
https://github.com/DevNetSandbox/sbx_nxos_ao.
