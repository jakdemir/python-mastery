from typing import Any


class Structure:
    _fields = ()

    def __init__(self, *args) -> None:
        # This can be improved with zip
        setattr(self, self._fields[0], args[0])
        setattr(self, self._fields[1], args[1])
        setattr(self, self._fields[2], args[2])

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({getattr(self, self._fields[0])}, {getattr(self, self._fields[1])}, {getattr(self, self._fields[2])})'

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in self._fields or __name.startswith('_'):
            super.__setattr__(self, __name, __value)
        else:
            raise AttributeError('Not attribute %s', __name)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

    def __init__(self, *args) -> None:
        if len(args) == 3:
            super().__init__(*args)
        else:
            raise TypeError("Expected 3 arguments")


class Date(Structure):
    _fields = ('year', 'month', 'day')


if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.1)
    print(s.name)
    print(s.shares)
    print(s.price)

    # s = Stock('AA',50)

    print(s)

    s._share = 60

    print(s._share)