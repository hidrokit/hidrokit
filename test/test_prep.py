import pytest

import hidrokit
from hidrokit.prep import read


def fun(n):
    return n + 1


def test_fun():
    assert fun(1) == 2, "Should be 2"
    assert fun(2) == 4, "Should be 2"
    assert fun(3) == 4, "Should be 2"

# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(fun(3), 4)
