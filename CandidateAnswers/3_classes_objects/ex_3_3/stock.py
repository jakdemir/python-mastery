#stock.py
import csv 

class Stock:
    __slots__ = ['name', 'shares', 'price']
    __types__ = [str, int, float]

    @classmethod
    def from_row(cls, row):
        values = [type(value) for type, value in zip(cls.__types__, row)]
        return cls(*values)

    def __init__(self, name, shares, price) -> None:
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)

    def sell(self, shares):
        if self.shares >= shares:
            self.shares -=  shares
        else:
            print(f'Not enough shares porfolio: {self.shares}, sell req: {shares}')

    def __repr__(self) -> str:
        return f"NAME: {self.name}, SHARES: {self.shares}, PRICE: {self.price}"

    def __str__(self) -> str:
        return f"NAME: {self.name}, SHARES: {self.shares}, PRICE: {self.price}"
    
def read_portfolio(filename, classname):
    stock_list = list()
    with open(filename) as file:
        rows = csv.reader(file)
        header = next(rows)
        for row in rows:
            stock_list.append(classname.from_row(row))
    return stock_list

def read_all():
    porfolio = read_portfolio('Data/portfolio.csv')
    for stock in porfolio:
        print(stock)

def printer():
    portfolio = read_portfolio('Data/portfolio.csv', Stock)
    for stock in portfolio:
        print("%10s %10d %10.2f" % (stock.name, stock.shares, stock.price))

def sell_test():
    s = Stock('GOOG', 100, 490.10)
    print(f"BEFORE SELL : {s}")
    s.sell(50)
    print(f"AFTER SELL : {s}")

if __name__ == '__main__':
    #A
    # sell_test()
    #B
    # read_all()
    printer()