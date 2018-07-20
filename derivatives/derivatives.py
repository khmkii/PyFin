import math
from scipy.stats import norm


class BSM:

    def __init__(self, price, strike, interest_rate, volatility, time):
        self.S = price
        self.X = strike
        self.r = interest_rate
        self.v = volatility
        self.T = time

    @property
    def d1(self):
        d1_numerator = math.log(
                self.S / self.X
            ) + self.r * self.T + ( ( self.v ** 2 * self.T ) / 2)
        d1_denominator = self.v * math.sqrt(self.T)

        return d1_numerator / d1_denominator

    @property
    def d2(self):
        return self.d1 - ( self.v * math.sqrt(self.T) )

    def call_price(self):
        return ( self.S * norm.cdf(self.d1) ) - (
            math.e ** ( -1 * self.r * self.T ) * self.X * norm.cdf(self.d2)
        )

    def put_price(self):
        return ( math.e ** ( -1 * self.r * self.T) * self.X * norm.cdf(-self.d2)
            ) - ( self.S * norm.cdf(-self.d1) )
