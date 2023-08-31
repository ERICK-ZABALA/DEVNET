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
    'oracle-01': {'prompt':'[opc@jenkins-master]', 'ip':'155.248.226.213', 'username':'opc', 'port':'22'} 
}
# copy the public key in the folder .ssh
key = paramiko.RSAKey.from_private_key_file('/home/codespace/.ssh/id_rsa')

for device in devices.keys():
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(devices[device]['ip'], 
                       username=devices[device]['username'], 
                       pkey=key,
                       look_for_keys=False,
                       allow_agent=False)
    
    stdin, stdout, stderr = connection.exec_command('ls -l')
    ls_result = stdout.read().decode('utf-8')
    print(ls_result)
    
    stdin, stdout, stderr = connection.exec_command('pwd')
    pwd_result = stdout.read().decode('utf-8')
    print(pwd_result)

    connection.close()

"""
Output: 

(iosv) @ERICK-ZABALA ➜ /workspaces/DEVNET/network/paramiko (main) $ python ssh_paramiko_02.py
ls -l
total 70464
drwxrwxr-x.  5 opc opc       80 Dec 28  2022 Angular
drwxr-xr-x.  3 opc opc       78 Jul 15  2022 aws
-rw-rw-r--.  1 opc opc 47030919 Jul 15  2022 awscliv2.zip
drwxrwxr-x.  2 opc opc       25 Nov 20  2022 Birthday
drwxrwxr-x.  3 opc opc      100 Mar  1  2023 ciscovpn
drwxrwxr-x.  5 opc opc       42 Nov  3  2022 cs50p
drwxrwxr-x. 10 opc opc     4096 Sep  4  2022 demo
drwxrwxr-x.  7 opc opc      219 Jul 26 20:15 DEVNET
drwxrwxr-x. 10 opc opc     4096 Jul 10  2022 easy-rsa
drwxrwxr-x.  8 opc opc     4096 Dec 22  2022 hello-world
-rwxrwxr-x.  1 opc opc    33684 Jul 23 22:37 install_thousandeyes.sh
drwxrwxr-x.  7 opc opc      104 Aug 26 06:14 kali
drwxrwxr-x.  5 opc opc      151 Dec  7  2022 loc-nmap
drwxrwxr-x.  3 opc opc       80 Jul 10  2022 openvpn-install
drwxr-xr-x. 17 opc opc     4096 Oct 15  2022 Python-3.10.2
-rw-rw-r--.  1 opc opc 25067363 Jan 13  2022 Python-3.10.2.tgz
drwxrwxr-x.  6 opc opc      158 Nov 20  2022 webex-api
drwxrwxr-x.  7 opc opc      257 Nov 29  2022 webex-websoket
drwxrwxr-x.  5 opc opc       58 Feb 18  2023 web-socket

pwd
/home/opc     
"""

    

