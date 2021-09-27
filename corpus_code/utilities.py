import re
import os
from nltk import word_tokenize
import requests
from bs4 import BeautifulSoup, SoupStrainer
import random
import io
import shutil
import json
import math

def inspection(object,object_list):
	for item in object_list:
		matchobj=re.match(item, object)
		if matchobj:
			return 1 
	return  0

def extract_urls(father_url, start, end):
	html = requests.get(father_url)
	startpoint = html.text.find(start)
	endpoint = html.text.find(end)
	usefullText = html.text[startpoint:endpoint]
	soup = BeautifulSoup(usefullText, 'html.parser')
	url_list = []
	only_urls=[]
	guilty=0
	for link in soup.find_all('a'):
		name = link.get('title')
		partial_url = link.get('href')
		if partial_url == None:
			continue
		matchobj = re.match(r'^/wiki/*', partial_url)
		if matchobj:
			url = "".join(("https://el.wikipedia.org", partial_url))
		if len(only_urls)>=1:
			guilty =inspection(url,only_urls) 
		if guilty:
			print(name)
			print("BUSTED")
			continue
		url_list.append({'title':name,'site':url})
		only_urls.append(url)
	print("All urls have been extracted")
	return url_list

def categories_surfer(link,archive):
	deep=5
	category = []
	url_list = []
	category.append({'title': link['title'], 'site': link['site'], 'depth':0})
	fo = io.open('urls.json', 'a+',  encoding='utf8')
	fp = io.open('categories.json', 'a+', encoding='utf8')
	archive.write(category[0]['site'])
	archive.write('\n')
	archive.flush()
	archive.seek(0)
	arcraw=archive.read()
	archive_urls = arcraw.splitlines()
	while(category[0]['depth'] <= deep ):
		try:
			html = requests.get(category[0]['site'])
		except:
			continue
		act = category[0]['depth']
		start = html.text.find("id=\"mw-subcategories\"")
		if start==-1:
			start=html.text.find("id=\"mw-pages\"")
		end = html.text.find("id=\"mw-normal-catlinks\"")
		if start==-1:
			break
		usefullText = html.text[start:end]
		soup = BeautifulSoup(usefullText, 'html.parser')
		for obj in soup.find_all('a'):
			name = obj.get('title')
			if name == None:
				continue
			print(name)
			categories = re.match("Κατηγορία:", name)
			partial_url = obj.get('href')
			if partial_url == None:
				continue
			matchobj = re.match(r'^/wiki/*', partial_url)
			if matchobj:
				url = "".join(("https://el.wikipedia.org", partial_url))
				guilty = inspection(url, archive_urls)
				if guilty:
					print("BUSTED")
					continue
				if categories:
					category.append({'title': name, 'site': url, 'depth': act+1})
					if act+1>deep:
						continue
					archive_urls.append(url)
					archive.write(url)
					archive.write('\n')
				else:
					url_list.append({'title': name, 'site': url,'team':category[0]['title']})
					archive_urls.append(url)
					archive.write(url)
					archive.write('\n')
					print("url have been extracted")
		archive.flush()
		category.remove(category[0])
		if len(category)<1:
			break
	json.dump(url_list, fo, ensure_ascii=False)
	json.dump(category, fp, ensure_ascii=False)
	fp.close()
	fo.close()

def get_raw_text(link):
	only_p=SoupStrainer("p")
	url=link['site']
	html= requests.get(url)
	soup = BeautifulSoup(html.text,"html.parser", parse_only=only_p )
	full_text=soup.getText()
	raw=re.sub(r'\[[0-9]+\]',"",full_text)
	raw=re.sub("\n", " ", raw)
	name=re.sub(r'[^\w ]','',link['title'])
	name=re.sub(' ','_',name)
	txtname=''.join((name,'.txt'))
	jsonname=''.join((name,'.json'))
	txtfile = io.open(txtname, "a+", encoding='utf8')
	jsonfile=io.open(jsonname,'a+',encoding='utf8')
	json.dump(link, jsonfile, ensure_ascii=False)
	txtfile.write(raw)
	txtfile.close()
	jsonfile.close()
	print(txtname)

