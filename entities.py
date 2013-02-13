# File for dealing with Wikipedia/Freebase entities.

import json
import urllib.parse
import urllib.request

WIKI_API_ENDPOINT = 'http://en.wikipedia.org/w/api.php'

def queryWikipedia(data):
  """Get a JSON object from the Wikipedia API for the given API query.
  
  Args:
    data: A dictionary of query args for the Wikipedia API. Be sure to include
      'action': 'query', 'titles': {Some title}, etc.
  """
  data['format'] = 'json'
  encodedData = bytes(urllib.parse.urlencode(data), 'utf-8')
  request = urllib.request.Request(WIKI_API_ENDPOINT, encodedData)
  response = urllib.request.urlopen(request)
  jsonStr = ''.join([bytes.decode(line) for line in response])
  jsonObj = json.loads(jsonStr)
  return jsonObj

def isDisambiguation(jsonObj):
  """Gets whether or not the page from the given response is a disambiguation
  page or not.
  """
  # There should only be one page ID.
  for pageId in jsonObj['query']['pages']:
    page = jsonObj['query']['pages'][pageId]
    categories = page['categories'] if 'categories' in page else []
    for category in categories:
      if category['title'] == 'Category:All disambiguation pages':
        return True
    return False

def normalizeTitle(jsonObj):
  """Gets the normalized title from the given Wikipedia API response.
  """
  if 'normalized' in jsonObj['query']:
    return jsonObj['query']['normalized'][0]['to']
  else:
    # There should only be one page ID.
    for pageId in jsonObj['query']['pages']:
      return jsonObj['query']['pages'][pageId]['title']
