import io
import os
import re
from functions import final_cut, greek_word,names
import json

dest='/Users/nic/Desktop/PythonProject/CORPUS'
os.chdir(dest)
contents= os.listdir(dest)
for text in contents:
	itsjson = re.match(r'.*\.json', text)
	if itsjson:
		continue
	print(text)
	fo = io.open(text, 'r', encoding='utf8')
	raw = fo.read()
	fo.close()
	sample = final_cut(raw)
	word=[w for w in sample if greek_word(w)]
	sum=len(word)
	passage=sample[0]
	for word in sample[1:]:
		passage=' '.join((passage,word))
	passage=re.sub(r"\.[ ]+(?=[Α-ΩA-Z])",".\n", passage)
	print(passage)
	fo = io.open(text, 'w', encoding='utf8')
	fo.write(passage)
	fo.close()
	jsonfile=re.sub("txt","json",text)
	fi = io.open(jsonfile, 'r', encoding='utf8')
	identity=json.load(fi)
	fi.close()
	identity['words']=sum
	fi = io.open(jsonfile, 'w+', encoding='utf8')
	json.dump(identity,fi,ensure_ascii=False,indent=4)
	fi.close()
names(dest)
