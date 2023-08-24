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
    # if not isinstance(formatter, TableFormatter):
    #     raise TypeError('Expected a TableFormatter')

    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

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

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

def create_formatter(name, column_formats=None, upper_headers=False):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()


if __name__ == "__main__":
    from tableformat import create_formatter
    import stock, reader
    formatter = create_formatter('csv', column_formats=['"%s"','%d','%0.2f'])
    portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock)
    print_table(portfolio, ['name','shares','price'], formatter)