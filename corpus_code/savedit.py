import io
import os
import re
import requests
from nltk.tokenize import word_tokenize
from myfunc import inspection, final_cut,greek_word, text_sorting,the_catalogue,full_text_list,count_results,sum_texts,compare_entries
import shutil
import random
import json
from bs4 import BeautifulSoup,SoupStrainer
def tags(root,tag_catalogue):
	os.chdir(root)
	#  tag_catalogue=[]
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

def sort_catalogue(catalogue):
	dest='C:/Users/nic/Desktop/PythonProject/categ_analysis'
	categories=[]
	labels=[]
	texts=[]
	graphs=[]
	labelspercategory=[]
	for dictionary in catalogue:
		oldc=inspection(dictionary["category"],categories)
		if oldc:
			continue
		categories.append(dictionary["category"])
	for category in categories:
		for dictionary in catalogue:
			if dictionary['category']==category:
				oldl=inspection(dictionary["label"],labels)
				if oldl:
					continue
				labels.append(dictionary["label"])
		for label in labels:
			for dictionary in catalogue:
				if dictionary['category']==category:
					if dictionary['label']==label:
						texts.append(dictionary['text'])
			textsperlabel={'label':label,'texts':texts}
			labelspercategory.append(textsperlabel)
			texts=[]	
		graph={'category':category,'labels':labelspercategory}
		graphs.append(graph)
		print(graph)
		labelspercategory=[]
		labels=[]
	os.chdir(dest)
	fo=io.open('fullinfo2.json','w',encoding='utf8')
	json.dump(graphs,fo,ensure_ascii=False,indent=4)
	fo.close()
	print(graphs)

# catalogues="C:/Users/nic/Desktop/PythonProject/categ_analysis"
root='/Users/nic/Desktop/PythonProject/CORPUS'
os.chdir(root)
# catalogue=[]
# tag_cat=tags(root,catalogue)
# sort_catalogue(tag_cat)
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
fo=io.open('map.json','w',encoding='utf8')
json.dump(catalogue,fo,ensure_ascii=False,indent=4)
fo.close()

#GET WIKI CATEG
# only_a=SoupStrainer("a")
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


# print(tag_cat)
# print(len(tag_cat))


# os.chdir(show)
# contents= os.listdir(show)
# for text in contents:
# 	itsjson = re.match(r'.*\.json', text)
# 	if itsjson:
# 		continue
# 	print(text)
# 	fo = io.open(text, 'r', encoding='utf8')
# 	raw = fo.read()
# 	fo.close()
# 	sample = final_cut(raw)
# 	word=[w for w in sample if greek_word(w)]
# 	sum=len(word)
# 	passage=sample[0]
# 	for word in sample[1:]:
# 		passage=' '.join((passage,word))
# 	passage=re.sub(r"\.[ ]+(?=[Α-ΩA-Z])",".\n", passage)
# 	print(passage)
# 	fo = io.open(text, 'w', encoding='utf8')
# 	fo.write(passage)
# 	fo.close()
# 	jsonfile=re.sub("txt","json",text)
# 	fi = io.open(jsonfile, 'r', encoding='utf8')
# 	identity=json.load(fi)
# 	fi.close()
# 	identity['words']=sum
# 	fi = io.open(jsonfile, 'w+', encoding='utf8')
# 	json.dump(identity,fi,ensure_ascii=False,indent=4)
# 	fi.close()

# os.chdir(catalogues)
# fi=io.open('analysis.json','r',encoding='utf8')
# analysis=json.load(fi)
# fi.close()
# for category in analysis:
# 	if category['category']=='ART':
# 		for label in category['labels']:
# 			if label['label']=='SHOW':
# 				Tlist=label['texts']
# for t in range(2):
# 	theOne=random.choice(Tlist)
# 	print(theOne)
# print("hello")




# unit='0'
# for fl in os.listdir(root):
# 	checked=re.match(unit,fl)
# 	if checked:
# 		continue
# 	itstext=re.match(r'.*\.txt',fl)
# 	if itstext:
# 		continue
# 	unit=fl[:4]
# 	cat=[]
# 	for text in os.listdir(root):
# 		itstext=re.match(r'.*\.txt',text)
# 		if itstext:
# 			continue
# 		team=re.match(unit,text)
# 		if team:
# 			cat.append(text)
# 	i=0
# 	for title in cat:
# 		if i<10:
# 			num="".join(("0",str(i)))
# 		else:
# 			num=str(i)
# 		name=re.sub(r'^.{6}',''.join((unit,num)),title)
# 		print(name)
# 		oldtxt=re.sub(r"json","txt",title)
# 		print(oldtxt)
# 		newtxt=re.sub(r"json","txt",name)
# 		os.rename(title,name)
# 		os.rename(oldtxt,newtxt)
# 		i=i+1
	

