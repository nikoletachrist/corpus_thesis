import json
import os
import io
from utilities import full_text_list,count_results,sum_texts,compare_entries

root = '/Users/nic/Desktop/PythonProject'
catal = 'C:/Users/nic/Desktop/PythonProject/categ_analysis'
arts = '/Users/nic/Desktop/PythonProject/Arts'
athl = '/Users/nic/Desktop/PythonProject/Athl'
geo = '/Users/nic/Desktop/PythonProject/Geo'
hist = '/Users/nic/Desktop/PythonProject/Hist'
liber = '/Users/nic/Desktop/PythonProject/Liber'
rel = '/Users/nic/Desktop/PythonProject/Rel'
scie = '/Users/nic/Desktop/PythonProject/Scie'
socie = '/Users/nic/Desktop/PythonProject/Socie'
sources = [arts, athl, geo, hist, liber, rel, scie, socie]

os.chdir(root)
for i in range(len(sources)):
	comparable1=sources[i]
	for source in sources[i+1:]:
		comparable2=source
		compare_entries(comparable1, comparable2)
fo=io.open('catalogue.json','w+',encoding='utf8')
catalogue=[]
counter=[]
for source in sources:
    index=full_text_list(source)
    results=count_results(source)
    for folder in results:
        counter.append(folder)
    for text in index:
        catalogue.append(text)
os.chdir(root)
json.dump(catalogue,fo,ensure_ascii=False)
fo.close()
print(counter)
print(sum_texts(counter))

