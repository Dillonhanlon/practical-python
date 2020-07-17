# pcost.py
#Exercise 3.18
import csv
from report import read_portfolio
def portfolio_cost(filename):
    
    portfolio = read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]}' 'portfoliofile')
    print('Total cost:', portfolio_cost(args[1]))
    
if __name__ == '__main__':
    import sys
    main(sys.argv)