# for fl in os.listdir(root):
# 	itstext=re.match(r'txt',fl)
# 	if itstext:
# 		continue
# 	character=re.match(r'..CH..\.json$',fl)
# 	comics=re.match(r'..CO..\.json$',fl)
# 	team=re.match(r'..TE..\.json$',fl)
# 	competition=re.match(r'..CO..\.json$',fl)
# 	computer=re.match(r'..CO..\.json$',fl)
# 	biology=re.match(r'..BI..\.json$',fl)
# 	if character:
# 		fo=io.open(fl,'r+',encoding='utf8')
# 		identity=json.load(fo)
# 		fo.close()
# 		if identity['label']=='CHARACTER':
# 			name=re.sub("CH","CR",fl)
# 			print(name)
# 			oldtxt=re.sub(r"json","txt",fl)
# 			print(oldtxt)
# 			newtxt=re.sub(r"json","txt",name)
# 			os.rename(fl,name)
# 			os.rename(oldtxt,newtxt)
# 		continue
# 	if comics:
# 		fo=io.open(fl,'r+',encoding='utf8')
# 		identity=json.load(fo)
# 		fo.close()
# 		if identity['label']=='COMICS':
# 			name=re.sub("CO","CC",fl)
# 			print(name)
# 			oldtxt=re.sub(r"json","txt",fl)
# 			print(oldtxt)
# 			newtxt=re.sub(r"json","txt",name)
# 			os.rename(fl,name)
# 			os.rename(oldtxt,newtxt)
# 		continue
# 	if team:
# 		fo=io.open(fl,'r+',encoding='utf8')
# 		identity=json.load(fo)
# 		fo.close()
# 		if identity['label']=='TEAM':
# 			name=re.sub("TE","TM",fl)
# 			print(name)
# 			oldtxt=re.sub(r"json","txt",fl)
# 			print(oldtxt)
# 			newtxt=re.sub(r"json","txt",name)
# 			os.rename(fl,name)
# 			os.rename(oldtxt,newtxt)
# 		continue
# 	if competition:
# 		fo=io.open(fl,'r+',encoding='utf8')
# 		identity=json.load(fo)
# 		fo.close()
# 		if identity['label']=='COMPETITION':
# 			name=re.sub("C0","CP",fl)
# 			print(name)
# 			oldtxt=re.sub(r"json","txt",fl)
# 			print(oldtxt)
# 			newtxt=re.sub(r"json","txt",name)
# 			os.rename(fl,name)
# 			os.rename(oldtxt,newtxt)
# 		continue
# 	if computer:
# 		fo=io.open(fl,'r+',encoding='utf8')
# 		identity=json.load(fo)
# 		fo.close()
# 		if identity['label']=='COMPUTER':
# 			name=re.sub("CO","CM",fl)
# 			print(name)
# 			oldtxt=re.sub(r"json","txt",fl)
# 			print(oldtxt)
# 			newtxt=re.sub(r"json","txt",name)
# 			os.rename(fl,name)
# 			os.rename(oldtxt,newtxt)
# 		continue
# 	if biology:
# 		fo=io.open(fl,'r+',encoding='utf8')
# 		identity=json.load(fo)
# 		fo.close()
# 		if identity['label']=='BIOLOGY':
# 			name=re.sub("BI","BL",fl)
# 			print(name)
# 			oldtxt=re.sub(r"json","txt",fl)
# 			print(oldtxt)
# 			newtxt=re.sub(r"json","txt",name)
# 			os.rename(fl,name)
# 			os.rename(oldtxt,newtxt)
# 		continue        
	# if nation:
	# 	fo=io.open(fl,'r+',encoding='utf8')
	# 	identity=json.load(fo)
	# 	fo.close()
	# 	if identity['label']=='NATION':
	# 		name=re.sub("NA","NT",fl)
	# 		print(name)
	# 		oldtxt=re.sub(r"json","txt",fl)
	# 		print(oldtxt)
	# 		newtxt=re.sub(r"json","txt",name)
	# 		os.rename(fl,name)
	# 		os.rename(oldtxt,newtxt)
	# 	continue

# croot='/Users/nic/Desktop/PythonProject/CORPUS'
# os.chdir(croot)
# root='/Users/nic/Desktop/PythonProject/Liber/Κοσμικισμός'
# os.chdir(root)
# fo=io.open('Χωρισμός_Κράτους_και_Εκκλησίας.txt','r',encoding='utf8')
# raw=fo.read()
# fo.close()
# sample = final_cut(raw)
# word=[w for w in sample if greek_word(w)]
# sum=len(word)
# print(sum)
# passage=sample[0]
# for word in sample[1:]:
# 	passage=' '.join((passage,word))
# passage=re.sub(r"\.[ ]+(?=[Α-ΩA-Z])",".\n", passage)
# print(passage)
# fi = io.open('Χωρισμός_Κράτους_και_Εκκλησίας.json', 'r', encoding='utf8')
# identity=json.load(fi)
# fi.close()
# os.chdir(croot)
# fo=io.open('SOPO13.txt','w',encoding='utf8')
# fo.write(passage)
# fo.close()
# jsonfile='SOPO13.json'
# identity['words']=sum
# fi = io.open(jsonfile, 'w+', encoding='utf8')
# json.dump(identity,fi,ensure_ascii=False,indent=4)
# fi.close()