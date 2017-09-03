#encoding=utf-8
import urllib
import urllib.request
import socket
import re
import time
import sys
import json

u1 = 'http://ieeexplore.ieee.org/document/'

reg = r'global.document.metadata=(.+?);\n'
glb = re.compile(reg)

def getHtml(url):
    try:
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
    except:
        print ('wrong with url: ' + url)
        html = ''
    return html

def getH(url, num):
    B = {}
    B['id'] = num
    html = getHtml(url+num+'/')
    if html == '':
        return B
    glb_ = re.findall(glb, html)
    if len(glb_) < 1:
        return B
    js = dict(json.loads(glb_[0]))
    print (type(js))
    if 'Keywords' not in js:
        return B
    for a in js['Keywords']:
        if a['type'].strip() == 'IEEE Keywords':
            B['IEEE Keywords'] = a['kwd']
        elif a['type'].strip() == 'Author Keywords':
            B['Author Keywords'] = a['kwd']
    return B

path = '/home/renyafeng/code/crawl/ieee/pdf_1/'
file1 = 'pieee_urls'
f1 = open(file1)
file2 = 'metadata.json'
f2 = open(file2, 'w')

for line in f1:
    i = 0
    num = line.strip().split('=')[-1]
    path1 = path + num
    #urllib.request.urlretrieve(line, '%s.pdf' % num)
    try:
        urllib.request.urlretrieve(line, '%s.pdf' % path1)
    except:
        i = 1
        print ('donwload error')
    time.sleep(0.5)
    if i == 1:
        continue
    B = getH(u1 , num)
    json.dump(B, f2)
    #f2.write(B)
    #f2.write('\n')
    time.sleep(0.5)
f1.close()
f2.close()
