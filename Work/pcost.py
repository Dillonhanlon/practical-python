# pcost.py

import csv
def portfolio_cost(filename):
    
    tot_cost = 0.0

    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:

        shares = int(row[1])
        share_price = float(row[2])
        tot_cost += shares * share_price
    return tot_cost

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)