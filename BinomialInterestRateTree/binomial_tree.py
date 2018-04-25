import logging
import numpy as np


class BinomialTree:

    def recalibrate(self, base_rates=None):
        if base_rates is None:
            base_rates = self.base_rates
        for column in range(0, self.levels):
            lower_value = base_rates[column] * np.e ** (
                -1 * column * self.volatility
            )
            row = self.center + column
            self.rates_matrix[row][column] = lower_value
            if column > 0:
                multiple = 2
                row -= multiple
                while row >= 0:
                    value = lower_value * np.e ** (multiple * self.volatility)
                    self.rates_matrix[row][column] = value
                    row -= multiple
                    multiple += 2

    def __init__(self, volatility, base_rates):
        self.volatility = volatility / 100
        self.base_rates = base_rates
        self.levels = len(base_rates)
        self.center = self.levels - 1
        self.rates_matrix = np.zeros(shape=((self.levels * 2) - 1, self.levels))
        self.recalibrate()
