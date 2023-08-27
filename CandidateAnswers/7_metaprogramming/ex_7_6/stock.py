# stock.py

from structure import Structure
# from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

if __name__ == '__main__':
    from stock import Stock
    from reader import read_csv_as_instances
    portfolio = read_csv_as_instances('Data/portfolio.csv', Stock)
    print(portfolio)
