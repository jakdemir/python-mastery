# reader.py
import csv
import logging

def csv_as_dicts_noheader(file: str, types: list[type], headers: list[str]) -> list[str]:
    records = []
    rows = csv.reader(file)
    for row in rows:
        record = {name: func(val)
                  for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records


def csv_as_instances_noheader(file: str, cls: type, headers: list[str]) -> list[str]:
    records = []
    rows = csv.reader(file)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records


def csv_as_dicts(file: str, types: list[str]) -> list[str]:
    records = []
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
        record = {name: func(val)
                  for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records


def csv_as_instances(file: str, cls: type) -> list[str]:
    records = []
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records


def read_csv_as_dicts(filename: str, types: type) -> list[str]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for index, row in enumerate(rows):
            try:
                record = {name: func(val)
                        for name, func, val in zip(headers, types, row)}
                records.append(record)
            except Exception as e:
                logging.warning(f'Row {index}: Bad row: {row}')
                logging.debug(e)
    return records


def read_csv_as_instances(filename: str, cls: type) -> list[str]:
    '''
    Read CSV data into a list of instances
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records

def make_dict(headers, row):
    return dict(zip(headers, row))


def convert_csv(lines, func):
    records = []
    headers = next(lines)
    for row in lines:
        print(func(headers.split(","), row.split(",")))
        records.append(func(headers, row))
    return records


if __name__ == '__main__':
    import io
    import os
    import gzip
    import reader

    # filedecoded = gzip.open('Data/portfolio.csv.gz')
    # file = io.TextIOWrapper(filedecoded, encoding='utf-8')
    # port = reader.csv_as_dicts(file, [str, int, float])
    # print(port)

    # file = open('Data/portfolio_noheader.csv')
    # header = ['name', 'shares', 'price']
    # port = reader.csv_as_dicts_noheader(file, [str, int, float], header)
    # print(port)


    # lines = open('Data/portfolio.csv')
    # convert_csv(lines, make_dict)
    logging.basicConfig(level=logging.DEBUG)
    port = read_csv_as_dicts('Data/missing.csv', types=[str, int, float])

    print(len(port))