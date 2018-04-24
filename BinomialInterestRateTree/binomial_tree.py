import math


class Node:
    def __init__(self, value, up, down, parent, level, root=False):
        self.value = value
        self.up_child = up
        self.down_child = down
        self.parent = parent
        self.level = level
        self.root = root

    def __str__(self):
        return str(self.value)


class BinomialTree:
    def __init__(self, volatility, base_rates):
        self.root_node = Node(
            level = 0,
            parent = None,
            value = base_rates[0],
            up = None,
            down = None,
            root = True,
        )
        current = self.root_node
        for period in range(1, len(base_rates)):
            current.down_child = Node(
                level = period,
                parent = current,
                value = base_rates[period] * (
                    math.e ** (-1 * period * volatility * 10 ** -2)
                ),
                up = None,
                down = None,
                root = False
            )
            current = current.down_child
        current = self.root_node
        for period in range(1, len(base_rates)):
            current.up_child = Node(
                level = period,
                parent = current,
                value = base_rates[period] * (
                    math.e ** (1 * period * volatility * 10 ** -2)
                ),
                up = None,
                down = None,
                root = False
            )
            current = current.up_child
