"""Hadoop reducer for removing disambiguation pages. The mapper removes the
disambiguation pages, so the reducer recomputes the conditional probabilities.
"""
import itertools
import sys

ANCHOR_COL = 0
CPROB_COL = 1
COUNT_COL = 4

def main():
  getAnchor = lambda line: line.split('\t')[ANCHOR_COL]
  for anchor, group in itertools.groupby(sys.stdin, getAnchor):
    totalCount = 0.0
    lines = list(group)
    for line in lines:
      count = int(line.split('\t')[COUNT_COL])
      totalCount += count
    for line in lines:
      columns = line.split('\t')
      columns[CPROB_COL] = str(int(columns[COUNT_COL]) / totalCount)
      print '\t'.join(columns),

if __name__ == '__main__':
  main()
