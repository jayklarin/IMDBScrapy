# -*- coding: utf-8 -*-
import scrapy
from ..items import ImdbscrapyItem

class ImdbpopulartvSpider(scrapy.Spider):
    name = 'imdbPopularTV'
    allowed_domains = ['imdb']
    start_urls = ['https://www.imdb.com/chart/tvmeter?ref_=nv_tvv_mptv']

    def parse(self, response):
        imdbLister = response.css('.lister-list tr')
        for il in imdbLister:
            imdbHref = il.css('.titleColumn a::attr("href")').extract_first()
            imdbYear = il.css('.secondaryInfo::text').extract_first()
            imdbRating = il.css('.imdbRating strong::text').extract_first()
            imdbRank = il.css('.velocity::text').extract_first()
            imdbTitle = il.css('.titleColumn a::text').extract_first()
            #imdbRankChange = il.css('.velocity .secondaryInfo::text')[1].extract()
            
            item = ImdbscrapyItem()

            item['href_link'] = imdbHref
            item['year'] = imdbYear
            item['rating'] = imdbRating
            item['title'] = imdbTitle
            yield item

        

