# pcost.py
#
# Exercise 1.27
import sys
import csv
import stock
from fileparse import parse_csv

def portfolio_cost(filename):
  with open(filename) as f:
    rows = parse_csv(f, select=['shares', 'price'], types=[int, float])
  records = [ stock.Stock('', d['shares'], d['price']) for d in rows ]
  total_cost = 0
  for r in records:
    total_cost += r.shares * r.price
  return total_cost

def main(argv):
  if len(sys.argv) == 2:
    filename = sys.argv[1]
  else:
    filename = 'Data/portfolio.csv'

  cost = portfolio_cost(filename)
  print('Total cost:', cost)
  
if __name__ == '__main__':
  main(sys.argv)

