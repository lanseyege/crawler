import json
from scrapy.spider import Spider
from scrapy.http import Request
from urllib import urlencode

class ieees(Spider):
    name = 'ieee'
    start_urls = ''
    
    def parse(self, response):
        return self.get_lineup('vulnerability')
    
    def get_lineup(self, pm):
        params = {
            'reload' : true
            'newsearch':true
            'queryText':pm
        }
        return Request(
            url='http://ieeexplore.ieee.org/search/searchresult.jsp?'+urlencode(params),
            dont_filter=True,
            callback=self.parse_lineup
        )

    def parse_lineaup(self, response):
        data = json.loads(response,body)
        print data
