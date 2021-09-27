import io
import os
from utilities import stock, share_samples
import json


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

os.chdir(catal)
total=stock()
fo=io.open('stock.json','r',encoding='utf8')
analysis=json.load(fo)
fo.close()
final=500
share_samples(analysis, total, final)
for item in analysis:
	total=item['sum']
	final=item['samples']
	share_samples(item['perlabel'], total, final)
	for obj in item['perlabel']:
		print(obj)
fn = io.open('stock.json', 'w', encoding='utf8')
json.dump(analysis, fn, ensure_ascii=False, indent=4)
fn.close()
