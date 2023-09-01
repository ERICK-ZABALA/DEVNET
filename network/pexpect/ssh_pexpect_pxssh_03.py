#!/workspaces/DEVNET/network/iosv/bin/python

"""
First Pexpect Program
Protocol: SSH 
Environment: EVE-NG
Router: CSR1000V
Library: pexpect, pxssh
"""

from pexpect import pxssh


devices = {
    'csr1k-01': {'prompt':'CSR1000V#', 'ip':'34.125.235.12', 'port':'922', 'username':'devnet', 'password':'devnet'}, 
    'csr1k-02': {'prompt':'CSR1000V#', 'ip':'34.125.235.12', 'port':'822', 'username':'devnet', 'password':'devnet'}
}

commands = ['term length 0', 'show version', 'show run']

for device in devices.keys():
    device_prompt = devices[device]['prompt']
    username = devices[device]['username']
    password = devices[device]['password']
    
    child = pxssh.pxssh()
    index = child.login(devices[device]['ip'], username, password, port=devices[device]['port'], auto_prompt_reset=False)
    
    print('Index: ', index)

    if index == 0:
        # Enviar 'yes' para aceptar la clave RSA
        child.sendline("yes")
    if index == 2:
        child.expect(["Password:"])
        child.sendline(password)
        child.expect(device_prompt, timeout=5)
        print( 'The Device is in Mode: "Configure Terminal"')
        
        # Start the loop commands
        outputFileName = device + '_output.txt'
        with open(outputFileName, 'wb') as f:
            for command in commands:
                child.sendline(command)
                child.expect(device_prompt)
                f.write(child.before)
        
        child.logout()



"""
*** Output: ***
Run: python get_info_00.py

"""
