import unittest

import numpy as np

from utils.distance import eucludian_distance


class DistanceTest(unittest.TestCase):
    def test_2d(self):
        v1 = np.array([2, 2])
        v2 = np.array([2, 2])
        final = eucludian_distance(v1, v2)
        self.assertEqual(final, 0)

    def test_16(self):
        v1 = np.zeros(16)
        v2 = np.ones(16)
        final = eucludian_distance(v1, v2)
        self.assertEqual(final, 4)

    def test_128(self):
        v1 = np.ones(128)
        v2 = np.ones(128) * -1
        final = eucludian_distance(v1, v2)
        print(final)
        self.assertGreater(final, 22)
        self.assertLess(final, 23)