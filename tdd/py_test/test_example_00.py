#!/usr/bin/python3
import pytest

def test_passing():
    assert(1, 2, 3) == (1, 2, 3)

def test_failing():
    assert(1, 2, 3) == (3, 2, 1)


"""
$ python3 -m pytest -v test_example_00.py

======================================== test session starts ========================================
platform linux -- Python 3.11.4, pytest-7.4.2, pluggy-1.3.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/devnet/devnet/DEVNET/tdd/py_test
plugins: anyio-3.7.0
collected 2 items                                                                                   

test_example_00.py::test_passing PASSED                                                       [ 50%]
test_example_00.py::test_failing FAILED                                                       [100%]

============================================= FAILURES ==============================================
___________________________________________ test_failing ____________________________________________

    def test_failing():
>       assert(1, 2, 3) == (3, 2, 1)
E       assert (1, 2, 3) == (3, 2, 1)
E         At index 0 diff: 1 != 3
E         Full diff:
E         - (3, 2, 1)
E         ?  ^     ^
E         + (1, 2, 3)
E         ?  ^     ^

test_example_00.py:8: AssertionError
====================================== short test summary info ======================================
FAILED test_example_00.py::test_failing - assert (1, 2, 3) == (3, 2, 1)
==================================== 1 failed, 1 passed in 0.40s ====================================


"""