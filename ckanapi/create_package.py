from ckanapi import RemoteCKAN, NotAuthorized
ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

demo = RemoteCKAN('http://ckan1.nchc.org.tw:5000', apikey='a6d44b37-7407-4ad1-b457-aa4b6c611d29', user_agent=ua)
try:
    pkg = demo.action.package_create(name='my-dataset', title='not going to work', owner_org='std')
except NotAuthorized:
    print 'denied'
