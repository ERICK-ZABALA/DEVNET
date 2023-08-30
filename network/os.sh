OS
To know OS
command: uname -a
$ uname -a
Linux codespaces-b04c0d 5.15.0-1041-azure #48-Ubuntu SMP Tue Jun 20 20:34:08 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

PYTHON
numeric: int, float, complex, bool
sequence: str, list, tuple, range
mapping: dict
sets: set, frozenset
none: null object (no value)

CLASS

"Process to initial variable via OOP in Python"
class switch(object):
    def __init__(self, name, vlan, description):
        self.name = name
        self.vlan = vlan
        self.description = description


sw1 = switch("SW-2960", "220", "Vlan 220 Administration")
sw1.name
sw1.vlan
sw1.description


### Proces Python ###
> class switch(object):
...     def __init__(self, name, vlan, description):
...         self.name = name
...         self.vlan = vlan
...         self.description = description
... 
>>> sw1 = switch("SW-2960", "220", "Vlan 220 Administration")
>>> sw1.name
'SW-2960'
>>> sw1.vlan
'220'
>>> sw1.description
'Vlan 220 Administration'
