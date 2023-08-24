#pcost.py

def calculate_portfolio(filename):
    with open(filename, 'r') as f:
        cost = 0
        for line in f.readlines():
            portfolio_dict = line.split()
            print(portfolio_dict)
            cost += float(portfolio_dict[1]) * float(portfolio_dict[2])
    print('cost: ', cost, end="\n")
    
    

if __name__ == '__main__':
    calculate_portfolio('Data/portfolio.dat')