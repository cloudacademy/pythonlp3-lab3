import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../challenge/three")

from challenge_three import list_uniqueness

class TestChallenge(unittest.TestCase):

    def _check_list_uniqueness(self, l, length, unique):
        dictionary = list_uniqueness(l)
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(dictionary['list_length'], length)
        self.assertEqual(dictionary['unique_items'], unique)

    def test(self):
        self._check_list_uniqueness([1, 2, 2, 4], 4, 3)
        self._check_list_uniqueness(['a', 'a', 'a', 1], 4, 2)


if __name__ == '__main__':
    unittest.main()