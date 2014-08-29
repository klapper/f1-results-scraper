import scrapy
import time
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor

import datetime
import calendar

from f1results.items import F1ResultsItem

class f1Spider(CrawlSpider):
    name = "f1"
    allowed_domains = ["formula1.com"]


    start_urls = []

    for i in range(1950,2020):
        start_urls.append("http://www.formula1.com/results/driver/%s" % (i))

    download_delay = 3

    rules = (
        Rule(LinkExtractor(allow=('http://www.formula1.com/results/driver/\d{4}/\d+\.html')),callback='parse_item'),
        )

    def parse_item(self, response):
        rows = response.xpath('//table[@class="raceResults"]/tr')
        items = []
        for index,row in enumerate(rows):
            item = F1ResultsItem()
            try:
                item['driver_name'] = response.xpath('//div[@class="tertiaryNavItem"]/ul/li[2]/span/a/text()').extract()[0].strip()
                item['location'] = row.xpath('td[1]/a/text()').extract()[0]
                item['date'] = calendar.timegm(datetime.datetime.strptime(row.xpath('td[2]/text()').extract()[0],'%d %b %Y').utctimetuple())
                item['team'] = row.xpath('td[3]/a/text()').extract()[0]
                item['grid'] = row.xpath('td[4]/text()').extract()[0]
                item['position'] = row.xpath('td[5]/text()').extract()[0]
                item['points'] = row.xpath('td[6]/text()').extract()[0]
            except (ValueError,IndexError) ,e:
                pass
            
            if (('driver_name' in item) and ('location' in item) and ('date' in item) and ('team' in item) and ('grid' in item) and ('position' in item) and ('points' in item)):
                print item	
                items.append(item)
        return items

