# pcost.py

import csv
def portfolio_cost(filename):
    
    tot_cost = 0.0

    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    for rowno, row in enumerate(rows,start = 1):
        record = dict(zip(headers, row))
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            tot_cost += nshares * price

        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
    return tot_cost

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)