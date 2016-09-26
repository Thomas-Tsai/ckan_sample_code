import sys
from ckanapi import RemoteCKAN
ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

mysite = RemoteCKAN('http://ckan1.nchc.org.tw:5000', apikey='a6d44b37-7407-4ad1-b457-aa4b6c611d29', user_agent=ua)
mysite.action.resource_create(
    package_id='my-dataset',
    url='filecsv',
    name='filecsv',
    upload=open("./file.csv", 'rb'))
