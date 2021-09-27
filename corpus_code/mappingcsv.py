import nltk
import re
import pprint
import os
from nltk import word_tokenize, sent_tokenize
from nltk.corpus.reader import wordlist
import requests
from bs4 import BeautifulSoup, SoupStrainer
import random
import glob
import io
import shutil
from nltk.corpus import PlaintextCorpusReader,CategorizedCorpusReader,CategorizedPlaintextCorpusReader
from nltk.text import TextCollection
import json
from xml.etree.ElementTree import ElementTree 	
from functions import full_text_list

root='C:/Users/nic/Desktop/PythonProject/CORPUS'
os.chdir(root)

catmap='ARAR00.txt,art\n'
for f in os.listdir(root)[2:]:
	print(f)
	machobj=re.match(r'.+\.json',f)
	if machobj:
		continue
	art=re.match(r'AR.{4}\.txt',f)
	if art:
		entry=','.join((f,'art\n'))
		catmap=''.join((catmap,entry))
	geography=re.match(r'GE.{4}\.txt',f)
	if geography:
		entry=','.join((f,'geography\n'))
		catmap=''.join((catmap,entry))
	history=re.match(r'HI.{4}\.txt',f)
	if history:
		entry=','.join((f,'history\n'))
		catmap=''.join((catmap,entry))
	religion=re.match(r'RE.{4}\.txt',f)
	if religion:
		entry=','.join((f,'religion\n'))
		catmap=''.join((catmap,entry))
	science=re.match(r'SC.{4}\.txt',f)
	if science:
		entry=','.join((f,'science\n'))
		catmap=''.join((catmap,entry))
	society=re.match(r'SO.{4}\.txt',f)
	if society:
		entry=','.join((f,'society\n'))
		catmap=''.join((catmap,entry))
	sports=re.match(r'SP.{4}\.txt',f)
	if sports:
		entry=','.join((f,'sports\n'))
		catmap=''.join((catmap,entry))
print(catmap)
jsonfile=io.open('cat_map.csv','a+',encoding='utf8')
jsonfile.write(catmap)
jsonfile.close()

