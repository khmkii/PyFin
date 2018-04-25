import math
import numpy as np
import random
import unittest

from binomial_tree import BinomialTree


class BinomialTreeTests(unittest.TestCase):

    def setUp(self):
        self.initial_test_matrix = np.array([
            [0.0, 0.0, 8.325],
            [0.0, 4.69381, 0.0],
            [2.0, 0.0, 6.167],
            [0.0, 3.47726022, 0.0],
            [0.0, 0.0, 4.56862597],
        ])

    def test_initial_calibration(self):
        btree = BinomialTree(15, [2, 4.04, 6.167])
        self.assertTrue(np.allclose(
                btree.rates_matrix,
                self.initial_test_matrix,
                rtol=1e-3
            )
        )



if __name__ == '__main__':
    unittest.main()
