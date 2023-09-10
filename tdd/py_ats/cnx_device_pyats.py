from pyats.topology import loader

testbed = loader.load('testbed.yml')

testbed.devices

ios_1 = testbed.devices['RP/0/RP0/CPU0:ansible-cisco.iosxr.iosxr']

ios_1.connect()

print(ios_1.execute('show version'))


ios_1.disconnect()

