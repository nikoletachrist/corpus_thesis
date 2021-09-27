import os
from functions import check_catalogue,tags,sort_catalogue

root='/Users/nic/Desktop/PythonProject'
arts = '/Users/nic/Desktop/PythonProject/Arts'
athl = '/Users/nic/Desktop/PythonProject/Athl'
geo = '/Users/nic/Desktop/PythonProject/Geo'
hist = '/Users/nic/Desktop/PythonProject/Hist'
liber = '/Users/nic/Desktop/PythonProject/Liber'
rel = '/Users/nic/Desktop/PythonProject/Rel'
scie = '/Users/nic/Desktop/PythonProject/Scie'
socie='/Users/nic/Desktop/PythonProject/Socie'
doubles='/Users/nic/Desktop/PythonProject/Doubles'
sources=[arts,athl,geo,hist,liber,rel,scie,socie]
os.chdir(root)

catalogue=[]
for source in sources:
	tag_cat=tags(source,catalogue)
	catalogue=[]
	for item in tag_cat:
		catalogue.append(item)
sort_catalogue(catalogue)
print(catalogue)
print(len(catalogue))
	
# check_catalogue()
