import re
import os
import io
from functions import extract_urls,inspection,read_dicts,text_sorting,categories_surfer

corpus_root = '/Users/nic/Desktop/PythonProject/Geo'
os.mkdir(corpus_root)
os.chdir(corpus_root)
father_url = "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CF%84%CE%B7%CE%B3%CE%BF%CF%81%CE%AF%CE%B1:%CE%93%CE%B5%CF%89%CE%B3%CF%81%CE%B1%CF%86%CE%AF%CE%B1"
start = "id=\"mw-subcategories\""
end = "title=\"Ειδικό:Κατηγορίες\""
url_list = extract_urls(father_url, start, end)
for dict in url_list:
	print(dict['title'])
archive=io.open('archive.txt','a+',encoding='utf8')
for link in url_list:
	new=re.sub(r'[^\w ]',' ',link['title'])
	new=re.sub('Κατηγορία', '', new)
	new_dir='/'.join((corpus_root,new))
	catalogue=os.listdir(corpus_root)
	guilty=inspection(new, catalogue)
	if guilty:
		print(new)
		continue
	os.mkdir(new_dir)
	os.chdir(new_dir)
	categories_surfer(link,archive)
	read_dicts(new_dir)
	text_sorting(new_dir)
	print("texts sorted and formated")
archive.close()
