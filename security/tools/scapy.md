# SCAPY

That is a tool that permit capture packet similar to wireshark for python and improve you automation network.

# Install SCAPY

$ git clone https://github.com/secdev/scapy.git
$ cd scapy
$ sudo apt-get install python3-pip
$ pip3 install setuptools
$ sudo python3 setup.py install
$ sudo scapy

@ERICK-ZABALA ➜ /workspaces/DEVNET/security/scapy (master) $ sudo scapy
INFO: Can't import PyX. Won't be able to use psdump() or pdfdump().
INFO: Can't import python-cryptography v1.7+. Disabled PKI & TLS crypto-related features.
INFO: Can't import python-cryptography v1.7+. Disabled WEP decryption/encryption. (Dot11)
INFO: Can't import python-cryptography v1.7+. Disabled IPsec encryption/authentication.
WARNING: No alternative Python interpreters found ! Using standard Python shell instead.
INFO: When using the default Python shell, AutoCompletion, History are disabled.
                                      
                     aSPY//YASa       
             apyyyyCY//////////YCa       |
            sY//////YSpcs  scpCY//Pp     | Welcome to Scapy
 ayp ayyyyyyySCP//Pp           syY//C    | Version 2.5.0.dev150
 AYAsAYYYYYYYY///Ps              cY//S   |
         pCCCCY//p          cSSps y//Y   | https://github.com/secdev/scapy
         SPPPP///a          pP///AC//Y   |
              A//A            cyP////C   | Have fun!
              p///Ac            sC///a   |
              P////YCpc           A//A   | Wanna support scapy? Star us on
       scccccp///pSP///p          p//Y   | GitHub!
      sY/////////y  caa           S//P   |             -- Satoshi Nakamoto
       cayCyayP//Ya              pY/Ya   |
        sY/PsY////YCc          aC//Yp 
         sc  sccaCY//PCypaapyCP//YSs  
                  spCPY//////YPSps    
                       ccaacs         
                                      
>>> exit()
Use exit() or Ctrl-D (i.e.

+ Test Scapy in python3:

@ERICK-ZABALA ➜ /workspaces/DEVNET/security (main) $ python3
Python 3.10.8 (main, Aug 19 2023, 00:31:12) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from scapy.all import *
>>> exit()

Client - 172.173.224.235
send(IP(dst="155.248.226.213")/ICMP())

p = sr1(IP(dst="155.248.226.213")/ICMP()) 
server - 155.248.226.213:
sudo tcpdump -i ens3 src host 172.173.224.235

