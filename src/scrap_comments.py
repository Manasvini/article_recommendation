import json
import urllib2
import time
import sys
from pprint import pprint
#file_writer = open('articles.csv','w')
file_reader = open('article_urls.txt', 'r')
urls = file_reader.readlines()
comments = []

for u in urls[6290:]:
	try:
		url = u.split()[1]
		data = urllib2.urlopen('http://api.nytimes.com/svc/community/v3/user-content/url.json?api-key=38984593db47abb6f1f297648c03d0b7:0:71568054&url='+url)

		news_json = json.load(data)
		#pprint(news_json)
		#print dir(news_json)
		if "comments" in news_json["results"]:
			for doc in news_json["results"]["comments"]:
				#pprint(doc)
				print doc['userID']
				print doc['commentBody']
				comments.append({'user_id':doc['userID'],'comment':doc["commentBody"], 'article_id':u.split()[0]})
				#print news_json["response"]["docs"][2]["snippet"]

			#for doc in news_json["response"]["docs"]:
				#print doc["_id"]
				#print doc["snippet"]
				#print doc["lead_paragraph"]
				#print doc["abstract"]
				#print doc["keywords"]
				#print doc["section_name"]
				#break
	except Exception, e:
		print "blah"
	time.sleep(0.5)

#json_data = json.dumps(articles)	
#print len(comments)
reviews = {"comments": comments}
json.dump(reviews, open('comments.json', 'wb'))

