#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint

siteurl="http://ckan1.nchc.org.tw:5000/"
apiuri=siteurl+"api/action/resource_create"

# upload file
import requests
requests.post(apiuri,
	data={"package_id":"my_dataset_name5", "url":"file5", "name":"file5"},
	headers={"Authorization": "a6d44b37-7407-4ad1-b457-aa4b6c611d29"},
	files=[('upload', file('./file.csv'))])


