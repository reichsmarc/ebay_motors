# scrapes completed listings for major automakers

import scrapy


class EbaySpider(scrapy.Spider):
    name = 'ebay_motors3'

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 8,
        "HTTPCACHE_ENABLED": True
    }

# completed sales, no zip code specified
    start_urls = [
    'https://www.ebay.com/sch/Acura/5330/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Alfa-Romeo/5340/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Aston-Martin/157054/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Audi/6002/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Bentley/157059/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/BMW/6006/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Buick/6135/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Cadillac/5347/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Chevrolet/5346/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Chrysler/5351/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Dodge/6191/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Fiat/175886/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Ford/6010/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/GMC/6243/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Honda/6252/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Hummer/5342/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Hyundai/6261/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Infiniti/6263/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Jaguar/6272/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Jeep/6279/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Kia/6287/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Land-Rover/6293/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Lexus/6297/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Lincoln/6302/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Lotus/116480/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Maserati/162313/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Mazda/6310/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Mercedes-Benz/6311/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Mercury/5363/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Mini/31860/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Mitsubishi/6348/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Nissan/6371/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Oldsmobile/6372/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Plymouth/6376/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Pontiac/6377/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Porsche/6013/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Ram/171998/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Rolls-Royce/157071/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Saab/6380/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Saturn/6381/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Scion/116483/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Smart/157077/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Subaru/6452/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Tesla/180041/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Toyota/6016/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Volkswagen/6018/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2',
    'https://www.ebay.com/sch/Volvo/6454/i.html?_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25&LH_PrefLoc=2'
    ]


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

        winningbid = response.xpath('//div[@class="u-flL w29 vi-price-np"]/span[@id]/text()').extract()
        buy_it_now_price = [bin.strip() for bin in response.xpath('//div[@class="u-flL w29 vi-price"]/span[@id]/text()').extract()]

        num_bids = response.xpath('//a[@class="vi-bidC"]/span/text()').extract_first()

        url = response.request.meta['url']

        catsvals = [catval.strip() for catval in response.xpath('//div[@class="section"]//tr//text()').extract()]

        yield {
            'title': title,
            'subtitle' : subtitle,
            'winningbid' : winningbid,
            'buy_it_now_price':buy_it_now_price,
            'num_bids' : num_bids,
            'url': url,
            'catsvals': catsvals
        }

    











