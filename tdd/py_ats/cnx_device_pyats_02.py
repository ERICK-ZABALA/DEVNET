from pyats.topology import loader
from pyats import aetest
from genie import testbed

testbed = loader.load('testbed.yml')

testbed.devices

ios_1 = testbed.devices['RP/0/RP0/CPU0:ansible-cisco.iosxr.iosxr']
ios_1.connect(learn_hostname=True, log_stdout=True)

print('xr is connected = ', ios_1.connected)

print('ios versionn = ', ios_1.execute('show version'))

ios_1.disconnect()

class PingTestcase(aetest.Testcase):

    @aetest.setup
    def setup(self):
        self.device = ios_1
    
    @aetest.test.loop(destination=('1.1.1.100', '10.10.20.175'))
    def ping(self, destination):
        
        try:
            result = self.device.ping(destination)
            if result:
                self.passed('Ping to {} was successful'.format(destination))
            else:
                self.failed('Ping to {} failed'.format(destination))
        except Exception as e:
            self.failed('Error while pinging {}: {}'.format(destination, str(e)))

if __name__ == '__main__':
    aetest.main()