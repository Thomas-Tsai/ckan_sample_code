import json
import requests

url='http://data.gov.tw/api/v1/rest/dataset/A41000000G-000001'
r=requests.get(url)
x=json.loads(r.text)
rs = x['result']
for k,v in rs.items():
    if k == "distribution":
	for desc in v:
	    for dk,dv in desc.items():
		print "%30s : %s" % (dk, dv)
    elif k == "keyword":
	for keyword in v:
	    print "%30s : %s" % ("keyword", keyword)
    else:
	print "%30s : %s" % (k, v)

