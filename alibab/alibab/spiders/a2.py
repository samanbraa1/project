import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import logging

class A2Spider(scrapy.Spider):
    name = 'a2'
    allowed_domains = ['alibaba.com']
    start_urls = ['https://www.alibaba.com/Electrical-Equipment-Supplies_p5?spm=a2700.8293689.scGlobalHomeHeader.184.500267afbZoLEo']
    
    
    def parse(self, response):
         pro=response.css('div.menuItemDiv')

         for link in pro:
            link1 = link.css('a::attr(href)').get()
        
            yield response.follow(url=link1,callback=self.parse_cat)
                    
              
   

         
    def parse_cat(self, response):
        
          product=response.css('div.tpl-wrapper')
          for p in product:
             yield{
              'name':p.css('div::attr(title)').get(),
               'img':p.css('img::attr(src)').get(),
               'price':p.xpath('//div[@class="flexColFloor flex5ColFloor"]/div/div/div/div[2]/div[2]/span/text()').get()

              }
          p2=response.css('div.nav')
          for l  in p2:
             w= p2.css('a::attr(href)')
             yield response.follow(w.get(),callback=self.parse_cat)