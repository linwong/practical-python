# tableformat.py

class TableFormatter:
  def create_formatter(self, fmt):
    pass
  
  def headings(self, headers):
    '''
    Emit the table headings.
    '''
    raise NotImplementedError()

  def row(self, rowdata):
    '''
    Emit a single row of table data.
    '''
    raise NotImplementedError()


class TextTableFormatter(TableFormatter):
  def headings(self, headers):
    for h in headers:
      print(f'{h:>10s}', end=' ')
    print()
    print(('-' * 10 + ' ') * len(headers))

  def row(self, rowdata):
    for r in rowdata:
      print(f'{r:>10s}', end=' ')
    print()



class CSVTableFormatter(TableFormatter):
  def headings(self, headers):
    print(','.join(headers))

  def row(self, rowdata):
    print(','.join(rowdata))



class HTMLTableFormatter(TableFormatter):
  def headings(self, headers):
    for h in headers:
      print('<th>' + h + '</th>', end='')
    print()

  def row(self, rowdata):
    for row in rowdata:
      print('<td>'+row+'</td>', end='')
    print()
