# -*- coding: utf-8 -*-
"""WikiProjScrapingCode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SNpBNBFfrzODLyLD5e79ZqfHn0MmI_ea
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://en.m.wikipedia.org/wiki/Wikipedia:WikiProject_Deletion_sorting/Academics_and_educators/archive_2"
# makes a request to the web page and gets its HTML
r = requests.get(url)
# stores the HTML page in 'soup', a BeautifulSoup object
soup = BeautifulSoup(r.content)

import numpy as np
alllinks=[]
alltitles=[]
for link in soup.find_all('a'):
  links= (link.get('href'))
  alllinks.append(str(links))
  titles= (link.get('title'))
  alltitles.append(str(titles))
wiki_combo=np.array([alltitles,alllinks])
wiki_combo=wiki_combo.T
wiki_combo=np.delete(wiki_combo,slice(0,18),0)

print(wiki_combo)
with open('/content/drive/My Drive/Wiki/wikicombo.csv', 'w') as csvfile:
  writer = csv.writer(csvfile,delimiter='/')
  writer.writerows(wiki_combo)

names = []
for x in alltitles:
  if 'Wikipedia:Articles for deletion/' in x:
    #print(x)
    name = x[32:]
    names.append(name)
  else:
    names.append(x)
names = np.array(names)
#names = names.T
#names = np.delete(names,slice(0,18),0)

wiki_combo=np.array([names,alltitles,alllinks])
wiki_combo=wiki_combo.T
wiki_combo=np.delete(wiki_combo,slice(0,18),0)



with open('/content/drive/My Drive/Wiki/wikicombo.csv', 'w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(wiki_combo)

print(wiki_combo)
print(len(wiki_combo))