catmap='ARAR00.txt,artifact\n'
for f in os.listdir(root)[2:]:
	print(f)
	machobj=re.match(r'.+\.json',f)
	if machobj:
		continue
	artifact=re.match(r'.{2}AR.{2}\.txt',f)
	if artifact:
		entry=','.join((f,'artifact\n'))
		catmap=''.join((catmap,entry))
	astronomy=re.match(r'.{2}AS.{2}\.txt',f)
	if astronomy:
		entry=','.join((f,'astronomy\n'))
		catmap=''.join((catmap,entry))
	biography=re.match(r'.{2}BI.{2}\.txt',f)
	if biography:
		entry=','.join((f,'biography\n'))
		catmap=''.join((catmap,entry))
	biology=re.match(r'.{2}BL.{2}\.txt',f)
	if biology:
		entry=','.join((f,'biology\n'))
		catmap=''.join((catmap,entry))
	book=re.match(r'.{2}BO.{2}\.txt',f)
	if book:
		entry=','.join((f,'book\n'))
		catmap=''.join((catmap,entry))
	business=re.match(r'.{2}BU.{2}\.txt',f)
	if business:
		entry=','.join((f,'business\n'))
		catmap=''.join((catmap,entry))
	comics=re.match(r'.{2}CC.{2}\.txt',f)
	if comics:
		entry=','.join((f,'comics\n'))
		catmap=''.join((catmap,entry))
	chemistry=re.match(r'.{2}CH.{2}\.txt',f)
	if chemistry:
		entry=','.join((f,'chemistry\n'))
		catmap=''.join((catmap,entry))
	cinema=re.match(r'.{2}CI.{2}\.txt',f)
	if cinema:
		entry=','.join((f,'cinema\n'))
		catmap=''.join((catmap,entry))
	country=re.match(r'.{2}CO.{2}\.txt',f)
	if country:
		entry=','.join((f,'country\n'))
		catmap=''.join((catmap,entry))
	character=re.match(r'.{2}CR.{2}\.txt',f)
	if character:
		entry=','.join((f,'character\n'))
		catmap=''.join((catmap,entry))
	culture=re.match(r'.{2}CU.{2}\.txt',f)
	if culture:
		entry=','.join((f,'culture\n'))
		catmap=''.join((catmap,entry))
	drama=re.match(r'.{2}DR.{2}\.txt',f)
	if drama:
		entry=','.join((f,'drama\n'))
		catmap=''.join((catmap,entry))
	economy=re.match(r'.{2}EC.{2}\.txt',f)
	if economy:
		entry=','.join((f,'economy\n'))
		catmap=''.join((catmap,entry))
	environment=re.match(r'.{2}EN.{2}\.txt',f)
	if environment:
		entry=','.join((f,'environment\n'))
		catmap=''.join((catmap,entry))
	era=re.match(r'.{2}ER.{2}\.txt',f)
	if era:
		entry=','.join((f,'era\n'))
		catmap=''.join((catmap,entry))
	event=re.match(r'.{2}EV.{2}\.txt',f)
	if event:
		entry=','.join((f,'event\n'))
		catmap=''.join((catmap,entry))
	game=re.match(r'.{2}GA.{2}\.txt',f)
	if game:
		entry=','.join((f,'game\n'))
		catmap=''.join((catmap,entry))
	lore=re.match(r'.{2}LO.{2}\.txt',f)
	if lore:
		entry=','.join((f,'lore\n'))
		catmap=''.join((catmap,entry))
	mathematics=re.match(r'.{2}MA.{2}\.txt',f)
	if mathematics:
		entry=','.join((f,'mathematics\n'))
		catmap=''.join((catmap,entry))
	medicine=re.match(r'.{2}ME.{2}\.txt',f)
	if medicine:
		entry=','.join((f,'medicine\n'))
		catmap=''.join((catmap,entry))
	movement=re.match(r'.{2}MO.{2}\.txt',f)
	if movement:
		entry=','.join((f,'movement\n'))
		catmap=''.join((catmap,entry))
	music=re.match(r'.{2}MU.{2}\.txt',f)
	if music:
		entry=','.join((f,'music\n'))
		catmap=''.join((catmap,entry))
	nature=re.match(r'.{2}NA.{2}\.txt',f)
	if nature:
		entry=','.join((f,'nature\n'))
		catmap=''.join((catmap,entry))
	physics=re.match(r'.{2}PH.{2}\.txt',f)
	if physics:
		entry=','.join((f,'physics\n'))
		catmap=''.join((catmap,entry))
	place=re.match(r'.{2}PL.{2}\.txt',f)
	if place:
		entry=','.join((f,'place\n'))
		catmap=''.join((catmap,entry))
	politics=re.match(r'.{2}PO.{2}\.txt',f)
	if politics:
		entry=','.join((f,'politics\n'))
		catmap=''.join((catmap,entry))
	show=re.match(r'.{2}SH.{2}\.txt',f)
	if show:
		entry=','.join((f,'show\n'))
		catmap=''.join((catmap,entry))
	social=re.match(r'.{2}SO.{2}\.txt',f)
	if social:
		entry=','.join((f,'social_science\n'))
		catmap=''.join((catmap,entry))
	sport=re.match(r'.{2}SP.{2}\.txt',f)
	if sport:
		entry=','.join((f,'sport\n'))
		catmap=''.join((catmap,entry))
	technology=re.match(r'.{2}TE.{2}\.txt',f)
	if technology:
		entry=','.join((f,'technology\n'))
		catmap=''.join((catmap,entry))
	theology=re.match(r'.{2}TH.{2}\.txt',f)
	if theology:
		entry=','.join((f,'theology\n'))
		catmap=''.join((catmap,entry))
	team=re.match(r'.{2}TM.{2}\.txt',f)
	if team:
		entry=','.join((f,'team\n'))
		catmap=''.join((catmap,entry))
	nation=re.match(r'.{2}NT.{2}\.txt',f)
	if nation:
		entry=','.join((f,'nation\n'))
		catmap=''.join((catmap,entry))
print(catmap)
jsonfile=io.open('lab_map.csv','a+',encoding='utf8')
jsonfile.write(catmap)
jsonfile.close()

