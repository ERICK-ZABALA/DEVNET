# Monitoring with Python
¿Qué ocurrió en el lapso de tiempo desde que la red funcionaba correctamente hasta que surgió un problema? Es probable que revises tu herramienta de monitoreo para verificar si alguno de los indicadores clave experimentó cambios en las últimas horas."

hardware, software, human mistakes.
information >>> interpretation from it

Python Library:

+ Matplotlib
+ Pygal

+ Python Integrated with MRTG and Cacti

# Install SNMP
$ sudo apt-get update
$ sudo apt-get install snmp

+ ROUTER
core-rtr01 - ios xr
router: 10.10.20.173

RP/0/RP0/CPU0:core-rtr01(config)#snmp-server community secret RO
RP/0/RP0/CPU0:core-rtr01(config)#commit

+ SERVER
server snmp: 192.226.134.67

+ $ snmpwalk -v2c -c secret 10.10.20.173 .1.3.6.1.4.1.9

devnet@pc1$ snmpwalk -v2c -c secret 10.10.20.173 .1.3.6.1.4.1.9
iso.3.6.1.4.1.9.9.6.1.1.1.1.10.10.20.173.23.192.168.254.11.5470 = Counter32: 345
iso.3.6.1.4.1.9.9.6.1.1.1.2.10.10.20.173.23.192.168.254.11.5470 = Counter32: 2896
iso.3.6.1.4.1.9.9.6.1.1.1.3.10.10.20.173.23.192.168.254.11.5470 = Counter32: 294
iso.3.6.1.4.1.9.9.6.1.1.1.4.10.10.20.173.23.192.168.254.11.5470 = Counter32: 209

# Process to Install PyAsn1 and PySNMP

Library:

PySNMP requires the PyASN1 package
venv

devnet@PC1 ~/devnet/DEVNET/monitoring $ python3 -m venv venv
devnet@PC1 ~/devnet/DEVNET/monitoring $ source venv/bin/activate
(venv) devnet@PC1 ~/devnet/DEVNET/monitoring $ mkdir tmp
(venv) devnet@PC1 ~/devnet/DEVNET/monitoring $ cd tmp/
(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp $ git clone https://github.com/etingof/pyasn1.git
Cloning into 'pyasn1'...

+ move to other version

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp $ cd pyasn1

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pyasn1 $ ls

CHANGES.rst             docs         MANIFEST.in  README.md         setup.cfg  tests       TODO.rst
devel-requirements.txt  LICENSE.rst  pyasn1       requirements.txt  setup.py   THANKS.txt  tox.ini

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pyasn1 $ git checkout 0.2.3

Note: switching to '0.2.3'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at a95b62a release 0.2.3
(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pyasn1 $ ls
CHANGES.rst  LICENSE.rst  pyasn1     requirements.txt  setup.py  THANKS.txt
doc          MANIFEST.in  README.md  setup.cfg         tests     TODO.rst

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pyasn1 $ python setup.py install 

# Install PySnmp

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pyasn1 $ cd ..

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp $ ls

pyasn1

(venv) devnet@PC1 /monitoring/tmp $ git clone https://github.com/etingof/pysnmp

Cloning into 'pysnmp'...
remote: Enumerating objects: 18718, done.
remote: Total 18718 (delta 0), reused 0 (delta 0), pack-reused 18718
Receiving objects: 100% (18718/18718), 3.08 MiB | 1.26 MiB/s, done.
Resolving deltas: 100% (13158/13158), done.

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp $ ls
pyasn1  pysnmp

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp $ cd pysnmp

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pysnmp $ git checkout v4.3.10

Note: switching to 'v4.3.10'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at c4ab03e1 4.3.10

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pysnmp $ ls

CHANGES.txt  examples     MANIFEST.in  README.md         runtests.sh  setup.py    TODO.txt
docs         LICENSE.txt  pysnmp       requirements.txt  setup.cfg    THANKS.txt

(venv) devnet@PC1 /tmp/pysnmp $ python setup.py install

Using /home/devnet/devnet/DEVNET/monitoring/venv/lib/python3.11/site-packages/pyasn1-0.2.3-py3.11.egg
Finished processing dependencies for pysnmp==4.3.10

$ python
>>> from pysnmp.entity.rfc3413.oneliner import cmdgen
>>> cmdGen = cmdgen.CommandGenerator()
>>> cisco_contact_info_oid = "1.3.6.1.4.1.9.2.1.61.0"

errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
cmdgen.CommunityData('secret'),
cmdgen.UdpTransportTarget(('10.10.20.173', 161)),
cisco_contact_info_oid)
>>> for name, val in varBinds:
print('%s=%s' % (name.prettyPrint(), str(val)))

Flow Configuration in Python3

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pysnmp $ python
Python 3.11.4 (main, Jun  7 2023, 10:13:09) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> from pysnmp.entity.rfc3413.oneliner import cmdgen
>>> cmdGen = cmdgen.CommandGenerator()
>>> cisco_contact_info_oid = "1.3.6.1.4.1.9.2.1.61.0"
>>> errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
... cmdgen.CommunityData('secret'),
... cmdgen.UdpTransportTarget(('10.10.20.173', 161)),
... cisco_contact_info_oid)
>>> for name, val in varBinds:
...     print('%s=%s' % (name.prettyPrint(), str(val)))
... 
SNMPv2-SMI::enterprises.9.2.1.61.0=
>>> 


