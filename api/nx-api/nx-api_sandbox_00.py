#!/workspaces/DEVNET/api/nx-api/nexus/bin/python

"""
# DO 

Show all the capabilities over protocol Netconf
+ NETCONF VIA SSH 22 PORT

# Sandbox Nexus 9000

Nexus 9000: sbx-nxos-mgmt.cisco.com
SSH Port: 22
NETCONF Port: 830
NXAPI Ports: 80 (http) & 443 (HTTPS)
RESTCONF Port : 443 (HTTPS)
Credentials:
Username: admin
Password: Admin_1234!

"""
from ncclient import manager

conn = manager.connect(
    host='sbx-nxos-mgmt.cisco.com',
    port=22,
    username='admin',
    password='Admin_1234!',
    # the known_host requirement for SSH; if not, the host needs to be listed in the ~/.ssh/known_hosts file.
    hostkey_verify=False, 
    device_params={'name': 'nexus'},
    # disables public-private key auth
    look_for_keys=False
    )


for value in conn.server_capabilities:
    print(value)

conn.close_session()

"""
    Output:
    DEVNET/api/nx-api (main) $ python nx-api_sandbox_00.py
        
    urn:ietf:params:xml:ns:netconf:base:1.0
    urn:ietf:params:netconf:base:1.0
    urn:ietf:params:netconf:capability:validate:1.0
    urn:ietf:params:netconf:capability:writable-running:1.0
    urn:ietf:params:netconf:capability:url:1.0?scheme=file
    urn:ietf:params:netconf:capability:rollback-on-error:1.0
    urn:ietf:params:netconf:capability:candidate:1.0
    urn:ietf:params:netconf:capability:confirmed-commit:1.0
        
"""
    