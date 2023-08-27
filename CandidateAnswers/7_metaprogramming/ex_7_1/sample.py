# sample.py

from logcall import logged
from validate import Integer, validated

@validated
def add(x: Integer, y: Integer) -> Integer:
    return x + y

@validated
def sub(x: Integer, y: Integer) -> Integer:
    return x - y

if __name__ == '__main__':
    import sample
    sample.add(3, 4)
    sample.sub(2, 3)