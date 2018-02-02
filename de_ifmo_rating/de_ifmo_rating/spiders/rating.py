# -*- coding: utf-8 -*-
import scrapy
from de_ifmo_rating.items import DeIfmoRatingItem


class RatingSpider(scrapy.Spider):
    name = 'rating'
    allowed_domains = ['de.ifmo.ru']
    start_urls = ['https://de.ifmo.ru/?node=rating']

    def parse(self, response):
        for href in response.css('.big-links a::attr(href)')[:1]:
            yield response.follow(href, self.parse_list)

    def parse_list(self, response):
        for row in response.css('.table-rating tr')[1:]:
            item = DeIfmoRatingItem()
            item['rank'] = row.css('td::text')[0].extract()
            item['name'] = row.css('td::text')[1].extract()
            item['department'] = row.css('td::text')[3].extract()
            yield item