import stock
from abc import ABC, abstractmethod

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()
    
    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(" ".join("%10s" %type for type in headers))
        print(" ".join("_"*10 for type in headers))
    
    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(type for type in headers))

    def row(self, rowdata):
        print(",".join(str(column) for column in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr> <th>"+"</th> <th>".join(type for type in headers), end="</th> </tr>\n")

    def row(self, rowdata):
        print("<tr> <td>" + "</td> <td>".join(str(column) for column in rowdata), end="</td> </tr>\n")

def print_table(records, fields, formatter):
    if isinstance(formatter, TextTableFormatter) or isinstance(formatter, CSVTableFormatter) or isinstance(formatter, HTMLTableFormatter):
        formatter.headings(fields)
        for r in records:
            rowdata = [getattr(r, fieldname) for fieldname in fields]
            formatter.row(rowdata)
    else:
        raise ValueError(f"{formatter} is not valid :)")

def create_formatter(formatter_type):
    if formatter_type == 'html':
        return HTMLTableFormatter()
    elif formatter_type == 'csv':
        return CSVTableFormatter()
    elif formatter_type == 'text':
        return TextTableFormatter()
    else:
        ValueError(f'{formatter_type} formatter not found!')

class MyFormatter(TableFormatter):
    def headings(self,headers): 
        pass
    def row(self,rowdata): 
        pass

def q_a():
    import stock, reader, tableformat
    print("hello")
    portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock)
    tableformat.print_table(portfolio, ['name','shares','price'], MyFormatter())

class NewFormatter(TableFormatter):
    def headers(self, headings):
        pass
    def row(self, rowdata):
        pass

def q_b():
    f = NewFormatter()

if __name__ == "__main__":
    q_b()