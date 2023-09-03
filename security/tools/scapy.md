# SCAPY

That is a tool that permit capture packet similar to wireshark for python and improve you automation network.

# Install SCAPY

$ git clone https://github.com/secdev/scapy.git
$ cd scapy
$ sudo apt-get install python3-pip
$ pip3 install setuptools
$ sudo python3 setup.py install

$ sudo apt-get install libpcap-dev

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

ex2: p = sr1(IP(dst="8.8.8.8")/UDP()/DNS(rd=1,qd=DNSQR(qname="www.google.com"))) 


# TEST SCAPY

* Send one packet echo ICMP
                                      
>>> send(IP(dst="155.248.226.213")/ICMP())
.
Sent 1 packets.

* Store one packet echo-request in var p

>>> p = sr1(IP(dst="155.248.226.213")/ICMP()) 
Begin emission:
Finished sending 1 packets.
*
Received 1 packets, got 1 answers, remaining 0 packets

>>> type (p)
<class 'scapy.layers.inet.IP'>

>>> ans, unans = sr(IP(dst="155.248.226.213")/ICMP()) 
Begin emission:
Finished sending 1 packets.
*
Received 1 packets, got 1 answers, remaining 0 packets
>>> type(ans)
<class 'scapy.plist.SndRcvList'>
>>> type(unans)
<class 'scapy.plist.PacketList'>


>>> for i in ans:
...     print(type(i))
... 
<class 'scapy.plist.QueryAnswer'>
>>> 
>>> for i in ans:
...     print(i)
... 
QueryAnswer(query=<IP  frag=0 proto=icmp dst=155.248.226.213 |<ICMP  |>>, answer=<IP  version=4 ihl=5 tos=0x0 len=28 id=28375 flags= frag=0 ttl=56 proto=icmp chksum=0x4b22 src=155.248.226.213 dst=172.30.157.251 |<ICMP  type=echo-reply code=0 chksum=0xffff id=0x0 seq=0x0 unused=b'' |>>)

>>> p = sr1(IP(dst="8.8.8.8")/UDP()/DNS(rd=1,qd=DNSQR(qname="www.google.com")))
Begin emission:
Finished sending 1 packets.
.*
Received 2 packets, got 1 answers, remaining 0 packets
>>> p
<IP  version=4 ihl=5 tos=0x0 len=76 id=43085 flags= frag=0 ttl=123 proto=udp chksum=0x3d2a src=8.8.8.8 dst=172.30.157.251 |<UDP  sport=domain dport=domain len=56 chksum=0x1aa9 |<DNS  id=0 qr=1 opcode=QUERY aa=0 tc=0 rd=1 ra=1 z=0 ad=0 cd=0 rcode=ok qdcount=1 ancount=1 nscount=0 arcount=0 qd=[<DNSQR  qname=b'www.google.com.' qtype=A qclass=IN |>] an=[<DNSRR  rrname=b'www.google.com.' type=A rclass=IN ttl=136 rdata=172.217.13.164 |>] |>>>

+ Capture packet icmp as sniffer

>>> a=sniff(filter="icmp", count=5)
>>> a.show()
0000 Ether / IP / ICMP 172.30.157.251 > 8.8.8.8 echo-request 0 / Raw
0001 Ether / IP / ICMP 8.8.8.8 > 172.30.157.251 echo-reply 0 / Raw
0002 Ether / IP / ICMP 172.30.157.251 > 8.8.8.8 echo-request 0 / Raw
0003 Ether / IP / ICMP 8.8.8.8 > 172.30.157.251 echo-reply 0 / Raw
0004 Ether / IP / ICMP 172.30.157.251 > 8.8.8.8 echo-request 0 / Raw
>>> 
>>> 
>>> for packet in a:
...     print(packet.show())
... 
###[ Ethernet ]### 
  dst       = 00:15:5d:04:ab:03
  src       = 00:15:5d:18:a3:e0
  type      = IPv4
###[ IP ]### 
     version   = 4
     ihl       = 5
     tos       = 0x0
     len       = 84
     id        = 3580
     flags     = DF
     frag      = 0
     ttl       = 64
     proto     = icmp
     chksum    = 0xd283
     src       = 172.30.157.251
     dst       = 8.8.8.8
     \options   \
###[ ICMP ]### 
        type      = echo-request
        code      = 0
        chksum    = 0xb746
        id        = 0x4647
        seq       = 0x1
        unused    = b''
###[ Raw ]### 
           load      = b'w\xf3\xf3d\x00\x00\x00\x00\xceE\x02\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'

None
###[ Ethernet ]### 
  dst       = 00:15:5d:18:a3:e0
  src       = 00:15:5d:04:ab:03
  type      = IPv4
