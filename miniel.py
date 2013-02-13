"""An "entity linker" that just does a Crosswikis lookup. The main function
compares different pruning/selection policies for getting candidate entities.
"""
import crosswikis
import entities as ents
import sys

jsonCache = {}

def getTopEntities(entities, minCprob=0.15, minCount=200, limit=3):
  """Gets the top n entities with the highest probabilities.

  Args:
    entities: A list of candidate entities.
    minCprob: The minimum probability. A value of None is the same as the
      minimum being 0.
    minCount: The minimum count.
    limit: The maximum number of entities to return. A value of None means there
      is no limit.
  """
  if minCprob == None:
    minCprob = 0
  if minCount == None:
    minCount = 0

  # First pass over the data, remove disambiguation pages and group entities by
  # normalized title.
  entityCounts = {}
  denom = 0
  for entity in entities:
    title, cprob, info, count = entity

    jsonObj = None
    if title in jsonCache:
      jsonObj = jsonCache[title]
    else:
      queryData = {'action': 'query', 'titles': title, 'prop': 'categories'}
      jsonObj = ents.queryWikipedia(queryData)
      jsonCache[title] = jsonObj

    # Remove disambiguation pages.
    isDisambiguation = ents.isDisambiguation(jsonObj)
    if isDisambiguation:
      continue

    # Group results by normalized title.
    normalizedTitle = ents.normalizeTitle(jsonObj)
    if normalizedTitle in entityCounts:
      entityCounts[normalizedTitle] += count
    else:
      entityCounts[normalizedTitle] = count
    denom += count

  # Second pass: recompute probabilities and filter.
  topEntities = []
  for title in entityCounts:
    count = entityCounts[title]
    prob = count / denom
    if prob >= minCprob and count >= minCount:
      topEntities.append((title, prob))
  topEntities = sorted(topEntities, key=lambda e: e[1], reverse=True)

  if limit != None:
    topEntities = topEntities[:limit]

  return topEntities

def getArg(query, removeThe=True):
  """Gets the arg from the given sample query. Assumes that there's only one
  arg. Removes leading "the" from the arg.
  """
  arg1, rel, arg2 = query
  if arg1 == '*':
    if removeThe == True and arg2.lower().startswith('the '):
      return arg2[4:]
    else:
      return arg2
  else:
    if removeThe == True and arg1.lower().startswith('the '):
      return arg1[4:]
    else:
      return arg1

def getSampleQuery(line):
  """Returns the arg1, rel, and arg2 for each sample query in the sample query
  file.
  """
  line = line.strip()[1:-1]
  lineParts = line.split(',')
  lineParts = [part.strip() for part in lineParts]
  arg1, rel, arg2 = lineParts[0], lineParts[1], lineParts[2]
  return arg1, rel, arg2

def comparePolicies(query):
  results = {}
  print('Working on {}'.format(query))
  arg = getArg(query)
  entities = crosswikis.getEntityDistribution(arg)
  entities = entities[:10]
  topEntities1 = getTopEntities(entities, minCprob=0, limit=3)
  topEntities2 = getTopEntities(entities, minCprob=0.2, limit=None)
  topEntities3 = getTopEntities(entities, minCprob=0.15, limit=5)
  results = (topEntities1, topEntities2, topEntities3)
  return results

def prettyPrintResults(query, results, outputFile):
  maxLen = max([len(result) for result in results])
  queryString = '({})'.format(', '.join(query))
  print(
    '\t'.join([queryString, 'Top 3', 'All >= 0.2', 'Top 5 >= 0.15']),
    file=outputFile
  )
  for i in range(maxLen):
    columns = ['']
    columns.extend([
      str(result[i]) if i < len(result) else ''
      for result in results
    ])
    print('\t'.join(columns), file=outputFile)
  print(file=outputFile)

def main():
  sampleFilePath = sys.argv[1]
  policyOutPath = sys.argv[2]
  sampleFile = open(sampleFilePath)
  outputFile = open(policyOutPath, 'w')
  for line in sampleFile:
    query = getSampleQuery(line)
    results = comparePolicies(query)
    prettyPrintResults(query, results, outputFile)

if __name__ == '__main__':
  main()
