import sys

def getCount(info):
  infoParts = info.split(' ')
  labels = ['W:', 'Wx:', 'w:', 'w:']
  count = 0
  for part in infoParts:
    if part.startswith('W:'):
      counts = part[2:]
      numerator = int(counts.split('/')[0])
      count += numerator
    elif part.startswith('Wx:'):
      counts = part[3:]
      numerator = int(counts.split('/')[0])
      count += numerator
    elif part.startswith('w:'):
      counts = part[2:]
      numerator = int(counts.split('/')[0])
      count += numerator
    elif part.startswith('w\':'):
      counts = part[3:]
      numerator = int(counts.split('/')[0])
      count += numerator
    else:
      continue
  return count

def main():
  for line in sys.stdin:
    lineParts = line.split('\t')
    cprob = lineParts[1]
    if cprob == '0.0':
      continue
    info = lineParts[3].strip()
    count = getCount(info)
    print '\t'.join([
      lineParts[0],
      lineParts[1],
      lineParts[2],
      info,
      str(count).strip()
    ])

if __name__ == '__main__':
  main()
