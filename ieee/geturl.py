#encoding=utf-8
import urllib
import urllib.request
import socket
import re
import time
import sys
import json

u1 = 'http://ieeexplore.ieee.org/document/'

#reg = r'global.document.metadata=(.+?);\n'
reg = r'<frame src="(.+?)" frameborder=0 />'
glb = re.compile(reg)

def getHtml(url):
    try:
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
    except:
        print ('wrong with url: ' + url)
        html = ''
    return html

def getH(url):
    B = {}
    html = getHtml(url)
    print (html)
    if html == '':
        return ''
    glb_ = re.findall(glb, html)
    print (glb_)
    if len(glb_) < 1:
        return ''
    return glb_

path = '/home/renyafeng/code/crawl/ieee/pdf_1/'
file1 = 'pieee_urls'
f1 = open(file1)
file2 = 'metadata.json'
f2 = open(file2, 'w')

for line in f1:
    i = 0
    B = getH(line)
    #json.dump(B, f2)
    #f2.write(B)
    #f2.write('\n')
    time.sleep(0.5)
f1.close()
f2.close()
