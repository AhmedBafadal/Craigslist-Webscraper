# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['london.craigslist.org']
    start_urls = ['https://london.craigslist.co.uk/search/edu/']

    def parse(self, response):
        listings = response.xpath(
            '//li[@class="result-row"]')
        for listing in listings:
            # Extracting the date
            date = listing.xpath(
                './/*[@class="result-date"]/@datetime').extract_first()
            # Extracting the link from each posting
            link = listing.xpath(
                './/a[@class="result-title hdrlnk"]/@href').extract_first()

            # Extracting the title from each posting
            text = listing.xpath(
                './/a[@class="result-title hdrlnk"]/text()').extract_first()

            yield {'date': date,
                   'link': link,
                   'text': text,
                   }
        next_page_url = response.xpath(
            '//a[text()="next > "]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
