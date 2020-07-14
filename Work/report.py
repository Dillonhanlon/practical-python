# report.py
import csv

def read_portfolio(filename):
    
    portfolio = []

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            stock = {
                 'name'   : row[0],
                 'shares' : int(row[1]),
                 'price'   : float(row[2])
            }
            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename,'rt') as f:
        rows = csv.reader(f) 
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')

total_cost = 0.0
total_value = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']
    total_value += s['shares']*prices[s['name']]

print('Total cost', total_cost)
print('Current value', total_value)
print('Gain', total_value - total_cost)

def make_report(portfolio,prices):
    rows = []
    for r in portfolio:
        price = prices[r['name']]
        change = price - r['price']
        Final = (r['name'], r['shares'], price, change)
        rows.append(Final)
    return rows

report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%8s %8s %8s %8s' % headers)
print(('-' * 8 + ' ') * len(headers))
for row in report:
    print('%8s %8d $%8.2f %8.2f' % row)
