#!/usr/bin/env python

import task4
import unittest

class TestPrime(unittest.TestCase):
    def setUp(self):
        """Init"""

    def test_sting(self):
        self.assertEqual(task4.list('string with spaces'), 'string-with-spaces')

    def tearDown(self):
        """Finish"""

if __name__ == '__main__':
    unittest.main()
