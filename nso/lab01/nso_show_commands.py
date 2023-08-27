"""

Output:
[developer@nso ~]$ python3 nso_show_commands.py

Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.175    YES NVRAM  up                    up
GigabitEthernet2       172.16.252.21   YES NVRAM  up                    up
GigabitEthernet3       172.16.252.25   YES NVRAM  up                    up
GigabitEthernet4       172.16.252.2    YES NVRAM  up                    up
GigabitEthernet5       172.16.252.10   YES NVRAM  up                    up
GigabitEthernet6       172.16.252.17   YES NVRAM  up                    up
Loopback0              unassigned      YES unset  administratively down down
dist-rtr01#
"""

import ncs

with ncs.maapi.single_read_trans('admin', 'python', groups=['ncsadmin']) as t:
    root = ncs.maagic.get_root(t)
    device_cdb = root.devices.device["dist-rtr01"]
    input1 = device_cdb.live_status.ios_stats__exec.any.get_input()
    input1.args = ["show ip interface brief"]
    show_command = device_cdb.live_status.ios_stats__exec.any(input1).result
    print (show_command)