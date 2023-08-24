import stock

def print_table(values, types):
    print(" ".join("%10s" %type for type in types))
    print(" ".join("_"*10 for type in types))
    for value in values:
        result = ""
        for type in types:
            result += "%10s" %getattr(value, type) + " "
        print(result)

if __name__ == "__main__":
    portfolio = stock.read_portfolio('Data/portfolio.csv')
    print_table(portfolio, ['name','shares','price'])