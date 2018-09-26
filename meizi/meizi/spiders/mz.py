# -*- coding: utf-8 -*-
import scrapy


class MzSpider(scrapy.Spider):
    name = 'mz'
    allowed_domains = ['meizitu.com']
    start_urls = ['http://www.meizitu.com/a/more_1.html/']

    def parse(self, response):
        pass
