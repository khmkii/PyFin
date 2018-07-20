import math
import numpy as np
import random
import unittest

from BinomialInterestRateTree import BinomialTree


class BinomialTreeTests(unittest.TestCase):

    def setUp(self):
        self.initial_test_matrix = np.array([])

    def test_initial_calibration(self):
        btree = BinomialTree(15, [2, 4.04, 6.167])
        # self.assertTrue(np.allclose(
        #         btree.rates_matrix,
        #         self.initial_test_matrix,
        #         rtol=1e-3
        #     )
        # )
        print(btree.discount_matrix)



if __name__ == '__main__':
    unittest.main()