###[ IP ]### 
     version   = 4
     ihl       = 5
     tos       = 0x0
     len       = 84
     id        = 0
     flags     = 
     frag      = 0
     ttl       = 118
     proto     = icmp
     chksum    = 0xea7f
     src       = 8.8.8.8
     dst       = 172.30.157.251
     \options   \
###[ ICMP ]### 
        type      = echo-reply
        code      = 0
        chksum    = 0xbf46
        id        = 0x4647
        seq       = 0x1
        unused    = b''
###[ Raw ]### 
           load      = b'w\xf3\xf3d\x00\x00\x00\x00\xceE\x02\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'

None
###[ Ethernet ]### 
  dst       = 00:15:5d:04:ab:03
  src       = 00:15:5d:18:a3:e0
  type      = IPv4
###[ IP ]### 
     version   = 4
     ihl       = 5
     tos       = 0x0
     len       = 84
     id        = 3665
     flags     = DF
     frag      = 0
     ttl       = 64
     proto     = icmp
     chksum    = 0xd22e
     src       = 172.30.157.251
     dst       = 8.8.8.8
     \options   \
###[ ICMP ]### 
        type      = echo-request
        code      = 0
        chksum    = 0x9a40
        id        = 0x4647
        seq       = 0x2
        unused    = b''
###[ Raw ]### 
           load      = b'x\xf3\xf3d\x00\x00\x00\x00\xeaJ\x02\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'

None
###[ Ethernet ]### 
  dst       = 00:15:5d:18:a3:e0
  src       = 00:15:5d:04:ab:03
  type      = IPv4
###[ IP ]### 
     version   = 4
     ihl       = 5
     tos       = 0x0
     len       = 84
     id        = 0
     flags     = 
     frag      = 0
     ttl       = 118
     proto     = icmp
     chksum    = 0xea7f
     src       = 8.8.8.8
     dst       = 172.30.157.251
     \options   \
###[ ICMP ]### 
        type      = echo-reply
        code      = 0
        chksum    = 0xa240
        id        = 0x4647
        seq       = 0x2
        unused    = b''
###[ Raw ]### 
           load      = b'x\xf3\xf3d\x00\x00\x00\x00\xeaJ\x02\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'

None
###[ Ethernet ]### 
  dst       = 00:15:5d:04:ab:03
  src       = 00:15:5d:18:a3:e0
  type      = IPv4
###[ IP ]### 
     version   = 4
     ihl       = 5
     tos       = 0x0
     len       = 84
     id        = 3738
     flags     = DF
     frag      = 0
     ttl       = 64
     proto     = icmp
     chksum    = 0xd1e5
     src       = 172.30.157.251
     dst       = 8.8.8.8
     \options   \
###[ ICMP ]### 
        type      = echo-request
        code      = 0
        chksum    = 0xcf37
        id        = 0x4647
        seq       = 0x3
        unused    = b''
###[ Raw ]### 
           load      = b'y\xf3\xf3d\x00\x00\x00\x00\xb4R\x02\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'

None
>>> 

# TCP PORT SCAN

Send SYN in order to receive SYN-ACK

p = sr1(IP(dst="155.248.226.213")/TCP(sport=677, dport=22, flags="S")) 

ans, unans = sr(IP(dst="155.248.226.213")/TCP(sport=680,dport=(20,22),flags="S"))

```python 
ans, unans = sr(IP(dst="155.248.226.213")/TCP(sport=680,dport=(20,22),flags="S"))
Begin emission:
Finished sending 3 packets.
.*..............^C
Received 16 packets, got 1 answers, remaining 2 packets
>>> for i in ans:
...     print(i)
... 
QueryAnswer(query=<IP  frag=0 proto=tcp dst=155.248.226.213 |<TCP  sport=680 dport=ssh flags=S |>>, answer=<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=56 proto=tcp chksum=0x79e4 src=155.248.226.213 dst=172.30.157.251 |<TCP  sport=ssh dport=680 seq=3775540677 ack=1 dataofs=6 reserved=0 flags=SA window=62720 chksum=0xab52 urgptr=0 options=[('MSS', 8960)] |>>)
>>> 
```

# Firewall Ubuntu Servers

+ Install UFW in server Ubuntu:

$ sudo apt-get install ufw
$ sudo ufw status
$ sudo ufw default outgoing
$ sudo ufw allow 22/tcp
$ sudo ufw allow www
$ sudo ufw default deny incoming

to verify status use:

$ sudo ufw status verbose Status: active

Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed) New
profiles: skip
To Action From
-- ------ ----
22/tcp ALLOW IN Anywhere
80/tcp ALLOW IN Anywhere
22/tcp (v6) ALLOW IN Anywhere (v6)
80/tcp (v6) ALLOW IN Anywhere (v6)