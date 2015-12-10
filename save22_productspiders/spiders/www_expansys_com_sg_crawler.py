from datetime import datetime

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
import re

from save22_productspiders.items import Www_Expansys_Com_Sg

class WwwExpansysComSgCrawler (CrawlSpider):
  name = "expansys_crawler"
  allowed_domains = ["expansys.com.sg"]
  start_urls = [
        "http://www.expansys.com.sg/",
    ]
  
  rules = (
        Rule(LxmlLinkExtractor(allow=(r'.+sg/\S+\d+/',),deny = (r'.+/.filter',)),
        callback = 'parse_item',
        follow=True),

        Rule(LxmlLinkExtractor(allow = (r'.+sg/?page.+',),deny = (r'.+/.filter',)),
        callback = 'parse_item',
        follow=True),
    )


  def parse_item(self, response):
      sku = []
      items = []
      item_na = response.xpath('//*[@id="product"]')
      item_sku = response.xpath('//@data-sku').extract()  

      if item_sku in sku:
          return
      sku.insert(len(sku), item_sku)


      for i in item_na:
          item = Www_Expansys_Com_Sg()
          item['url'] = response.url or None
          item['sku'] = item_sku  or None

          items_search =i.xpath('//*[@id="prod_core"]/ul/li').extract() or None

          for item_search in items_search:
          	print item_search
          	# sku = re.search('content="sku:(\d+)"', item_search)
          	ean = re.search('content="ean:(\d+)"', item_search)
          	upc = re.search('content="upc:(\d+)"', item_search)
          	mfr = re.search('content="mpn:(\d+)"', item_search)
          	brand = re.search('brand">(\w+)</a>', item_search)

          	# if sku:
	          # item['sku'] = sku.group(1) or None

	        if ean:
	          item['ean'] = ean.group(1) or None
	        if upc:
	          item['upc'] = upc.group(1) or None
	        if mfr:
	          item['mfr'] = mfr.group(1) or None
	        if brand:
	          item['brand'] = brand.group(1) or None

          item['title'] = i.xpath('//div[@id="title"]/h1/text()').extract()  or None
          item['description'] = i.xpath('//div[@id="description"]/h2/text()').extract()  or None
          item['image_urls'] = i.xpath('//*[@id="image"]/a/@href').extract() or None
          item['currency'] = i.xpath('//*[@id="price"]/meta/@content').extract() or None
          item['price'] = i.xpath('//p[@id="price"]/strong/span/text()').extract()   or None
          item['old_price'] = i.xpath('//*[@id="prod_core"]/span/ul/li[1]/strong/strike/text()').extract() or None
          item['offer'] = i.xpath('//*[@id="del_note"]/span/text()').extract() or None
          item['stock'] = i.xpath('//*[@id="stock"]/text()').extract()  or None
          items.append(item)
          yield item