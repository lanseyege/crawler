#encoding=utf-8
import urllib
import urllib.request
import socket
import re
import time
import sys
import json

u1 = 'http://ieeexplore.ieee.org/document/'
u2 = 'http://ieeexplore.ieee.org'

reg = r'global.document.metadata=(.+?);\n'
glb = re.compile(reg)

socket.setdefaulttimeout(30)

def getHtml(url):
    try:
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
    except:
        print ('wrong with url: ' + url)
        html = ''
    return html

def getH(line, num):
    fileh = 'html/'+num
    fh = open(fileh, 'w')
    B = {}
    B['id'] = num
    B['url'] = line
    html = getHtml(u1+num+'/')
    fh.write(html)
    fh.flush()
    fh.close()
    if html == '':
        print ('html none')
        return B
    glb_ = re.findall(glb, html)
    #print (glb_)
    if len(glb_) < 1:
        print ('reg none')
        return B
    try:
        js = dict(json.loads(glb_[0]))
    except:
        return B
    print (type(js))
    if 'pdfPath' in js:
        #print (js['pdfPath'])
        B['pdfPath'] = u2+js['pdfPath']
    if 'title' in js:
        B['title'] = js['title']
    if 'keywords' not in js:
        print ('keywords none')
        return B
    for a in js['keywords']:
        if 'type' not in a:
            continue
        if a['type'].strip() == 'IEEE Keywords':
            B['IEEE Keywords'] = a['kwd']
        elif a['type'].strip() == 'Author Keywords':
            B['Author Keywords'] = a['kwd']
    return B

path = '/home/renyafeng/code/crawl/ieee/pdf_1/'
file1 = 'pieee_urls_p5'
f1 = open(file1)
file2 = 'metadata10.json'
f2 = open(file2, 'w')

for line in f1:
    i = 0
    num = line.strip().split('=')[-1]
    if num == '':
        continue
    if i == 1:
        continue
    B = getH(line.strip(), num)
    json.dump(B, f2)
    #f2.write(B)
    f2.write('\n')
    f2.flush()
    time.sleep(0.5)
f1.close()
f2.close()
