#!/usr/bin/python3
import pytest

class router(object):
    def __init__(self, hostname=None, os=None, device_type='cisco_ios'):
        self.hostname = hostname
        self.os = os
        self.device_type = device_type
        self.interfaces = 24
    
def test_defaults():
    r1 = router()
    assert r1.hostname == None
    assert r1.os == None
    assert r1.device_type == 'cisco_ios'
    assert r1.interfaces == 24

devices = {
    'nx-osv-1': {
        'os': 'nxos_version'
    }
}

def test_non_defaults():
    r2 = router(hostname='lax-r2', os='nxos', device_type='cisco_nxos')
    assert r2.hostname == 'lax-r2'
    assert r2.os == 'nxos'
    assert r2.device_type == 'cisco_nxos'
    assert r2.interfaces == 24

def test_version():
    assert devices['nx-osv-1']['os'] == "nxos_version"



"""
python3 -m pytest -v test_router_00.py
======================================== test session starts ========================================
platform linux -- Python 3.11.4, pytest-7.4.2, pluggy-1.3.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/devnet/devnet/DEVNET/tdd/py_test
plugins: anyio-3.7.0
collected 3 items                                                                                   

test_router_00.py::test_defaults PASSED                                                       [ 33%]
test_router_00.py::test_non_defaults PASSED                                                   [ 66%]
test_router_00.py::test_version PASSED                                                        [100%]

========================================= 3 passed in 0.02s =========================================

"""