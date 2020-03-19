import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../challenge/two")

from challenge_two import append

class TestChallenge(unittest.TestCase):

    def _check_append(self, l, item, solution):
        append(l, item)
        self.assertEqual(l, solution)

    def test(self):
        self._check_append([1, 2, 3], 4, [1, 2, 3, 4])
        self._check_append(['a','b', 'c'], 'd', ['a','b','c','d'])


if __name__ == '__main__':
    unittest.main()