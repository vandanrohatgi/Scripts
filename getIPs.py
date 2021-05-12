import requests
import json
import time

api=''
secret=''
url='https://censys.io/api/v1/search/ipv4'
target=input("enter url: ")
query={"query":target,'fields':["ip"],}
final=[]

res=requests.post(url=url+"/search/ipv4",auth=(api,secret),data=json.dumps(query))

pages=res.json()['metadata']['pages']
time.sleep(1)

try:
	for y in range(1,pages+1):
		print("requesting page no. {}".format(y))
		query={'query':target,'fields':["ip"],'page':y,}
		res=requests.post(url=url,auth=(api,secret),data=json.dumps(query))
		print(res.json())
		result=res.json()['results']
		filtered=[x.get('ip') for x in result]
		final+=filtered
		time.sleep(1)
except:
	print(final)
	data='\n'.join(final)
	f=open("IPs.txt",'w')
	f.write(data)
	f.close()
