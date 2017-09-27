# scrapes active 'Buy it Now' listings

import scrapy


class EbaySpider(scrapy.Spider):
    name = 'ebay_motors'

    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        "CONCURENT_REQUESTS_PER_DOMAIN": 3,
        "HTTPCACHE_ENABLED": True
    }

# Used cars, 'Buy it Now', no zip code specified

# Need to use Selenium to select max per page results
    start_urls = ['https://www.ebay.com/sch/Cars-Trucks/6001/i.html?LH_ItemCondition=2%7C0&rt=nc&LH_BIN=1']


    def parse(self, response):
        # Extract links to each car listing
        for href in response.xpath(
                '//h3[@class="lvtitle"]/a/@href'
        ).extract():
            # For each car link, call 'parse_car' (defined later)
            yield scrapy.Request(
                url=href,
                callback=self.parse_car,
                meta={'url': href}
            )
        # Follow pagination links and repeat
        next_url = response.xpath(
            '//td[@class="pagn-next"]/a/@href'
        ).extract()[0]

        yield scrapy.Request(
            url=next_url,
            callback=self.parse
        )

    def parse_car(self, response):

        title = response.xpath('//h1/text()').extract()

        subtitle = [subtl.strip() for subtl in response.xpath('//h2[@class="it-sttl"]/text()').extract()]

        price_list = response.xpath('//div[@class="u-flL w29 vi-price"]/span[@id]/text()').extract()

        num_bids = response.xpath('//a[@class="vi-bidC"]/span/text()').extract_first()

        url = response.request.meta['url']

        cats = [cat.strip() for cat in response.xpath('//td[@class="attrLabels"]/text()').extract()]

        vals = [val.strip() for val in response.xpath('//td[@class="attrLabels"]/following-sibling::td/descendant::*/text()').extract()]

        yield {
            'title': title,
            'subtitle' : subtitle,
            'price_list' : price_list,
            'num_bids' : num_bids,
            'url': url,
            'cats': cats,
            'vals': vals
        }

    











