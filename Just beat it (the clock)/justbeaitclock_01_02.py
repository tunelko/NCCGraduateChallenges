#!/usr/bin/env python
import requests
import string
import base64
import string
import re
from bs4 import BeautifulSoup as BS

url ='http://web1.ncc.ninja/43dfef686083239/'

def extract_http(url):
  r = requests.get(url)
  html = BS(r.text)
  data = (html.find_all('strong'))
  datalist = []
  for datas in data:
    datalist.append(str(datas))
    a=datalist[0].replace('<strong>Challenge String: ','')
    b=a.replace('</strong>','')
  return b 
  
  
def b64(text):
    print 'Base64: ', text 
    return base64.b64decode(text) 

def rev(text):
    print 'Reverse: ', text 
    return text[::-1]
  
def swap(text):
    print 'Swap: ', text 
    return ''.join([c[1] + c[0] for c in zip(text[::2], text[1::2])])
  
def solve(text):
  a = b64(text)
  b = rev(a)
  c = swap(b)
  data={'answer':c}
  r = requests.post(url, data)
  output = BS(r.text)
  flag = output.find_all("div", { "class" : "alert alert-dismissible alert-success closable" })
  return flag 
  
flag = str(solve(extract_http(url)))
print flag
