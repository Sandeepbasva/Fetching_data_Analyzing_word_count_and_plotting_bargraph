# URL
# https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=swecha

import urllib2
import json

# Fetching data from URL
URL = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=swecha"
response = urllib2.urlopen(URL)
html = response.read()

# print html

# Converting string to JSON Object
jObject = json.loads(html)

subQuery = jObject['query']['pages']