catmap='ARAR00.txt,art,artifact\n'
for f in os.listdir(root)[2:]:
	print(f)
	machobj=re.match(r'.+\.json',f)
	if machobj:
		continue
	art=re.match(r'AR.{4}\.txt',f)
	if art:
		entry=','.join((f,'art'))
		catmap=''.join((catmap,entry))
		artifact=re.match(r'.{2}AR.{2}\.txt',f)
		if artifact:
			entry='artifact\n'
			catmap=','.join((catmap,entry))
		book=re.match(r'.{2}BO.{2}\.txt',f)
		if book:
			entry='book\n'
			catmap=','.join((catmap,entry))
		show=re.match(r'.{2}SH.{2}\.txt',f)
		if show:
			entry='show\n'
			catmap=','.join((catmap,entry))
		place=re.match(r'.{2}PL.{2}\.txt',f)
		if place:
			entry='place\n'
			catmap=','.join((catmap,entry))
		movement=re.match(r'.{2}MO.{2}\.txt',f)
		if movement:
			entry='movement\n'
			catmap=','.join((catmap,entry))
		music=re.match(r'.{2}MU.{2}\.txt',f)
		if music:
			entry='music\n'
			catmap=','.join((catmap,entry))
		drama=re.match(r'.{2}DR.{2}\.txt',f)
		if drama:
			entry='drama\n'
			catmap=','.join((catmap,entry))
		cinema=re.match(r'.{2}CI.{2}\.txt',f)
		if cinema:
			entry='cinema\n'
			catmap=','.join((catmap,entry))
		comics=re.match(r'.{2}CC.{2}\.txt',f)
		if comics:
			entry='comics\n'
			catmap=','.join((catmap,entry))
		biography=re.match(r'.{2}BI.{2}\.txt',f)
		if biography:
			entry='biography\n'
			catmap=','.join((catmap,entry))
		character=re.match(r'.{2}CR.{2}\.txt',f)
		if character:
			entry='character\n'
			catmap=','.join((catmap,entry))
	geography=re.match(r'GE.{4}\.txt',f)
	if geography:
		entry=','.join((f,'geography'))
		catmap=''.join((catmap,entry))
		place=re.match(r'.{2}PL.{2}\.txt',f)
		if place:
			entry='place\n'
			catmap=','.join((catmap,entry))
		country=re.match(r'.{2}CO.{2}\.txt',f)
		if country:
			entry='country\n'
			catmap=','.join((catmap,entry))
		nation=re.match(r'.{2}NT.{2}\.txt',f)
		if nation:
			entry='nation\n'
			catmap=','.join((catmap,entry))
		biography=re.match(r'.{2}BI.{2}\.txt',f)
		if biography:
			entry='biography\n'
			catmap=','.join((catmap,entry))
	history=re.match(r'HI.{4}\.txt',f)
	if history:
		entry=','.join((f,'history'))
		catmap=''.join((catmap,entry))
		place=re.match(r'.{2}PL.{2}\.txt',f)
		if place:
			entry='place\n'
			catmap=','.join((catmap,entry))
		country=re.match(r'.{2}CO.{2}\.txt',f)
		if country:
			entry='country\n'
			catmap=','.join((catmap,entry))
		nation=re.match(r'.{2}NT.{2}\.txt',f)
		if nation:
			entry='nation\n'
			catmap=','.join((catmap,entry))
		artifact=re.match(r'.{2}AR.{2}\.txt',f)
		if artifact:
			entry='artifact\n'
			catmap=','.join((catmap,entry))
		biography=re.match(r'.{2}BI.{2}\.txt',f)
		if biography:
			entry='biography\n'
			catmap=','.join((catmap,entry))
		era=re.match(r'.{2}ER.{2}\.txt',f)
		if era:
			entry='era\n'
			catmap=','.join((catmap,entry))
		event=re.match(r'.{2}EV.{2}\.txt',f)
		if event:
			entry='event\n'
			catmap=','.join((catmap,entry))
		culture=re.match(r'.{2}CU.{2}\.txt',f)
		if culture:
			entry='culture\n'
			catmap=','.join((catmap,entry))
	religion=re.match(r'RE.{4}\.txt',f)
	if religion:
		entry=','.join((f,'religion'))
		catmap=''.join((catmap,entry))
		biography=re.match(r'.{2}BI.{2}\.txt',f)
		if biography:
			entry='biography\n'
			catmap=','.join((catmap,entry))
		theology=re.match(r'.{2}TH.{2}\.txt',f)
		if theology:
			entry='theology\n'
			catmap=','.join((catmap,entry))
		lore=re.match(r'.{2}LO.{2}\.txt',f)
		if lore:
			entry='lore\n'
			catmap=','.join((catmap,entry))
	science=re.match(r'SC.{4}\.txt',f)
	if science:
		entry=','.join((f,'science'))
		catmap=''.join((catmap,entry))
		biography=re.match(r'.{2}BI.{2}\.txt',f)
		if biography:
			entry='biography\n'
			catmap=','.join((catmap,entry))
		technology=re.match(r'.{2}TE.{2}\.txt',f)
		if technology:
			entry='technology\n'
			catmap=','.join((catmap,entry))
		nature=re.match(r'.{2}NA.{2}\.txt',f)
		if nature:
			entry='nature\n'
			catmap=','.join((catmap,entry))
		physics=re.match(r'.{2}PH.{2}\.txt',f)
		if physics:
			entry='physics\n'
			catmap=','.join((catmap,entry))
		computer=re.match(r'.{2}CM.{2}\.txt',f)
		if computer:
			entry='computer\n'
			catmap=','.join((catmap,entry))
		mathematics=re.match(r'.{2}MA.{2}\.txt',f)
		if mathematics:
			entry='mathematics\n'
			catmap=','.join((catmap,entry))
		medicine=re.match(r'.{2}ME.{2}\.txt',f)
		if medicine:
			entry='medicine\n'
			catmap=','.join((catmap,entry))
		economy=re.match(r'.{2}EC.{2}\.txt',f)
		if economy:
			entry='economy\n'
			catmap=','.join((catmap,entry))
		environment=re.match(r'.{2}EN.{2}\.txt',f)
		if environment:
			entry='environment\n'
			catmap=','.join((catmap,entry))
		astronomy=re.match(r'.{2}AS.{2}\.txt',f)
		if astronomy:
			entry='astronomy\n'
			catmap=','.join((catmap,entry))
		biology=re.match(r'.{2}BL.{2}\.txt',f)
		if biology:
			entry='biology\n'
			catmap=','.join((catmap,entry))
		chemistry=re.match(r'.{2}CH.{2}\.txt',f)
		if chemistry:
			entry='chemistry\n'
			catmap=','.join((catmap,entry))
	society=re.match(r'SO.{4}\.txt',f)
	if society:
		entry=','.join((f,'society'))
		catmap=''.join((catmap,entry))
		social=re.match(r'.{2}SO.{2}\.txt',f)
		if social:
			entry='social_science\n'
			catmap=','.join((catmap,entry))
		politics=re.match(r'.{2}PO.{2}\.txt',f)
		if politics:
			entry='politics\n'
			catmap=','.join((catmap,entry))
		game=re.match(r'.{2}GA.{2}\.txt',f)
		if game:
			entry='game\n'
			catmap=','.join((catmap,entry))
		culture=re.match(r'.{2}CU.{2}\.txt',f)
		if culture:
			entry='culture\n'
			catmap=','.join((catmap,entry))
		artifact=re.match(r'.{2}AR.{2}\.txt',f)
		if artifact:
			entry='artifact\n'
			catmap=','.join((catmap,entry))
		business=re.match(r'.{2}BU.{2}\.txt',f)
		if business:
			entry='business\n'
			catmap=','.join((catmap,entry))
	sports=re.match(r'SP.{4}\.txt',f)
	if sports:
		entry=','.join((f,'sports'))
		catmap=''.join((catmap,entry))
		biography=re.match(r'.{2}BI.{2}\.txt',f)
		if biography:
			entry='biography\n'
			catmap=','.join((catmap,entry))
		team=re.match(r'.{2}TM.{2}\.txt',f)
		if team:
			entry='team\n'
			catmap=','.join((catmap,entry))
		sport=re.match(r'.{2}SP.{2}\.txt',f)
		if sport:
			entry='sport\n'
			catmap=','.join((catmap,entry))
		competition=re.match(r'.{2}CP.{2}\.txt',f)
		if competition:
			entry='competition\n'
			catmap=','.join((catmap,entry))
print(catmap)
jsonfile=io.open('map.csv','a+',encoding='utf8')
jsonfile.write(catmap)
jsonfile.close()	