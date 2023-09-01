#! /workspaces/DEVNET/network/iosv/bin/python

"""
First Paramiko Program
Protocol: SSH 
Environment: EVE-NG
Router: CSR1000V
Library: paramiko
"""
import paramiko
import time, json

with open('devices.json', 'r') as f:
    devices = json.load(f)

print(devices)

with open('commands.txt', 'r') as f:
    commands = f.readlines()

print(commands)

# copy the public key in the folder .ssh in your remote SERVER or ROUTER
key = paramiko.RSAKey.from_private_key_file('/home/codespace/.ssh/id_rsa')

for device in devices.keys():
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    connection.connect(devices[device]['ip'], 
                       username=devices[device]['username'], 
                       port=devices[device]['ip'],  
                       pkey=key,
                       look_for_keys=False,
                       allow_agent=False)

    new_connection = connection.invoke_shell()
    output = new_connection.recv(5000)
    print(output)

    new_connection.send("show version | i V\n")
    time.sleep(3)
    output = new_connection.recv(5000)
    print(output)

    new_connection.close()
    


