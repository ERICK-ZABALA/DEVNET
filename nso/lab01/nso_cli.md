+ CLI Commands NSO

[developer@nso ~]$ 
[developer@nso ~]$ 
[developer@nso ~]$ ncs_cli

User developer last logged in 2023-08-06T02:21:31.319277+00:00, to nso, from 10.10.20.49 using rest-https
developer connected from 10.20.0.16 using ssh on nso
developer@ncs# show devices list
NAME             ADDRESS       DESCRIPTION  NED ID                ADMIN STATE  
-----------------------------------------------------------------------------
core-rtr01       10.10.20.173  -            cisco-iosxr-cli-7.44  unlocked     
core-rtr02       10.10.20.174  -            cisco-iosxr-cli-7.44  unlocked     
dist-rtr01       10.10.20.175  -            cisco-ios-cli-6.90    unlocked     
dist-rtr02       10.10.20.176  -            cisco-ios-cli-6.90    unlocked     
dist-sw01        10.10.20.177  -            cisco-nx-cli-5.23     unlocked     
dist-sw02        10.10.20.178  -            cisco-nx-cli-5.23     unlocked     
edge-firewall01  10.10.20.171  -            cisco-asa-cli-6.17    unlocked     
edge-sw01        10.10.20.172  -            cisco-ios-cli-6.90    unlocked     
internet-rtr01   10.10.20.181  -            cisco-ios-cli-6.90    unlocked     
developer@ncs# devices device dist-rtr01 ?
Possible completions:
  add-capability         This action adds a capability to the list of capabilities.
  capability             A list of capabil...


developer@ncs# devices device dist-rtr01 live-status exec any show ip interface brief
result
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.175    YES NVRAM  up                    up
GigabitEthernet2       172.16.252.21   YES NVRAM  up                    up
GigabitEthernet3       172.16.252.25   YES NVRAM  up                    up
GigabitEthernet4       172.16.252.2    YES NVRAM  up                    up
GigabitEthernet5       172.16.252.10   YES NVRAM  up                    up
GigabitEthernet6       172.16.252.17   YES NVRAM  up                    up
Loopback0              unassigned      YES unset  administratively down down
dist-rtr01#
developer@ncs#

One trick to note is that at this point, you can also save the output using the | save option appended at the end of your command. It will save the file in the directory where you initiated the NSO CLI, such as devices device dist-rtr01 live-status exec any show ip interface brief | save sh-ip-br.txt:

developer@ncs# devices device dist-rtr01 live-status exec any show ip interface brief | save sh-ip-br.txt
developer@ncs# exit

[developer@nso ~]$ ls
Desktop    shutdown.sh
Downloads  sh-ip-br.txt

[developer@nso ~]$ cat sh-ip-br.txt
result
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.175    YES NVRAM  up                    up
GigabitEthernet2       172.16.252.21   YES NVRAM  up                    up
GigabitEthernet3       172.16.252.25   YES NVRAM  up                    up
GigabitEthernet4       172.16.252.2    YES NVRAM  up                    up
GigabitEthernet5       172.16.252.10   YES NVRAM  up                    up
GigabitEthernet6       172.16.252.17   YES NVRAM  up                    up
Loopback0              unassigned      YES unset  administratively down down
dist-rtr01#
[developer@nso ~]$