# coticker.py
from structure import Structure

class Ticker(Structure):
    name = String()
    price =Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv

# This one is tricky. See solution for notes about it
@consumer
def to_csv(target):
    def producer():
        while True:
            yield line

    reader = csv.reader(producer())
    while True:
        line = yield
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        row = yield
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        record = yield
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        rec = yield
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)

if __name__ == '__main__':
    import csv
    from tableformat import create_formatter, print_table

    # # Old iterative
    # formatter = create_formatter('text')
    # lines = follow('Data/stocklog.csv')
    # rows = csv.reader(lines)
    # records = (Ticker.from_row(row) for row in rows)
    # negative = (rec for rec in records if rec.change < 0)
    # print_table(negative, ['name','price','change'], formatter)

    # #new coroutine
    # follow('Data/stocklog.csv',printer())
    fields = ['name','price','change']
    formatter = 'text'
    #declarative
    follow('Data/stocklog.csv', to_csv(create_ticker(negchange(ticker(formatter, fields)))))