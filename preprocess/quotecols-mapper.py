"""Double-quotes quotes in Crosswikis data, and puts quotes around text fields.
This format is necessary to import the data into Apache Derby.
"""
import sys

def main():
  for line in sys.stdin:
    line = line.replace('"', '""')
    lineParts = line.split('\t')
    print '\t'.join([
      '"{0}"'.format(lineParts[0]),
      lineParts[1],
      '"{0}"'.format(lineParts[2]),
      '"{0}"'.format(lineParts[3]),
      lineParts[4].strip()
    ])

if __name__ == '__main__':
  main()
