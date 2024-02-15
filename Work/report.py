#!/usr/bin/env python
# report.py
#
# Exercise 2.4
import sys
import csv
import stock
import tableformat
from fileparse import parse_csv

def read_portfolio(filename):
  types = [str, int, float] # portfolio.csv
  with open(filename) as lines:
    return [ stock.Stock(d['name'], d['shares'], d['price']) for d in parse_csv(lines, types=types) ]

def read_prices(filename):
  with open(filename) as lines:
    prices_array = parse_csv(lines, types=[str,float], has_headers=False)
    prices = {}
    for p in prices_array:
      prices[p[0]] = p[1]
    return prices

def make_report(portfolio, prices):
  report = []
  for p in portfolio:
    report.append((p.name,
                   p.shares,
                   prices[p.name],
                   prices[p.name] - p.price
                   ))
  return report

def print_report(report, formatter):
  '''
  Print nicely report
  '''
  formatter.headings(['Name', 'Shares', 'Price', 'Change'])
  for name, shares, price, change in report:
    rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
    formatter.row(rowdata)
  
def portfolio_report(portfolio_filename, prices):
  portfolio = read_portfolio(portfolio_filename)
  prices    = read_prices(prices)
  report    = make_report(portfolio, prices)
  formatter = tableformat.HTMLTableFormatter()
  print_report(report, formatter)


def main(argv):
  if len(argv) != 3:
    raise RuntimeError("Not enough agruments")
  portfolio_report(argv[1], argv[2])
  
if __name__ == '__main__':
  main(sys.argv)
