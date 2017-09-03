#encoding=utf-8
import urllib2
from urllib2 import Request
import socket
import re
import time
import sys
import json
import cookielib
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler

reload(sys)
sys.setdefaultencoding('utf-8')

reg = r'<frame src="(.+?)" frameborder=0 />'
glb = re.compile(reg)

def getUrl(res):
    #print res
    glb_ = re.findall(glb, res)
    print glb_
    if len(glb_) < 1:
        return ''
    return glb_[0]

file1 = 'pieee_urls'
f1 = open(file1)
file2 = 'rurls_3'
f2 = open(file2, 'w')
for line in f1:
    i = 0
    num = line.strip().split('=')[-1]
    #path1 = path + num
    try:
        cj = cookielib.CookieJar()
        opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())
        req = Request(line)
        f = opener.open(req)
        res = opener.open(line)
        rhtml = res.read()
        url_ = getUrl(rhtml)
    except:
        f2.write(num +'\n')
        time.sleep(30)
        continue
    f2.write(num+' '+url_+'\n')
    time.sleep(30)
f1.close()
f2.close()
