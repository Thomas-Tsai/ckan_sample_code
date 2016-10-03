from ckanapi import RemoteCKAN, NotAuthorized
url="http://127.0.0.1"
ckan_key=""
ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

demo = RemoteCKAN(url, apikey=ckan_key, user_agent=ua)
try:
    pkg = demo.action.package_create(name='my-dataset-0', title='going to work', owner_org='org01')
except NotAuthorized:
    print 'denied'
