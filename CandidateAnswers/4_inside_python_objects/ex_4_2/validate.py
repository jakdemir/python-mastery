#validate.py

class Validator:
    @classmethod
    def check(cls, value):
        return value
    
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)
    
class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type =float

class String(Typed):
    expected_type = str

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value <= 0:
            raise ValueError(f'Value should be greater than zero {value}')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError(f'Len of value should be greater than zero')
        return super().check(value)

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, PositiveInteger):
    pass

class NonEmptyString(String, NonEmpty):
    pass

class Stock:
    __slots__ = ['name', '_shares', '_price']
    _types = [str, int, float]

    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        # if not isinstance(value, self._types[1]):
        #     raise ValueError(f"Value should be correct type {value}")
        # elif value <= 0:
        #     raise ValueError(f"Value should be greater than ZERO {value}")
        # else:
        self._shares = Positive.check(value)
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise ValueError(f"Value should be correct type {value}")
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
