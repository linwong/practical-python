# fileparse.py
#
# Exercise 3.3
import csv
import gzip

def parse_csv(items,
              select=[],
              types=[],
              has_headers=True,
              delimiter=',',
              silence_errors=False):
  '''
  Parse a csv file into a list of records
  '''
  # Sanity check
  if select and has_headers == False:
    raise RuntimeError("select argument requires headers")

  rows = csv.reader(items, delimiter=delimiter)
  records = []
  if has_headers:
    # Read the header
    headers = next(rows)

    # If select list is passed, we only get those headers
    if select:
      indices = [ headers.index(col) for col in select ]
      headers = select
    else:
      indices = []

    for i,row in enumerate(rows):
      if not row: # skip empty rows
        continue

      if indices:
        row = [ row[i] for i in indices ]

      if types:
        try:
          row = [ func(val) for func, val in zip(types, row) ]
        except ValueError as e:
          if not silence_errors:
            print(f"Row {i+1}: Couldn't convert {row}")
            print(f"Row {i+1}: Reason {e}")

      record = dict(zip(headers, row))
      records.append(record)
  else: # no headers
    for row in rows:
      row = [ func(val) for func, val in zip(types, row) ]
      try:
        records.append((row[0], row[1]))
      except IndexError:
        pass

  return records
