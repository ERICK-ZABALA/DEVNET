#!/workspaces/DEVNET/network/iosv/bin/python

import time 
import json 
import paramiko

"""
First Paramiko Program
Protocol: SSH 
Environment: EVE-NG
Router: CSR1000V
Library: paramiko
"""

with open('devices.json', 'r') as f:
    devices = json.load(f)

print(devices)


with open('commands.txt', 'r') as f:
    commands = f.readlines()

print(commands)
    
# Define una lista de algoritmos que deseas deshabilitar
#disabled_algorithms = {
#    'kex': ['ecdh-sha2-nistp256', 'ecdh-sha2-nistp384'],
#    'server_host_key': ['ssh-rsa'],
#    'cipher': ['aes128-cbc']
#}
# disabled_algorithms=disabled_algorithms

# copy the public key in the folder .ssh in your remote SERVER or ROUTER

key = paramiko.RSAKey.from_private_key_file('/home/codespace/.ssh/id_rsa')

for device in devices.keys():
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)
    print(devices[device]['ip'])
    
    connection.connect(devices[device]['ip'],
                       port= 922, 
                       username=devices[device]['username'], 
                       pkey=key,
                       look_for_keys=False,
                       allow_agent=False,
                       disabled_algorithms=dict(pubkeys=["rsa-sha2-512", "rsa-sha2-256"])
                       )
    
    new_connection = connection.invoke_shell()
    output = new_connection.recv(5000)
    print(output)

    new_connection.send("show version | i V\n")
    time.sleep(3)
    output = new_connection.recv(5000)
    print(output)
    
    for command in commands:
        print(command)
        new_connection.send(command)
        time.sleep(3)
    
    new_connection.close()
    


