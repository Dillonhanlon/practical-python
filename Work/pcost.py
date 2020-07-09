# pcost.py
#
# Exercise 1.27


#f = open('Data/portfolio.csv','rt')
def portfolio_cost(filename):
    f = open(filename,'rt')
    tot_cost = 0
    headers = next(f)
    for line in f:
        row = line.split(',')
        shares = int(row[1])
        share_price = float(row[2])
        tot_cost += share_price * shares
    return tot_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total Cost:', cost)