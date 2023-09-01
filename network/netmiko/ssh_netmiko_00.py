#!/workspaces/DEVNET/network/iosv/bin/python

from netmiko import ConnectHandler


devices = {
    'device_type':'linux', 'host':'155.248.226.213', 'username':'opc', 'use_keys':True, 'key_file': '/home/codespace/.ssh/id_rsa', 'port':22
    }

net_connect = ConnectHandler(**devices)
prompt = net_connect.find_prompt()
print(prompt)
output = net_connect.send_command('ls -l')
print(output)
# Using send_config_set maintain la same session and insert command line sequence
config = net_connect.send_config_set(['export TRIAL="AAB62"', 'echo $TRIAL'])
print(config)





net_connect.disconnect()