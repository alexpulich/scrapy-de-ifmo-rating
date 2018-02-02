# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DeIfmoRatingPipeline(object):
    def process_item(self, item, spider):
        item['group'], item['department'] = item['department'].split(', ')
        item['group'] = item['group'].replace('гр. ', '')
        item['department'] = item['department'].replace('каф. ', '')
        return item