def read_dicts(folder):
	url_file = io.open('urls.json', "r+", encoding='utf8')
	urls = json.load(url_file )
	url_file.close()
	categ_file=io.open('categories.json','r+',encoding='utf8')
	categories=json.load(categ_file)
	categ_file.close()
	if len(urls)==0:
		if len(categories)==0:
			return
		link=categories[0]
		get_raw_text(link)
		print(folder)
		return 
	for url in urls:
		get_raw_text(url)
	print('READY')

def greek_word(word):
	matchobj=re.match(r'^[^a-zA-Z0-9]+$',word)
	if word.isalpha():
		if matchobj:
			return 1 

def text_sorting(root):
	print(root)
	os.chdir(root)
	filelist=os.listdir(root)
	textlist=[]
	usefulltexts=[]
	for f in filelist:
		matchobj=re.match(r'.*\.txt$', f)
		if matchobj:
			textlist.append(f)
	for fileid in textlist:
		print(fileid)
		fo=io.open(fileid,"r+", encoding='utf8')
		raw=fo.read()
		text=word_tokenize(raw)
		word=[w for w in text if greek_word(w)]
		if len(word)>2000:
			usefulltexts.append(fileid)
			fo.close()
		else:
			fo.close()
			os.remove(fileid)
			jsonid=re.sub('.txt','.json', fileid)
			os.remove(jsonid)
	return usefulltexts

def full_text_list(root):
	root_name=re.sub('/Users/nic/Desktop/PythonProject/','',root)
	os.chdir(root)
	texts = []
	folders = os.listdir(root)
	for fol in folders:
		matcho = re.match(r'.*\.(txt|json)', fol)
		if matcho:
			continue
		direct = '/'.join((root, fol))
		ind = os.listdir(direct)
		for t in ind:
			matchobj = re.match('.*\.txt', t)
			if matchobj:
				texts.append({'title':t,'folder':fol,'source':root_name})
	return texts

def compare_entries(comparable1,comparable2):
	dest='/Users/nic/Desktop/PythonProject/Doubles'
	doubles='/'.join((dest,'doubles.json'))
	fo=io.open(doubles,'r+',encoding='utf8')
	fo.seek(0)
	guilt=json.load(fo)
	if len(guilt)==0:
		guilt=[]
	root_texts=full_text_list(comparable1)
	comp_texts=full_text_list(comparable2)
	root_list=[]
	for text in root_texts:
		root_list.append(text['title'])
	for text in comp_texts:
		guilty=inspection(text['title'], root_list)
		if guilty:
			guilt.append(text)
			contents=os.listdir(dest)
			multiples=inspection(text['title'], contents)
			jsonfile=re.sub('.txt','.json', text['title'])
			direct='/'.join((comparable2,text['folder']))
			os.chdir(direct)
			if multiples:
				os.remove(text['title'])
				os.remove(jsonfile)
				continue
			shutil.move((text['title']),dest)
			shutil.move(jsonfile,dest)
			print(text)
	os.chdir(dest)
	fo.seek(0)
	json.dump(guilt, fo, ensure_ascii=False)
	fo.close()

def count_results(root):
	os.chdir(root)
	texts = []
	fine_index = []
	texts=full_text_list(root)
	fol=texts[0]['folder']
	length=0
	for text in texts:
		if text['folder']==fol:
			length=length+1
		else:
			fine_index.append({'foldel': fol, 'items': length})
			length=1
			fol=text['folder']
	fine_index.append({'foldel': fol, 'items': length})
	return fine_index

def sum_texts(index_list):
	sum=0
	for fol in index_list:
		sum=sum+int(fol['items'])
	return sum

