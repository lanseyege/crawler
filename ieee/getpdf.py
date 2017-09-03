#encoding=utf-8
import urllib2
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import socket
import re
import time
import sys
import json
import cookielib
import os

reload(sys)
sys.setdefaultencoding('utf-8')

uall = 'http://ieeexplore.ieee.org/'
pth = 'pdf_6/'
data = []
fi_loss = 'file_loss'
fi = open(fi_loss, 'w')
reg = r'<frame src="(.+?)" frameborder=0 />'
glb = re.compile(reg)

def get_json(file1):
    with open(file1) as f:
        for line in f:
            data.append(json.loads(line))

def get_url(url):
    glb_ = re.findall(glb, url)
    if len(glb_) < 1:
        return ''
    return glb_[0]

def get_pdf2(url, id):
    
    try:
        cj = cookielib.CookieJar()
        opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())
        req = Request(url)
        f = opener.open(req)
        res = opener.open(url)
        html = get_url(res.read())
        print id+' '+html
        if html == '':
            return
        fi.write(id+' '+html+'\n')
    except:
        return

def get_pdf():
    for d in data:
        id = ''
        if not d.has_key('id'):
            continue
        id = d['id']
        #if id not in A:
        #    continue
        if not d.has_key('pdfPath'):
            if not d.has_key('url'):
                continue
            #get_pdf2(d['url'], id)
            continue
        url = d['pdfPath']
        url = url.split('/')
        fg  = url[3]
        a = uall + fg[0:3]+'x'+fg[3:4]+'/' + url[-4] + '/' + url[-3] + '/0' + id + '.pdf'
        print a
        try:
            cj = cookielib.CookieJar()
            opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())
            req = Request(a)
            f = opener.open(req)
            ff = opener.open(a)
            pdf = ff.read()
            file2 = open(pth + id+'.pdf', 'w')
            file2.write(pdf)
            file2.close()
        except:
            print 'wrong'
        time.sleep(30)
def get_un(dirs):
    di = os.listdir(dirs)
    A = [d[:-4] for d in di]
    return A
#dirs_ = 'pdf_4/'
#A = get_un(dirs_)
#print A
#exit()
file1 = 'metadata_7.json'
get_json(file1)
get_pdf()
fi.close()
