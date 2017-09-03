#coding:utf-8
from bs4 import BeautifulSoup
import urllib2
import mechanize
import time

url = 'http://www.qiushibaike.com/text/'
urls = []
urls.append(url)
for i in range(34):
    urls.append(url + 'page/'+str(i+2)+'/?s=4959240')

br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)

fw = open('qiubai.humor.'+str(int(time.time())), 'w')

for i in range(len(urls)):
    br.open(urls[i])
    content = br.response().read()
    soup = BeautifulSoup(content, 'html.parser')

    mya = soup.findAll('div', {'class':'article block untagged mb15'})
    for mya_ in mya:
        myb = mya_.find('a', {'class':'contentHerf'})
        myd = myb.find('div', {'class':'content'})
        a = myd.find('span').text
        try:
            mycom = mya_.find('div', {'class':'stats'})    
            mycom_ = mycom.find('i', {'class':'number'}).text
        except:
            mycom_ = 0
        try:
            mynum = mya_.find('a', {'class':'qiushi_comments'})
            mynum_ = mynum.find('i', {'class':'number'}).text
        except:
            mynum_ = 0
        myid = mya_.get('id')
        s = a.encode('utf-8') + '\t' + str(mycom_) + '\t' + str(mynum_) + '\t' + str(myid) + '\n'
        '''
        print a
        print mycom_
        print mynum_
        print s
        '''
        fw.write(s)

fw.close()

