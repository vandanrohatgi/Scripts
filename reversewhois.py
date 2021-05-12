#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import sys

if len(sys.argv) != 2:
	print("Usage: python3 reversewhois.py <target>")
	exit()

target=sys.argv[1]
print("Reverse Whois Lookup for {}".format(target))

res=requests.get("https://www.reversewhois.io/?searchterm={}".format(target))

soup=BeautifulSoup(res.text,'lxml')

if soup.find_all('table') !=[]:
	table=soup.find_all('table')[0]
	for row in table.find_all('tr'):
	columns=row.find_all('td')
	content=str(columns[1])
	print(content[4:-5])
else:
	print("Data not found for the domain")



