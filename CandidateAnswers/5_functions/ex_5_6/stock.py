# stock.py

class Stock:
    __slots__ = ['name', '_shares', '_price']
    _types = [str, int, float]

    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Value should be correct type {value}")
        elif value <= 0:
            raise ValueError(f"Value should be greater than ZERO {value}")
        else:
            self._shares = value
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Value should be correct type {value}")
        elif value <= 0:
            raise ValueError(f"Value should be greater than ZERO {value}")
        else:
            self._price = value

    @property
    def cost(self):
        return self.shares * self.price

    @classmethod
    def from_row(cls, row):
        values = [type(value) for type, value in zip(cls._types, row)]
        return cls(*values)

    def __init__(self, name, shares, price) -> None:
        self.name = self._types[0](name)
        self.shares = self._types[1](shares)
        self.price = self._types[2](price)

    def sell(self, shares):
        if self.shares >= shares:
            self.shares -=  shares
        else:
            print(f'Not enough shares porfolio: {self.shares}, sell req: {shares}')

    def __repr__(self) -> str:
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def __str__(self) -> str:
        return f"NAME: {self.name}, SHARES: {self.shares}, PRICE: {self.price}"
    
    def __eq__(self, other: object):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == (other.name, other.shares, self.price))
    