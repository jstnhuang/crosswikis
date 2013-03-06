"""Hadoop mapper that removes all entries in Crosswikis whose entities end with
_(disambiguation). This does not truly remove all disambiguation pages, but this
is probably the best we can do without going to the Wikipedia API.
"""
import sys

ENTITY_COL = 2

def main():
  """Assumes the line is tab-separated, with columns: anchor, cprob, entity,
  info, count."""
  for line in sys.stdin:
    columns = line.split('\t')
    entity = columns[ENTITY_COL]
    if not entity.endswith('_(disambiguation)'):
      print line,

if __name__ == '__main__':
  main()