# Server SNMP Linux

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pysnmp $ snmpwalk -v2c -c secret 10.10.20.173 1.3.6.1.2.1.2.2.1.2
iso.3.6.1.2.1.2.2.1.2.1 = STRING: "Null0"
iso.3.6.1.2.1.2.2.1.2.3 = STRING: "MgmtEth0/RP0/CPU0/0"
iso.3.6.1.2.1.2.2.1.2.4 = STRING: "Loopback0"
iso.3.6.1.2.1.2.2.1.2.7 = STRING: "GigabitEthernet0/0/0/0"
iso.3.6.1.2.1.2.2.1.2.8 = STRING: "GigabitEthernet0/0/0/1"


(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pysnmp $ snmpwalk -v2c -c secret 10.10.20.173 1.3.6.1.2.1.2.2.1.17.7
iso.3.6.1.2.1.2.2.1.17.7 = Counter32: 700

# Verifying

RP/0/RP0/CPU0:core-rtr01(config)#do sh int gi0/0/0/0 | i packets
Sun Sep  3 18:44:19.046 UTC
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     708 packets input, 77880 bytes, 10 total input drops
     Received 0 broadcast packets, 0 multicast packets
 >   700 packets output, 76864 bytes, 0 total output drops
     Output 1 broadcast packets, 0 multicast packets


# CRON Service Linux 

With this service we can execute code in python each 5 min.

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pysnmp $ pwd
/home/devnet/devnet/DEVNET/monitoring/tmp/pysnmp

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pysnmp$ sudo service cron status

cron is not running ... failed!
(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pysnmp$ sudo service cron restart

Restarting periodic command scheduler: cronStopping periodic command scheduler: cron.
Starting periodic command scheduler: cron.

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pysnmp $ sudo service cron status
cron is running.

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring/tmp/pysnmp $ crontab -e
no crontab for devnet - using an empty one

Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.tiny

Choose 1-2 [1]: 1
crontab: installing new crontab

# crontab configuration -- put in final line in the document

*/5 * * * * /home/devnet/devnet/DEVNET/monitoring/venv/bin/python /home/devnet/devnet/DEVNET/monitoring/tmp/pysnmp/pysnmp1.py >> /home/devnet/devnet/DEVNET/monitoring/tmp/pysnmp/archivo.log 2>&1

# to verify is working  see file archivo.log
SNMPv2-MIB::sysName.0 = core-rtr01.virl.info
SNMPv2-SMI::mib-2.2.2.1.10.7 = 147516
SNMPv2-SMI::mib-2.2.2.1.11.7 = 1294
SNMPv2-SMI::mib-2.2.2.1.16.7 = 146354
SNMPv2-SMI::mib-2.2.2.1.17.7 = 1284
{'Time': '2023-09-03T20:17:02.357532', 'hostname': 'core-rtr01.virl.info', 'Gig0-0_In_Octet': '147516', 'Gig0-0_In_uPackets': '1294', 'Gig0-0_Out_Octet': '146354', 'Gig0-0_Out_uPackets': '1284'}

# Python Data Visualization

pip install matplotlib

Python 3.11.4 (main, Jun  7 2023, 10:13:09) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import matplotlib.pyplot as plt
>>> plt.plot([0,1,2,3,4], [0,10,20,30,40])
[<matplotlib.lines.Line2D object at 0x7f046ef0f890>]
>>> plt.ylabel('Something on Y')
Text(0, 0.5, 'Something on Y')
>>> plt.xlabel('Something on X')
Text(0.5, 0, 'Something on X')
>>> plt.show()
plt.savefig('figure1.png')
plt.savefig('figure1.pdf')

# PYGAL 

pip install pygal

>>> import pygal
>>> line_chart = pygal.Line()
>>> line_chart.title = 'Browser usage evolution (in %)'
>>> line_chart.x_labels = map(str, range(2002, 2013))
>>> line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4,
45.5, 46.3, 42.8, 37.1])
<pygal.graph.line.Line object at 0x7f4883c52b38>
>>> line_chart.add('Chrome', [None, None, None, None, None, None, 0,
3.9, 10.8, 23.8, 35.3])
<pygal.graph.line.Line object at 0x7f4883c52b38>
>>> line_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7,
44.8, 36.2, 26.6, 20.1])
<pygal.graph.line.Line object at 0x7f4883c52b38>
>>> line_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9,
5.8, 6.7, 6.8, 7.5])
<pygal.graph.line.Line object at 0x7f4883c52b38>
>>> line_chart.render_to_file('pygal_example_1.svg')

# CACTI

Debido a que Cacti es una herramienta integral que incluye una interfaz web, scripts de recopilación y una base de datos en el backend, a menos que ya tengas experiencia con Cacti, te recomendaría instalar la herramienta en una máquina virtual independiente en nuestro laboratorio. La instalación en Ubuntu es sencilla cuando se utiliza APT en la máquina virtual de gestión de Ubuntu.

