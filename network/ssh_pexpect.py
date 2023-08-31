"""
Login via SSH to router CSR1000V

Output:

(iosv) @ERICK-ZABALA ➜ /workspaces/DEVNET/network (main) $ python ssh_pexpect.py 

2 >>> Index value

show version | i V
Cisco IOS XE Software, Version 17.03.02
Cisco IOS Software [Amsterdam], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 17.3.2, RELEASE SOFTWARE (fc3)
licensed under the GNU General Public License ("GPL") Version 2.0.  The
software code licensed under GPL Version 2.0 is free software that comes
GPL code under the terms of GPL Version 2.0.  For more details, see the
CSR1000V uptime is 1 hour, 52 minutes
cisco CSR1000V (VXE) processor (revision VXE) with 2072007K/3075K bytes of memory.

"""

import pexpect

child = pexpect.spawn('ssh devnet@34.125.235.12 -p 922')

index = child.expect(["Are you sure you want to continue connecting", pexpect.EOF, pexpect.TIMEOUT])

print('Index:', index)

if index == 0:
    # Enviar 'yes' para aceptar la clave RSA
    child.sendline("yes")
if index == 2:
    child.expect(["Password:", pexpect.EOF, pexpect.TIMEOUT])
    child.sendline('devnet')
    child.expect("CSR1000V#")
    print( 'The Device is in Mode: "Configure Terminal"')

    print('Generating... - show version | include V\n')

    child.sendline('show version | i V')
    # Esperar a que aparezca la salida del comando
    child.expect('CSR1000V#')  
    # Puedes ajustar este patrón según la salida real

    # Imprimir la salida del comando show version
    print(child.before.decode())
    print(child.before)
    print(child.after)

    child.sendline('show run | i hostname')
    child.expect('CSR1000V#')
    print(child.before)
    
    child.close()
