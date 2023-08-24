import csv
from collections.abc import MutableSequence 
from collections import defaultdict
import collections
from typing import Any
import tracemalloc
from sys import intern
from tableformat import TableFormatter, TextTableFormatter, CSVTableFormatter 


# reader.py


import csv
from abc import ABC, abstractmethod

class CSVParser(ABC):

    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass

class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)

def read_csv_as_dicts(filename, types):
    parser = DictCSVParser(types)
    return parser.parse(filename)

def read_csv_as_instances(filename, cls):
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)

portfolio = read_csv_as_dicts('Data/portfolio.csv', [str,int,float])
# for s in portfolio:
#     print(s)

class DataSource(list):
    def __init__(self):
        self.values = list()

    def append(self, header, types, row):
        # print("appending")
        record = {}
        for col_name, value, col_type in zip(header, row, types):
            record[col_name] = col_type(value)
        self.values.append(record)
    
    def __getitem__(self, idx):
        return self.values[idx]
    
    def __repr__(self):
        return self.values
    
    def __len__(self) -> int:
        return self.values.__len__()


def read_csv_as_columns(filepath, types):
    with open(filepath) as f:
        rows = csv.reader(f)
        header = next(rows)
        result = DataSource()
        for row in rows:
            #print(row)
            result.append(header, types, row)
    return result

# tracemalloc.start()
# data = read_csv_as_columns('Data/ctabus.csv', types=[intern,intern,intern, int])
# print(len(data))
# print(tracemalloc.get_traced_memory())