import json
import urllib2
import time
import sys
#file_writer = open('articles.csv','w')
articles = []
filename = "articles_"+sys.argv[1]+".json"
for i in range(101):
	data = urllib2.urlopen('http://api.nytimes.com/svc/search/v2/articlesearch.json?q='+sys.argv[1]+'&page='+str(i)+'&f1=(_id,web_url,snippet,newsdesk,source,headline,keywords,word_count,pub_date)&api-key=28d7855953adb8b53f90091bec95f073:2:71568054')

	news_json = json.load(data)
	for doc in news_json["response"]["docs"]:
		articles.append({'web_url':doc['web_url'],'id':doc["_id"], 'snippet':doc["snippet"], 'lead_paragraph':doc["lead_paragraph"],'abstract':doc["abstract"], 'keywords':doc["keywords"], 'section':doc["section_name"]})
	#print news_json["response"]["docs"][2]["snippet"]

	#for doc in news_json["response"]["docs"]:
		#print doc["_id"]
		#print doc["snippet"]
		#print doc["lead_paragraph"]
		#print doc["abstract"]
		#print doc["keywords"]
		#print doc["section_name"]


	time.sleep(0.5)
#json_data = json.dumps(articles)	
print len(articles)
news = {"articles": articles}
json.dump(news, open(filename, 'wb'))

