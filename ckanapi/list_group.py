from ckanapi import RemoteCKAN
url="http://127.0.0.1"
ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

demo = RemoteCKAN(url, user_agent=ua)
groups = demo.action.group_list()
print groups
