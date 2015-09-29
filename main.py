#!/usr/bin/python3
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs4

base_url = 'http://amp.dascene.net/'
data = urlopen('http://amp.dascene.net/detail.php?detail=modules&view=7588') # timer amiga MODs
soup = bs4(data)
top = soup.find_all('div',{'id':'result'})[1]
mid = top.find_all('a',{'target':'_new'})
#for link in mid:
#    print(link.get('href'))
links = [base_url+link.get('href') for link in mid]

f = open('links.txt','w')
for link in links:
    f.write(link+'\n')
    print('Link:'+link+' written.')
f.close()
