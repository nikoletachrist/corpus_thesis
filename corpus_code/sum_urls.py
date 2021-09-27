import io
import os
import re
from utilities import inspection
import json

root='/Users/nic/Desktop/PythonProject'
arts = '/Users/nic/Desktop/PythonProject/Arts'
athl = '/Users/nic/Desktop/PythonProject/Athl'
geo = '/Users/nic/Desktop/PythonProject/Geo'
hist = '/Users/nic/Desktop/PythonProject/Hist'
liber = '/Users/nic/Desktop/PythonProject/Liber'
rel = '/Users/nic/Desktop/PythonProject/Rel'
scie = '/Users/nic/Desktop/PythonProject/Scie'
socie='/Users/nic/Desktop/PythonProject/Socie'
sources=[arts,athl,geo,hist,liber,rel,scie,socie]
count=0
os.chdir(root)
allurls=[]
for source in sources:
	contents=os.listdir(source)
	for content in contents:
		matchone=re.match(r'.*\.txt',content)
		if matchone:
			continue
		matchtwo=re.match(r'.*\.json',content)
		if matchtwo:
			print(content)
			os.chdir(source)
			fo=io.open(content,'r',encoding='utf8')
		else:
			folder='/'.join((source,content))
			print(folder)
			os.chdir(folder)
			fo=io.open('urls.json','r',encoding='utf8')
		urls=json.load(fo)
		for url in urls:
			print(url['title'])
			guilty=inspection(url['site'], allurls)
			if guilty:
				print('Busted')
				continue
			allurls.append(url['site'])
		fo.close()
		count=count+len(urls)
		print(count)
		print(len(allurls))
print('FINAL')
print(count)
print(len(allurls))
os.chdir(root)
fp=io.open('allurls.json','w',encoding='utf8')
json.dump(allurls,fp,ensure_ascii=False)
fp.close()