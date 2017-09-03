#encoding=utf8
import urllib2
from urllib2 import Request
import socket
import re
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

u1 = 'http://ieeexplore.ieee.org/mobile/MobileSearch.jsp?queryText=vulnerability' 
u2 = 'rowsPerPage=10'
u3 = 'newsearch=true'
u4 = 'pageNumber='
ur = 'http://ieeexplore.ieee.org'

reg = r'<a href="(.+?)">PDF</a>'
href = re.compile(reg)

file1 = 'pieee_urls_2'
f1 = open(file1, 'w')

def getHtml(url):
    try:
        req = Request(url)
        page = urllib2.urlopen(req)
        #page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
    except:
        print 'wrong with url: ' + url
        html = ''
        
    return html

def getH(url):
    html = getHtml(url)
    if html == '':
        return
    href_l = re.findall(href, html)
    socket.setdefaulttimeout(30)
    f1.write('\n'.join(ur+l for l in href_l)+'\n')

def getHtmls():
    i = 0
    while i < 1000:
        if i == 0:
            url = u1 + '&' + u2 + '&' + u3
        else:
            url = u1 + '&' + u2 + '&' + u3 + '&' + u4 + str(i+1)
        getH(url)
        i += 1
        time.sleep(1)
        if i % 20 == 0:
            print i

getHtmls()
f1.close()
