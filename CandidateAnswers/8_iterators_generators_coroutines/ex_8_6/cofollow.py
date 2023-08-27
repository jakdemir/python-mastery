# cofollow.py
import os
import time

# Data source
def follow(filename,target):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line != '':
                target.send(line)
            else:
                time.sleep(0.1)

# Decorator for coroutine functions
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args,**kwargs):
        f = func(*args,**kwargs)
        f.send(None)
        return f
    return start

# Sample coroutine
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)

def receive(expected_type):
    msg = yield
    assert isinstance(msg, expected_type), 'Expected type %s' % (expected_type)
    return msg

# if __name__ == '__main__':
#follow('Data/stocklog.csv',printer())
    # from cofollow import printer
    # p = printer()
    # p.send('hello')
    # p.send(42)
    # p.throw(ValueError('It failed'))
    # try:
    #     int('n/a')
    # except ValueError as e:
    #     p.throw(e)
