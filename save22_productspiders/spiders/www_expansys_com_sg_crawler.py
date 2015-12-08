from datetime import datetime

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from save22_productspiders.items import Www_Expansys_Com_Sg

class WwwExpansysComSgCrawler (CrawlSpider):
  name = "expansys_crawler"
  allowed_domains = ["expansys.com.sg"]
  start_urls = [
        "http://www.expansys.com.sg/",
    ]
  
  rules = (
        Rule(LinkExtractor(allow=(r'.+sg/\S+\d+/',),deny = (r'.+/.filter',)),
        callback = 'parse_item',
        follow=True),

        Rule(LinkExtractor(allow = (r'.+sg/?page.+',),deny = (r'.+/.filter',)),
        callback = 'parse_item',
        follow=True),
    )


  def parse_item(self, response):
      sku = list()
      items = list()
      item_na = response.xpath('//*[@id="product"]')
      item_sku = response.xpath('//@data-sku').extract()  

      if item_sku in sku:
          return
      sku.insert(len(sku), item_sku)

      for i in item_na:
          item = Www_Expansys_Com_Sg()
          item['url'] = i.xpath('//html/head/link[1]/@href').extract() 
          item['sku'] = item_sku
          item['ean'] = i.xpath('//*[@id="prod_core"]/ul/li[2]/span/text()').extract()
          item['mfr'] =i.xpath('//*[@id="prod_core"]/ul/li[3]/span/text()').extract()
          item['brand'] = i.xpath('//*[@id="prod_core"]/ul/li[4]/a/text()').extract() or None
          item['title'] = i.xpath('//div[@id="title"]/h1/text()').extract()
          item['description'] = i.xpath('//div[@id="description"]/h2/text()').extract()
          item['image_urls'] = i.xpath('//*[@id="image"]/a/@href').extract()
          item['currency'] = i.xpath('//*[@id="price"]/meta/@content').extract()
          item['price'] = i.xpath('//p[@id="price"]/strong/span/text()').extract() 
          item['old_price'] = i.xpath('//*[@id="prod_core"]/span/ul/li[1]/strong/strike/text()').extract() or None
          item['offer'] = i.xpath('//*[@id="del_note"]/span/text()').extract() or None
          item['stock'] = i.xpath('//*[@id="stock"]/text()').extract()
          items.append(item)
          yield item