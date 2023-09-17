#!/workspaces/DEVNET/network/iosv/bin/python

from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(inventory = { "options": { "host_file":"/home/devnet/devnet/DEVNET/network/web/nornir/hosts.yaml"}}, 
                logging={"log_file": "mylogs", "level": "DEBUG"})

result = nr.run(
    task = netmiko_send_command,
    command_string= "ls"
)

print_result(result)

