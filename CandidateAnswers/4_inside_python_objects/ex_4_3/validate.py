#validate.py

class Validator:

    def __init__(self, name = None):
        self.name = name
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
    
    def __set_name__(self, cls, name):
        self.name = name

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
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price