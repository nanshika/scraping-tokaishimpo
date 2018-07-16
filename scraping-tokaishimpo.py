#!/usr/bin/env python
# -*- coding: utf-8 -*-
# scraping-tokaishimpo.py
import requests, urllib, hashlib, os, time, datetime, re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def fix_filePath(tarStr):
     return re.sub(r'[\\|/|:|?|.|"|<|>|\|]', '', tarStr) # "

def tempScraping(first_link):
    first_link = "https://tohkaishimpo.com/yomaigoto/"
    modDate = datetime.date.today().strftime("%Y%m%d")
    outDir = os.environ['GOOGLE_DRIVE_PATH'] + "/memo/tokaishimpo/"
    f = open( outDir + modDate + "_Tokaishimpo.txt", 'w',encoding = 'utf-8_sig')
    first_res  = requests.get(first_link)
    first_soup = BeautifulSoup(first_res.content,'lxml')
    body = first_soup.find("div","postText_noimage").text
    f.writelines(''.join(map(str,body)).replace(u'\n','').replace(u'\u3000','')+"\n\n")
    f.close
    print(body)

tempScraping("https://tohkaishimpo.com/yomaigoto/")

print("___Finished!___")
time.sleep(10)
