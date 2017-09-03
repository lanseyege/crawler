#coding:utf-8
from bs4 import BeautifulSoup
import urllib2
import mechanize

html = 'http://www.qiushibaike.com/text/'

br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)

br.open(html)
content = br.response().read()

soup = BeautifulSoup(content, 'html.parser')

mya = soup.findAll('div', {'class':'article block untagged mb15'})
for mya_ in mya:
    myb = mya_.find('a', {'class':'contentHerf'})
    myd = myb.find('div', {'class':'content'})
    a = myd.find('span')
    print a.text
    mycom = mya_.find('div', {'class':'stats'})
    mycom_ = mycom.find('i', {'class':'number'})
    print mycom_.text
    mynum = mya_.find('a', {'class':'qiushi_comments'})
    mynum_ = mynum.find('i', {'class':'number'})
    print mynum_.text
#print soup.find_all([])

