#!/usr/bin/env python

import rethinkdb as r
from optparse import OptionParser
import sys
import os
import urllib, json
import pprint

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

print options
print args

# url = "http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false"
# url = "https://api.github.com/orgs/materials-commons/repos"
# gets last of 29 pages of issues in any state
url = "https://api.github.com/repos/materials-commons/materialscommons.org/issues?state=all&page=29"
response = urllib.urlopen(url)
body = response.read()
pp = pprint.PrettyPrinter(indent=4)
data = json.loads(body)
#pp.pprint(data)

for element in data:
    print element['number'],element['id'],element['created_at'],element['closed_at']
