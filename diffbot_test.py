import json

import requests
from pprint import pprint

import sqlite3

##INIT

DIFFBOT_API_KEY = "339693268e6182d0244242f5e8c44f0f"
BASE_URL = "http://api.diffbot.com/v3/crawl"

ARTICLE_URL = "http://api.diffbot.com/v3/article"
ANALYZE_URL = "http://api.diffbot.com/v3/analyze?mode=auto"

db = sqlite3.connect('diffbot.db')

##API ACCESS

class Crawl(object):
	def __init__(self, name, url):
		Crawl.name = name
		Crawl.url = url


	def query(self):
		params = {"apiUrl":ANALYZE_URL,
				  "name":self.name,
				  "token":DIFFBOT_API_KEY,
				  "seeds":self.url,
				  "maxToCrawl":100,
				  "maxToSpider":100}
		r = requests.get(BASE_URL,params=params)
		print r.text
		return

	def retrieve(self):
		diffbot_url = BASE_URL + "/data"
		r = requests.get(diffbot_url,params={"token":DIFFBOT_API_KEY,"name":self.name})
		return r.json()

##WIP##
	def save(self):
		cursor = db.cursor()
		for page in self.retrieve():
			columns = set(page.keys())
			values = (page[key] for key in columns)
	 		query = """INSERT INTO pages ? VALUES ?"""

	 		columns_values = (columns, values)
	 		cursor.execute(query, columns_values)
	 	return

##PRINT TO TERMINAL##
	def check(self):
		data = self.retrieve()
		print "Articles from %s at url %s" % (self.name, self.url)
		print len(data), "items retrieved"
		for page in data:
			if page.get('type') == 'article':
				print page.get('type'),' | ',page.get('title'),' | ',page.get('timestamp'), " | ",page.get('pageUrl')
		return
##TESTING##

test_names_urls = [('nc_test','')
			 	  ,('analyze_test','http://insights.newscred.com')
			 	  ,('analyze_test2','https://insights.newscred.com')
			 	  ,('contently','https://contently.com/strategist/')
				  ]

crawl = Crawl(test_names_urls[3][0],test_names_urls[3][1])
#crawl.query()
crawl.check()
#crawl.save()
