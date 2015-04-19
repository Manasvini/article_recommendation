# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from bs4 import BeautifulSoup
import json
import requests

# <codecell>

file_reader = open('article_urls.txt','r')
urls = file_reader.readlines()
articles = []

for u in urls:
#link = "http://www.somesite.com/details.pl?urn=2344"
    try:
        article_id, link = u.split(',')
        f = requests.get(link.strip())
        soup = BeautifulSoup(f.text)
        paras = soup.find_all('p')
    #print paras
        text = ''
        for p in paras:
            if str(p).find('story-body-text story-content') != -1:
                s = BeautifulSoup(str(p))
                text += s.get_text()
        articles.append({'id':article_id, 'text': text})
    except Exception, e:
        print e.message
    
file_reader.close()

# <codecell>

articles_json  = {"articles": articles}
json.dump(articles_json, open('articles.json', 'wb'))

# <codecell>


