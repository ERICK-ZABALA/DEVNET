#!/home/devnet/devnet/DEVNET/network/web/venv/bin/python

from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from flask import jsonify

def show_list():
    nr = InitNornir(inventory = { "options": { "host_file":"/home/devnet/devnet/DEVNET/network/web/nornir_custom/hosts.yaml"}}, 
                logging={"log_file": "mylogs", "level": "DEBUG"})
    
    try:
        result = nr.run(
        task = netmiko_send_command,
        command_string= "ls"
        )
        # Captura la salida en una variable como una cadena
        output = result["linux-server"][0].result
        print_result(result)
        return (output)
    
    except Exception as e:
        return jsonify({"error": "Error connection ssh device", "details": str(e)}), 500

