#!/workspaces/DEVNET/network/iosv/bin/python

"""
First Paramiko Program
Protocol: SSH 
Environment: EVE-NG
Router: CSR1000V
Library: paramiko
"""
import paramiko, time

devices = {
    'csr1k-01': {'prompt':'CSR1000V#', 'ip':'34.125.235.12', 'port':'922', 'username':'devnet', 'password':'devnet'}, 
    'csr1k-02': {'prompt':'CSR1000V#', 'ip':'34.125.235.12', 'port':'822', 'username':'devnet', 'password':'devnet'}
}

commands = [ 'show version', 'show run']

key = paramiko.RSAKey.from_private_key_file('/workspaces/DEVNET/network/paramiko/.ssh/id_rsa')


def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)

for device in devices.items():
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(devices[device]['ip'], 
                       username=devices[device]['username'], 
                       password=devices[device]['password'],
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
    


