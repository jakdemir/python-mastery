# sample.py

from logcall import logged, logformat
from validate import Integer, validated, enforce

@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    'Adds two things'
    return x + y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
    return x * y

class Spam:
    @logged
    def instance_method(self):
        pass

    @logged
    @classmethod
    def class_method(cls):
        pass

    @logged
    @staticmethod
    def static_method():
        pass

    @logged
    @property
    def property_method(self):
        pass

if __name__ == '__main__':

    add(3, 4)
    # mul(2,3)

    # s = Spam()
    # s.instance_method()