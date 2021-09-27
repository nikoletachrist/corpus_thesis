
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


os.chdir(root)
# fr=io.open("fixes.json",'r',encoding='utf8')
# texts=json.load(fr)
# fr.close()
texts=[]
for text in os.listdir(root):
	matchobj=re.match(r'.*\.(json|csv)',text)
	if not matchobj:
		texts.append(text)
fix=[]
patterns=[r'\n[^\.]+\.$']
for text in texts:
	fr=io.open(text,'r+',encoding='utf8')
	raw=fr.read()
	fr.close()
	for pattern in patterns:
		matchobj=re.search(pattern,raw)
		if matchobj:
			string=matchobj.group()
			print(string)
			fix.append({'fileid':text,'pattern':string})
os.chdir(root)
fo=io.open("fixes.json",'w',encoding='utf8')
json.dump(fix,fo,ensure_ascii=False,indent=4)
fo.close()  

# for text in fix[2:]:
# 	os.chdir(root)
# 	jsonfile=re.sub("txt",'json',text['fileid'])
# 	fr=io.open(jsonfile,'r',encoding='utf8')
# 	ident=json.load(fr)
# 	fr.close()
# 	print(ident['title'])
# 	for source in sources:
# 		os.chdir(source)
# 		for folder in os.listdir(source):
# 			matchobj=re.match(ident['folder'],folder)
# 			if not matchobj:
# 				continue
# 			os.chdir(folder)
# 			name=re.sub(r'[^\w ]','',ident['title'])
# 			name=re.sub(' ','_',name)
# 			fo=io.open(''.join((name,'.txt')),'r',encoding='utf8')
# 			raw=fo.read()
# 			fo.close()
# 			os.chdir(root)
# 			sample = final_cut(raw)
# 			word=[w for w in sample if greek_word(w)]
# 			sum=len(word)
# 			passage=sample[0]
# 			for word in sample[1:]:
# 				passage=' '.join((passage,word))
# 			passage=re.sub(r"\.[ ]+(?=[Α-ΩA-Z])",".\n", passage)
# 			print(passage)
# 			fo = io.open(text['fileid'], 'w', encoding='utf8')
# 			fo.write(passage)
# 			fo.close()
# 			# jsonfile=re.sub("txt","json",text)
# 			fi = io.open(jsonfile, 'r', encoding='utf8')
# 			identity=json.load(fi)
# 			fi.close()
# 			identity['words']=sum
# 			fi = io.open(jsonfile, 'w+', encoding='utf8')
# 			json.dump(identity,fi,ensure_ascii=False,indent=4)
# 			fi.close()


# # fr=io.open("fixes.json",'r',encoding='utf8')
# # fix=json.load(fr)
# # fr.close()
# # fix=[]
# sources=[root]
# # # patterns=[r'[A-ZΑ-Ω]{1,} ?\. *([Α-ΩA-Zα-ωa-z]{1,} ?\. *)+(?=[Α-ΩA-Z][α-ωa-z]+)']
# # # patterns=[r'\.[^\s[A-Za-zΑ-Ωα-ω][0-9]]']
# patterns=[r'\n[^\.]+\.$']
# for source in sources:
#     for text in os.listdir(source):
#         # notfol=re.match(r'.*\.(json|txt)$',cont)
#         # if notfol:
#         #     continue
#         # folder='/'.join((source,cont))
#         # os.chdir(folder)
#         # texts=os.listdir(folder)
#     # for text in texts:
#         nottxt=re.match(r'.*\.json$',text)
#         if nottxt:
#             continue
#         print(text)
#         fr=io.open(text,'r+',encoding='utf8')
#         raw=fr.read()
#         fr.close()
#         for pattern in patterns:
#             matchobj=re.search(pattern,raw)
#             if matchobj:
#                 string=matchobj.group()
#                 # ignore=re.match(r'(μ\.(Χ\.|μ\.|χ\.)|κ\.(α\.|λπ\.|μ\.|κ\.)|π\.(Χ\.|χ\.|μ\.|π\.)|ο\.(κ\.|χ\.)|ε\.φ\.|τ\.(χλμ\.|χ\.|λ\.)|λ\.(χ\.|π\.))\n.*', string)
#                 # if ignore:
#                 #     continue
#                 print(string)
#                 fix.append({'fileid':text,'pattern':string})
# os.chdir(root)
# fo=io.open("fixes.json",'w',encoding='utf8')
# json.dump(fix,fo,ensure_ascii=False,indent=4)
# fo.close()    


