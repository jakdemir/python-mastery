# stock.py

from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

# Stock.set_fields()
Stock.create_init()

if __name__ == '__main__':
    # import inspect
    # sig = inspect.signature(Stock)
    # print(tuple(sig.parameters))
    # s = Stock(name='GOOG', shares=100, price=490.1)
    # print(s)
    # print(s.name)
    # print(s.shares)