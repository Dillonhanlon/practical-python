# pcost.py
#
# Exercise 1.27
tot_cost = 0

f = open('Data/portfolio.csv','rt')
headers = next(f)
for line in f:
    row = line.split(',')
    shares = int(row[1])
    share_price = float(row[2])
    tot_cost += share_price * shares
print(f'Total Cost = {tot_cost:0.2f}')