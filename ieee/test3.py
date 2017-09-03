import scrapy
from selenium import webdriver

class PaperSpider(scrapy.Spider):
    name = 'paper_spider'
    allowed_domains = ['http://ieeexplore.ieee.org/']
    start_urls = ['http://ieeexplore.ieee.org/search/searchresult.jsp?reload=true&newsearch=true&queryText=vulnerability']

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        data = self.driver.get(response.url)
        print 'hehe'
        print data
        while True:
            n = self.driver.find_element_by_xpath('//td[@class="pdfUrl"]/a')
            
            print n
        
        self.driver.close()

