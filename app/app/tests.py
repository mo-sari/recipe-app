"""
sample tests

"""

from django.test import SimpleTestCase
from .calc import add, sub


class CaleTests(SimpleTestCase):
    """ Test the calc module"""
    def test_add_func(self):
        res = add(4, 3)
        self.assertEqual(res, 7)

    def test_sub_func(self):
        res = sub(4, 5)
        self.assertEqual(res, 1)
