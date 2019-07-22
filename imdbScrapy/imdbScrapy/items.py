# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    year = scrapy.Field()
    rating = scrapy.Field()
    href_link = scrapy.Field()
    title = scrapy.Field()
    
