# stock.py

from structure import Structure, validate_attributes
from validate import  String, PositiveInteger, PositiveFloat

#@validate_attributes
class Stock(Structure):
    #_fields = ('name', 'shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveFloat):
        self.shares -= nshares

# Stock.create_init()

if __name__ == '__main__':
    # s = Stock.from_row(['GOOG', '100', '490.1'])

    s = Stock('GOOG', 100, 490.1)
    s.sell(25)
    s.sell(-25)
    print(s)
