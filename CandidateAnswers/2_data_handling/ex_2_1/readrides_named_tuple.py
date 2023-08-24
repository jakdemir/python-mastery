# readrides.py

import csv
from collections import namedtuple

def read_rides_as_named_tuples(filename):
    '''
    Read the bus ride data as a list of named tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        Record = namedtuple('Record', ['route', 'date', 'daytype', 'rides'])  

        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Record(route,date,daytype,rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_named_tuples('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())