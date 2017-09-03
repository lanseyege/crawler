#encoding=utf-8
import urllib2
from urllib2 import Request
import socket
import re
import time
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')

u1 = 'http://ieeexplore.ieee.org/document/7371485'

reg = r'global.document.metadata=(.+?);\n'
glb = re.compile(reg)

def getHtml(url):
    try:
        req = Request(url)
        page = urllib2.urlopen(req)
        html = page.read().decode('utf-8')
    except:
        print 'wrong with url: ' + url
        html = ''
    return html

def getH(url):
    html = getHtml(url)
    if html == '':
        return
    glb_ = re.findall(glb, html)
    #print glb_
    #print 'type of : ' + str(type(glb_))
    print len(glb_)
    print type(glb_[0])
    if len(glb_) < 1:
        print 're null'
        return
    js = json.loads(glb_[0])
    print type(js)
    A = js['keywords']
    print len(A)
    for a in A:
        if a['type'].strip() == 'IEEE Keywords':
            print a['kwd']
        elif a['type'].strip() == 'Author Keywords':
            print a['kwd']
    #print js['keywords']

getH(u1)
