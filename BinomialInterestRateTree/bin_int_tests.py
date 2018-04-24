import math
import random
import unittest

from binomial_tree import BinomialTree, Node


class BinomialTreeTests(unittest.TestCase):

    def setUp(self):
        self.rates = [1, 1.402, 1.351, 1.864, 3.5]
        self.volatility = random.randint(5, 20)

    def tearDown(self):
        del self.rates
        del self.volatility

    def test_binomial_tree_lower_population(self):
        btree = BinomialTree(self.volatility, self.rates)
        calculated_rates = [
            ra * (math.e ** (-1 * (en + 1) * (self.volatility / 100) ) ) for
            en, ra in enumerate(self.rates[1:])
        ]
        calculated_rates.insert(0, self.rates[0])
        binomial_rates = [btree.root_node.value]
        next = btree.root_node.down_child
        while next is not None:
            binomial_rates.append(next.value)
            next = next.down_child
        self.assertEqual(binomial_rates, calculated_rates)

    def test_binomial_tree_upper_population(self):
        btree = BinomialTree(self.volatility, self.rates)
        calculated_rates = [
            ra * (math.e ** (1 * (en + 1) * (self.volatility / 100) ) ) for
            en, ra in enumerate(self.rates[1:])
        ]
        calculated_rates.insert(0, self.rates[0])
        binomial_rates = [btree.root_node.value]
        next = btree.root_node.up_child
        while next is not None:
            binomial_rates.append(next.value)
            next = next.up_child
        self.assertEqual(binomial_rates, calculated_rates)


if __name__ == '__main__':
    unittest.main()
