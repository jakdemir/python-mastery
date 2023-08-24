# readrides.py

import csv

def read_rides_as_dictionary(filename):

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            record = {'route': row[0], 
                      'date' : row[1], 
                      'daytype' : row[2], 
                      'rides' : int(row[3])}

            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_dictionary('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())