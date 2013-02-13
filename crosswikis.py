import sqlite3
import unicodedata

CROSSWIKIS_DB_PATH = '../../data/crosswikis/crosswikis.db'

def query(queryString, args):
  """Executes the given query and yields the results.

  Args:
    queryString: The SQLite query string.
    args: A tuple with all the args to pass to the query string.

  Yields: The rows returned from the query.
  """
  connection = sqlite3.connect(CROSSWIKIS_DB_PATH)
  cursor = connection.cursor()
  for row in cursor.execute(queryString, args):
    yield row
  connection.commit()
  connection.close()

def getLnrm(arg):
  """Normalizes the given arg by stripping it of diacritics, lowercasing, and
  removing all non-alphanumeric characters.
  """
  arg = ''.join([
    c for c in unicodedata.normalize('NFD', arg)
    if unicodedata.category(c) != 'Mn'
  ])
  arg = arg.lower()
  arg = ''.join([
    c for c in arg
    if c in set('abcdefghijklmnopqrstuvwxyz0123456789')
  ])
  return arg

def getEntityDistribution(string, minCprob=None, minCount=None, limit=None):
  """Gets the distribution of entities linked to the synonym in Crosswikis.

  Queries the Crosswikis data for the string we're interested in, and gets a
  list of entities associated with it and their counts.

  Args:
    string: The string to search for.
    table: The table to look for the string in.

  Returns: A list of (entity, cprob, num, denom) tuples, sorted in descending
    order of conditional probability.
  """
  queryParts = [
    'SELECT entity, cprob, info, count',
    'FROM crosswikis',
    'WHERE anchor=?'
  ]
  lnrm = getLnrm(string)
  args = [lnrm]

  if minCprob != None:
    queryParts.append('AND cprob >= ?')
    args.append(minCprob)
  if minCount != None:
    queryParts.append('AND count >= ?')
    args.append(minCount)

  queryParts.append('ORDER BY cprob desc')

  if limit != None:
    queryParts.append('LIMIT ?')
    args.append(limit)

  queryString = ' '.join(queryParts)
  return [row for row in query(queryString, tuple(args))]
