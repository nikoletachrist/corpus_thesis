import io
import os
import re
import json

root='/Users/nic/Desktop/PythonProject/CORPUS'
arts = '/Users/nic/Desktop/corpus/10/Arts'
athl = '/Users/nic/Desktop/corpus/10/Athl'
geo = '/Users/nic/Desktop/corpus/10/Geo'
hist = '/Users/nic/Desktop/corpus/10/Hist'
liber = '/Users/nic/Desktop/corpus/10/Liber'
rel = '/Users/nic/Desktop/corpus/10/Rel'
scie = '/Users/nic/Desktop/corpus/10/Scie'
socie='/Users/nic/Desktop/corpus/10/Socie'
sources=[arts,athl,geo,hist,liber,rel,scie,socie]


patterns1=[r'Συντεταγμένες:.*?\/ ?-?\d+\.?\d*; ?-?\d+\.?\d* ']
patterns2=[r'\.([^\.\:]+)\:[^\.]+ +$', r'\.[^\.]+: +$']
patterns3=[r'\[στ\]',r'\[(i+v?|vi*)\]', r'\[[a-zα-ω]\]',r'[α-ωa-z] \[ \›\]']
patterns4=[r'\[(Σ|σ)ημ( |\. ?)[0-9]+\]', r'\[ ?[0-9]+ ?\]', r'\[ *(n|σ|Π|Ν|Σ) [0-9]+ *\]', r'\[ *(Ν|n)ote [0-9]+ *\]',r'\[(Σ|σ)ημείωση [0-9]+\]', r'\[Υποσημ\. 1\]']
patterns5=[r'π • σ • ε ?', r'\[Αρχείο:.*?\]', r'(Δ|δ)είτε κείμενο', r'\[Παραπομπή που απαιτείται\]']
patterns6=[r'^( *([A-Za-z]{3,})\s){3,}', r'^(([A-Z][a-z]{2,}|[a-z]+|[0-9]+)(\s|:|\(|\[|\]|\)|\-|–)+){3,}']
patterns7=[r'^ *Β\' Παγκόσμιος Πόλεμος ', r'^( ){0,}Έμβλημα( ){0,}', r'^( ){0,}Σημαία( ){0,}', r'† Συμμετοχές \(Γκολ\)']
patterns8=[r'\.([^\.\(\)]+\([^\(\)]+\))+ +$']
patterns9=[r'\.([^\.\(\)]+\([^\(\)]+\))+ +$']

os.chdir(root)
patterns=patterns1
texts=[]
fix=[]
for source in sources:
	for cont in os.listdir(source):
		notfol=re.match(r'.*\.(json|txt)$',cont)
		if notfol:
			continue
		folder='/'.join((source,cont))
		os.chdir(folder)
		texts=os.listdir(folder)
		for text in texts:
			nottxt=re.match(r'.*\.json$',text)
			if nottxt:
				continue
			print(text)
			fr=io.open(text,'r+',encoding='utf8')
			raw=fr.read()
			fr.close()
			for pattern in patterns:
				matchobj=re.search(pattern,raw)
				if matchobj:
					string=matchobj.group()
	                print(string)
	                fix.append({'fileid':text,"folder":folder,'pattern':string})
os.chdir(root)
fo=io.open("fixes.json",'w',encoding='utf8')
json.dump(fix,fo,ensure_ascii=False,indent=4)
fo.close()    

