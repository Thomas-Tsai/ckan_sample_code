#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint

# upload file
import requests
requests.post('http://ckan1.nchc.org.tw:5000/api/action/resource_create', 
	data={"package_id":"my_dataset_name3", "url":"file2", "name":"file"},
	headers={"Authorization": "a6d44b37-7407-4ad1-b457-aa4b6c611d29"},
	files=[('upload', file('./file.csv'))])