# for text in fix:
#     print(text)
#     os.chdir(text['folder'])
#     fr=io.open(text['fileid'],'r+',encoding='utf8')
#     raw=fr.read()
#     fr.close()
#     new=''.join((text['pattern'],'. '))
#     fixed=re.sub(r'\.[^\.]+ +$',new,raw)
#     fw=io.open(text['fileid'],'w',encoding='utf8')
#     fw.write(fixed)
#     fw.close()
#     print('Done')

# " http://www.thelatinlibrary.com/sen/sen.tranq.shtml http://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/42*.html http://www.forumromanum.org/literature/gellius7.html#17 http://www.forumromanum.org/literature/ammianus22.html  "
# Ο πλήρης κατάλογος
# 'folder':folder,
#Patterns που εχω καθαρίσει
## patterns=[r'Συντεταγμένες:(.*?\/){2}.*?;( ){1,}(\d){1,}\.(\d){1,}( ){1,}',r'_{2,}',r'^ +',r'Παρακαλούμε βοηθήστε στην βελτίωση της μετάφρασής του\.']
## patterns=[r'^ *Β\' Παγκόσμιος Πόλεμος ',r'^( ){0,}Έμβλημα( ){0,}',r'^( ){0,}Σημαία( ){0,}',r'\[.*?\]',r'\[.*?\|.*\]',r'^( *([A-Za-z]{3,})\s){3,}']
## patterns=[r'[^(\.\s?)]$',r'^(([A-Z][a-z]{2,}|[a-z]+|[0-9]+)(\s|:|\(|\[|\]|\)|\-|–)+){3,}',r'\[ ?(παραπομπή που απαιτείται|(ν|Ν)εκρός σύνδεσμος|(Χ|χ)ρειάζεται σελίδα|χρειάζεται αποσαφήνιση|(Α|α)παιτείται αναφορά|δεν αναφέρεται στην παραπομπή|Note 1) ?\]']
## patterns=[r'Συντεταγμένες:.*?\/ ?-?\d+\.?\d*; ?-?\d+\.?\d* ',r'\[εκκρεμεί παραπομπή\]',r'\[Σημ( |\. ?)[0-9]\]',r'\[(i+v?|vi*)\]',r'\[Υποσημ\. 1\]',r'\[Σ [0-9]\]',r'\[N [0-9]\]',r'\[[a-zα-ω]\]']
## patterns=[r'^([0-9]+(\s|:|\-|–|\.|\w*|,|)+)+',r'^[0-9]+',[r'[α-ωa-z]\[\›\]',r'\[(Σ|σ)ημ( |\. ?)[0-9]+\]',r'\[sic\]',r'\[στ\]',r'\[ ?[0-9]+ ?\]',r'\[ *(n|σ|Π|Ν|Σ) [0-9]+ *\]',r'\[ασαφές\]',r'\[ *note [0-9]+ *\]',r'\[σημείωση [0-9]+\]']
##patterns=[r'Κατηγορία:',r'† Συμμετοχές \(Γκολ\)',r'ɪ? ?\(βοήθεια·λήψη\)',r'\(see footnote\)'',r'π • σ • ε ?',r'(Δ|δ)είτε κείμενο',r'\.([^\.\:]+)\:[^\.]+ +$']
##patterns=[r'\[Παραπομπή που απαιτείται\]',r'\[Αρχείο:.*?\]',r'\[Σημείωση [0-9] *\]',r'\{\\ ?(frac|displaystyle|mathrm).*?(\} )+ *',r'\.[^\.]+: +$',r'\.([^\.\(\)]+\([^\(\)]+\))+ +$']

#Patterns που ΔΕΝ έχω καθαρίσει
# patterns=[r' \d{1,2} ?\.\s(\w+\s+\d{1,2} ?\.\s){1,}',r'[Α-Ωα-ω]\.[Α-Ωα-ω](\w+)?\.\n\w+ '];
# patterns=[r'(\(Πηγή: )?http\:\/\/(.*?\.){1,2}(.*?[^\)])\s',r'\[.*?\]',r'\{.*?\\.*?(\} )+ *',r'\{.*?\}']
#r'[[Πρίγκιπας Ανδρέας της Ελλάδας|πρίγκηπα Ανδρέα]'
# patterns=[r'\.([^\.][\w\d\(\)])+ $',r'.{,30}\([^\(\)]+\) ?$'] 