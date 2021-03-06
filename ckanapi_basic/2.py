#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint

siteurl="http://ckan1.nchc.org.tw:5000/"
apiuri=siteurl+"api/action/package_create"

# Put the details of the dataset we're going to create into a dict.
dataset_dict = {
    'name': 'my_dataset_name5',
    'notes': 'A long description of my dataset',
    'owner_org':'std'
}

# Use the json module to dump the dictionary to a string for posting.
data_string = urllib.quote(json.dumps(dataset_dict))

# We'll use the package_create function to create a new dataset.
request = urllib2.Request(apiuri)

# Creating a dataset requires an authorization header.
# Replace *** with your API key, from your user account on the CKAN site
# that you're creating the dataset on.
request.add_header('Authorization', 'a6d44b37-7407-4ad1-b457-aa4b6c611d29')

# Make the HTTP request.
response = urllib2.urlopen(request, data_string)
assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
assert response_dict['success'] is True

# package_create returns the created package as its result.
created_package = response_dict['result']
pprint.pprint(created_package)

