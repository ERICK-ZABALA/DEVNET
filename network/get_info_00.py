"""
First Pexpect Program
Protocol: SSH 
Environment: EVE-NG
Router: CSR1000V
Library: pexpect
"""

import pexpect

devices = {
    'csr1k-01': {'prompt':'CSR1000V#', 'ip':'34.125.235.12', 'port':'922', 'username':'devnet', 'password':'devnet'}, 
    'csr1k-02': {'prompt':'CSR1000V#', 'ip':'34.125.235.12', 'port':'822', 'username':'devnet', 'password':'devnet'}
}

for device in devices.keys():
    device_prompt = devices[device]['prompt']
    username = devices[device]['username']
    password = devices[device]['password']
    
    child = pexpect.spawn('ssh ' + username + '@' + devices[device]['ip'] + ' -p ' + devices[device]['port'])
    index = child.expect(["Are you sure you want to continue connecting", pexpect.EOF, pexpect.TIMEOUT])
    
    print('Index: ', index)

    if index == 0:
        # Enviar 'yes' para aceptar la clave RSA
        child.sendline("yes")
    if index == 2:
        child.expect(["Password:", pexpect.EOF, pexpect.TIMEOUT])
        child.sendline(password)
        child.expect(device_prompt)
        print( 'The Device is in Mode: "Configure Terminal"')

        print('**** Generating... - show version | include V ****\n')

        child.sendline('show version | i V')
        # Esperar a que aparezca la salida del comando
        child.expect(device_prompt)
        print(child.before)
        child.sendline('exit')


"""
*** Output: ***
Run: python get_info_00.py

"""
