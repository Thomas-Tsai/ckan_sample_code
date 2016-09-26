from ckanapi import RemoteCKAN
ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

demo = RemoteCKAN('http://ckan1.nchc.org.tw:5000', user_agent=ua)
groups = demo.action.group_list(id='data-explorer')
print groups
