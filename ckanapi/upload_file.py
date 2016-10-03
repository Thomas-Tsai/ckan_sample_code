import sys
from ckanapi import RemoteCKAN
url="http://127.0.0.1"
ckan_key=""
ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

mysite = RemoteCKAN(url, apikey=ckan_key, user_agent=ua)
mysite.action.resource_create(
    package_id='my-dataset-0',
    url='filecsv',
    name='filecsv',
    upload=open("./file.csv", 'rb'))
