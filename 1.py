#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint

siteurl="http://ckan1.nchc.org.tw:5000/"
apiuri=siteurl+"api/3/action/group_list"

# Use the json module to dump a dictionary to a string for posting.
data_string = urllib.quote(json.dumps({'id': 'data-explorer'}))

# Make the HTTP request.
response = urllib2.urlopen(apiuri, data_string)
assert response.code == 200
# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())

# Check the contents of the response.
assert response_dict['success'] is True
result = response_dict['result']
pprint.pprint(result)
