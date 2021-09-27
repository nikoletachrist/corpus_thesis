import io
import os
import re
import requests
from nltk.tokenize import word_tokenize
import json
from bs4 import BeautifulSoup

def tags2(root,tag_catalogue):
	os.chdir(root)
	for fileid in os.listdir(root):
		itstxt=re.match(r'((.*\.(txt|csv)|fixes.json))',fileid)
		if itstxt:
			continue
		fo=io.open(fileid,'r',encoding='utf8')
		identity=json.load(fo)
		fo.close()
		textid=re.sub('json','txt',fileid)
		tag_catalogue.append({'name':textid,'title':identity['title'],'url':identity['site'],'category':identity['category'],'label':identity['label'],'Wiki_categ':'0','greekWords':identity['words'],'words':'0'} )
	print(tag_catalogue)
	return tag_catalogue

root='/Users/nic/Desktop/PythonProject/CORPUS'
os.chdir(root)
catalogue=[]
tag_cat=tags2(root,catalogue)
fo=io.open('map.json','w',encoding='utf8')
json.dump(catalogue,fo,ensure_ascii=False,indent=4)
fo.close()
fo=io.open('map.json','r',encoding='utf8')
catalogue=json.load(fo)
fo.close()
for text in catalogue:
	fo=io.open(text['name'],'r',encoding='utf8')
	raw=fo.read()
	fo.close()
	words=word_tokenize(raw)
	count=0
	for w in words:
		if w.isalpha():
			count=count+1
	print(count)
	text['words']=count
for item in catalogue:
	categ=[]
	html = requests.get(item['url'])
	start = html.text.find("id=\"mw-normal-catlinks\"")
	end = html.text.find("id=\"mw-hidden-catlinks\"")
	if start==-1:
		break
	if end==-1:
		end = html.text.find("id=\"	mw-data-after-content\"")
	usefullText = html.text[start:end]
	soup = BeautifulSoup(usefullText, 'html.parser')
	for link in soup.find_all('a'):
		name = link.get('title')
		if name==None:
			continue
		if name=="Ειδικό:Κατηγορίες":
			continue
		matchobj=re.match(r'Κατηγορία:',name)
		if not matchobj:
			continue
		name=re.sub('Κατηγορία:','',name)
		print(name)
		categ.append(name)
	item['Wiki_categ']=categ
fo=io.open('map.json','w',encoding='utf8')
json.dump(catalogue,fo,ensure_ascii=False,indent=4)
fo.close()
