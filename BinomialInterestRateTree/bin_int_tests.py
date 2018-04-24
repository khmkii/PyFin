import math
import random
import unittest

from binomial_tree import BinomialTree, Node


class BinomialTreeTests(unittest.TestCase):

    def setUp(self):
        self.rates = [1, 1.402, 1.351, 1.864, 3.5]

    def tearDown(self):
        del self.rates

    def test_binomial_tree_lower_population(self):
        btree = BinomialTree(10, self.rates)
        self.assertEqual(
            btree.root_node.value,
            self.rates[0]
        )
        next = btree.root_node.down_child
        factor = 1
        while next is not None:
            self.assertEqual(
                next.value,
                self.rates[factor] * ( math.e ** (-1 * factor) )
            )
            factor += 1
            next = next.down_child

    def test_binomial_tree_upper_population(self):
        pass


if __name__ == '__main__':
    unittest.main()
