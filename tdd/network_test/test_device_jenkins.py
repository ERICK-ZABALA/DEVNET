#!/usr/bin/python3
import pytest

devices = {
    'nx-osv-1': {
        'os': 'nxos_version'
    }
}

def test_version():
    assert devices['nx-osv-1']['os'] == "nxos_version"

"""
python3 -m pytest -v test_device_jenkins.py 

======================================== test session starts ========================================
platform linux -- Python 3.11.4, pytest-7.4.2, pluggy-1.3.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/devnet/devnet/DEVNET/tdd/network_test
plugins: anyio-3.7.0
collected 1 item                                                                                    

test_device_jenkins.py::test_version PASSED                                                   [100%]

========================================= 1 passed in 0.68s =========================================

"""


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