def add_keys(sources):
	for source in sources:
		contents=os.listdir(source) 
		for cont in contents:
			matchobj=re.match(r'.*\.(txt|json)',cont)
			if matchobj:
				continue
			print(cont)
			directory='/'.join((source,cont))
			os.chdir(directory)
			files=os.listdir(directory)
			for f in files:
				itstxt=re.match(r'(.*\.txt|^urls\.json$|^categories\.json$)',f)
				if itstxt:
					continue
				print(f)
				txtname=re.sub('.json','.txt', f)
				nothere=inspection(txtname, files)
				if nothere==0:
					os.remove(f)
					continue
				jsonfile = io.open(f, "r+", encoding='utf8')
				values= json.load(jsonfile)
				if len(values.items())==5:
					new_keys={"folder":cont,"words":0}
				else:
					new_keys={"category":"NONE","label":"NONE","folder":cont,"words":0}
				values.update(new_keys)
				print(values)
				jsonfile.seek(0)
				json.dump(values, jsonfile,ensure_ascii=False,indent=4)
				jsonfile.close()

def tags(root,tag_catalogue):
	os.chdir(root)
	for folder in os.listdir(root):
		matchobj = re.match(r'.*\.(txt|json)', folder)
		if matchobj:
			continue
		direct='/'.join((root,folder))
		os.chdir(direct)
		for fileid in os.listdir(direct):
			itstxt=re.match(r'(.*\.txt|^urls\.json$|^categories\.json$)',fileid)
			if itstxt:
				continue
			fo=io.open(fileid,'r',encoding='utf8')
			identity=json.load(fo)
			fo.close()
			tag_catalogue.append({'filepath':{'name':fileid,'source':direct},'category':identity['category'],'label':identity['label']})
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
						texts.append(dictionary['filepath'])
			textsperlabel={'label':label,'texts':texts}
			labelspercategory.append(textsperlabel)
			texts=[]	
		graph={'category':category,'labels':labelspercategory}
		graphs.append(graph)
		print(graph)
		labelspercategory=[]
		labels=[]
	os.chdir(dest)
	fo=io.open('analysis.json','w',encoding='utf8')
	json.dump(graphs,fo,ensure_ascii=False,indent=4)
	fo.close()
	print(graphs)

def check_catalogue():
	root='C:/Users/nic/Desktop/PythonProject/categ_analysis'
	os.chdir(root)
	fo=io.open('analysis.json','r',encoding='utf8')
	analysis=json.load(fo)
	fo.close()
	for category in analysis:
		for label in category['labels']:
			for text in label['texts']:
				os.chdir(text['source'])
				fo=io.open(text['name'],'r',encoding='utf8')
				identity=json.load(fo)
				fo.close()
				if identity['category']==category['category'] and identity['label']==label['label']:
					continue
				else:
					identity['category']=category['category']
					identity['label']=label['label']
					fo=io.open(text['name'],'w',encoding='utf8')
					json.dump(identity,fo,ensure_ascii=False,indent=4)
					fo.close()
					print(identity)
					print('done')
	print("nothing")

def stock():
	fo = io.open('analysis.json', 'r', encoding='utf8')
	analysis = json.load(fo)
	fo.close()
	counting = []
	total = 0
	for category in analysis:
		labelpercategory = []
		count = 0
		for label in category['labels']:
			count = count+len(label['texts'])
			lenperlabel = {'label': label['label'],
			    'sum': (len(label['texts'])), 'samples': 0}
			labelpercategory.append(lenperlabel)
		counting.append(
		    {'category': category['category'], 'sum': count, 'samples': 0, 'perlabel': labelpercategory})
		total = total+count
	fn = io.open('stock.json', 'w', encoding='utf8')
	json.dump(counting, fn, ensure_ascii=False, indent=4)
	fn.close()
	print(total)
	return total

def share_samples(label_list, total, final):
	count = 0
	rest=[]
	for i in range (len(label_list)):
		number=label_list[i]['sum']
		sample=math.modf(final*(number/total))
		count=count+int(sample[1])
		rest.append({'s':int(sample[1]),'r':sample[0]})
	minus=1
	while count<final:
		for i in range(len(rest)):
			point=0
			for j in range(len(rest)):
				if i!=j:
					if rest[i]['r']>=rest[j]['r']:
						point=point+1
			if point==len(rest)-minus:
				minus=minus+1
				rest[i]['s']=rest[i]['s']+1
				count=count+1
				break
	print(count)
	for i in range(len(label_list)):
		label_list[i]['samples']=rest[i]['s']
	for label in label_list:
		print("files['category'] :",label['category'],", files['samples'] :",label['samples'])

