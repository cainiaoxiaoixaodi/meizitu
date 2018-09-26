# -*- coding: utf-8 -*-
from pprint import pprint

import scrapy


class MzSpider(scrapy.Spider):
    name = 'mz'
    allowed_domains = ['meizitu.com']
    start_urls = ['http://www.meizitu.com/a/more_1.html']

    def parse(self, response):
        data = response.text
        item = {}
        item['data'] = data
        return item
