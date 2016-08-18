
import urllib.request
import urllib
import socket
import re

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read().decode('utf-8')
    return html

def getPdf(html, path):
    reg=r'<a href="(.+?)"><img alt="Pdf" height="16" src=".+?" title="Open PDF of \&\#39;(.+?)\&\#39;" width="16" /></a>'
    pdff=re.compile(reg)
    pdflist=re.findall(pdff,html)
    socket.setdefaulttimeout(30)
    for pdf in pdflist:
        print (pdf)
        #print (pdf[0])
        #print (pdf[1])
        title = pdf[1].replace(':', ' ')
        title = title.replace('-', ' ')
        title = title.replace('?', ' ')
        title = title.replace('!', ' ')
        title = title.replace('.', ' ')
        title = title.replace('%', ' ')
        title = title.replace('\\', ' ')
        title = title.replace('"', ' ')
        title = title.replace('/', ' ')
        title = path + title
        try:
            urllib.request.urlretrieve(pdf[0], '%s.pdf' % title)
            print ('......download ' + title)
        except urllib.error.URLError as e:
            print ('......down url error...')
        except urllib.error.HTTPError as e:
            print ('......down http error...')
        except socket.timeout as e:
            print ('......time out...')
url='http://aclanthology.info/events/emnlp-2015'
path='F:\\学习\\科研\\NLP\\EMNLP\\2015\\'
html=getHtml(url)
getPdf(html, path)
