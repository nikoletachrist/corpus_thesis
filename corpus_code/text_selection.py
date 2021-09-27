import io
import os
from utilities import final_set
import json

root='/Users/nic/Desktop/PythonProject'
dest='/Users/nic/Desktop/PythonProject/CORPUS'
catalogues="C:/Users/nic/Desktop/PythonProject/categ_analysis"
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

os.chdir(catalogues)
fo=io.open('stock.json','r',encoding='utf8')
stock=json.load(fo)
fo.close()
fi=io.open('analysis.json','r',encoding='utf8')
analysis=json.load(fi)
fi.close()
for category in analysis:
	destin='/'.join((dest,category['category']))
	os.mkdir(destin)
	for label in category['labels']:
		tList=label['texts']
		for item in stock:
			if category['category']==item['category']:
				for obj in item['perlabel']:
					if obj['label']==label['label']:
						tNum=obj['samples']
						final_set(tList,tNum,destin)





