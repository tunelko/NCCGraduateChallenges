#!/usr/bin/env python
import requests
import binascii, hashlib
import string
import itertools
from bs4 import BeautifulSoup as BS
import timeit
from datetime import datetime
current_time = lambda: str(datetime.now()).split(' ')[1].split('.')[0]
start = timeit.default_timer()

url='http://web1.ncc.ninja/a37bd1eea839e86/'
letters = string.ascii_lowercase
digits = string.digits
suffix='NCCGRADCHALLENGE'
charlist = letters+digits
dic = []

r = requests.get(url)
html = BS(r.text)
data = (html.find_all('strong'))
datalist = []
for datas in data:
    datalist.append(str(datas))

def setHash(hastype,hashstring):
    if hashtype == 'md5':
        return hashlib.md5(str(hashstring))

    elif hashtype == 'sha1':
        return hashlib.sha1(str(hashstring))

    elif hashtype == 'ntlm':
        return binascii.hexlify(hashlib.new('md4', hashstring.encode('utf-16le')).digest())
        
    else:
	return ''

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))


for current in xrange(4):
    a = [i for i in charlist]
    for y in xrange(current):
        a = [x+i for i in charlist for x in a]
    dic = dic+a


hashtype = datalist[3].replace('<strong>','')
hashtype = hashtype.replace('</strong>','')
hashtype = hashtype.lower() 

hashstring = datalist[0].replace('<strong>Hash:','')
hashstring = hashstring.replace('</strong>','')
hashstring = hashstring.replace(' ','')

solution = ''

for prefix in dic:
    tried = prefix + suffix
    obj = setHash(hashtype.lower(), tried)
    if hashtype == 'ntlm':
        need = obj
    else:
        need = obj.hexdigest()

    print 'Trying' , hashtype, '(',hashstring,') ...' , tried , ' = ' , need 
    if need == hashstring:
         stop = timeit.default_timer()
         total_time = stop - start	
         solution = tried
         print current_time() , 'Solution is: ' , need , '-> ', tried
         print 'Cracked in: ', total_time
         break

data = {'answer': solution}
r = requests.post(url,data)
output = BS(r.text)
if total_time > 60:
    flag = ['NOT in time']
else:
    flag = output.find_all("div", { "class" : "alert alert-dismissible alert-success closable" })
print flag
