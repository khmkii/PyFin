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
            self.discount_matrix[row][column] = 1 / ( 1 + ( lower_value / 100 ) )
            if column > 0:
                multiple = 2
                row -= multiple
                while row >= 0:
                    value = lower_value * np.e ** (multiple * self.volatility)
                    self.discount_matrix[row][column] = 1 / ( 1 + ( value / 100 ) )
                    row -= multiple
                    multiple += 2

    def __init__(self, volatility, base_rates):
        self.volatility = volatility / 100
        self.base_rates = base_rates
        self.levels = len(base_rates)
        self.center = self.levels - 1
        self.discount_matrix = np.zeros(shape=((self.levels * 2) - 1, self.levels))
        self.calibrated = False
        self.recalibrate()

    def value(self, coupon, face_value):
        shape = self.discount_matrix.shape()
        # may have to work with transpose of matrix
        # iterate over elements in rows/columns if not zero perform discount

    def calibrate(self):
        pass
