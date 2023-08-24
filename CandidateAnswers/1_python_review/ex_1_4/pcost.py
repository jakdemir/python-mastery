#pcost.py

def portfolio_cost(filename):
    with open(filename, 'r') as f:
        cost = 0
        for line in f.readlines():
            try:
                portfolio_dict = line.split()
                print(portfolio_dict)
                cost += float(portfolio_dict[1]) * float(portfolio_dict[2])
            except ValueError as v:
                print('Skipping ValueError', v)
    return cost    
    

if __name__ == '__main__':
    print(portfolio_cost('Data/portfolio3.dat'))