def final_set(texts,samples,dest):
	for t in range(samples):
		theOne=random.choice(texts)
		print(theOne)
		foldercont=os.listdir(dest)
		guilty=inspection(theOne['name'],foldercont)
		while guilty:
			theOne=random.choice(texts)
			print(theOne)
			foldercont=os.listdir(dest)
			guilty=inspection(theOne['name'],foldercont)
		os.chdir(theOne['source'])
		txtname=re.sub('.json','.txt',theOne['name'])
		shutil.copy(theOne['name'],dest)
		shutil.copy(txtname,dest)

def final_cut(raw):
	words=word_tokenize(raw)
	count=0
	pos=0
	dotindex=[0]
	startendPairs=[]
	for w in words:
		if w is '.':
			if pos+1>=len(words):
				dotindex.append(pos+1)
				pos= pos+1
				continue
			matchobj=re.match(r'[A-ZΑ-ΩΈΆΊΌΏΎΉ].*',words[pos+1])
			if matchobj:
				dotindex.append(pos+1)
		pos= pos+1
	pos=0
	for index in dotindex:
		for w in words[index:]:
			if greek_word(w):
				count=count+1
			if count>=2000:
				if w is '.':
					startendPairs.append((index,index+pos+1))
					break
			pos=pos+1
		count=0
		pos=0
	num=random.randrange(0,len(startendPairs),1)
	start=startendPairs[num][0]
	end=startendPairs[num][1]
	print("sample has been taken!")
	return words[start:end]

def create_pre(categ,label):
	print(label)
	character=re.match(r'CHARACTER',label)
	if character:
		prefix="".join((categ[:2],'CR'))
		return prefix
	comics=re.match(r'COMICS',label)
	if comics:
		prefix="".join((categ[:2],'CC'))
		return prefix
	engineering=re.match(r'ENGINEERING',label)
	if engineering:
		prefix="".join((categ[:2],'EG'))
		return prefix
	team=re.match(r'TEAM',label)
	if team:
		prefix="".join((categ[:2],'TM'))
		return prefix
	competition=re.match(r'COMPETITION',label)
	if competition:
		prefix="".join((categ[:2],'CP'))
		return prefix
	computer=re.match(r'COMPUTER',label)
	if computer:
		prefix="".join((categ[:2],'CM'))
		return prefix
	biology=re.match(r'BIOLOGY',label)
	if biology:
		prefix="".join((categ[:2],'BL'))
		return prefix
	nation=re.match(r'NATION',label)
	if nation:
		prefix="".join((categ[:2],'NT'))
		return prefix
	else:
		prefix="".join((categ[:2],label[:2]))
	print(prefix)
	return prefix

def names(root):
	os.chdir(root)
	texts=os.listdir(root)
	for text in texts:
		matcho = re.match(r'.*\.json', text)
		if not matcho:
			continue
		json_file=io.open(text,'r+',encoding='utf8')
		identity=json.load(json_file)
		json_file.close()
		categ=identity["category"]
		label=identity["label"]
		prefix=create_pre(categ,label)
		n="".join((prefix,r'\d\d\d?\.json'))
		count=0
		for item in os.listdir(root):
			matchpre = re.match(n, item)
			if matchpre:
				count=count+1
		if count<10:
			num="".join(("0",str(count)))
		else:
			num=str(count)
		oldtxt=re.sub(r"json","txt",text)
		print(oldtxt)
		newjson="".join(("".join((prefix,num)),".json"))
		print(newjson)
		newtxt="".join(("".join((prefix,num)),".txt"))
		os.rename(text,newjson)
		os.rename(oldtxt,newtxt)	