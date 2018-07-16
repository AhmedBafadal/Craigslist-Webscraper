# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['london.craigslist.org']
    start_urls = ['http://london.craigslist.org/']

    def parse(self, response):
        pass
