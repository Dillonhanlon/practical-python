# report.py
import csv
from fileparse import parse_csv

def read_portfolio(filename):
    return parse_csv(filename, select=['name','shares','price'], types=[str,int,float])


def read_prices(filename):
    return dict(parse_csv(filename,types=[str,float], has_headers=False))


def make_report(portfolio,prices):
    rows = []
    for r in portfolio:
        price = prices[r['name']]
        change = price - r['price']
        Final = (r['name'], r['shares'], price, change)
        rows.append(Final)
    return rows

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%8s %8s %8s %8s' % headers)
    print(('-' * 8 + ' ') * len(headers))
    for row in report:
        print('%8s %8d $%8.2f %8.2f' % row)


def portfolio_report(portfolio_filename,prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create the report data
    report = make_report(portfolio,prices)

    # Print it out
    print_report(report)


def main(args):
    if len(args) !=3:
        raise SystemExit(f'Usage: {sys.argv[0]}' 'portfile pricefile')
    portfolio_report(args[1],args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)