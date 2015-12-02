from datetime import datetime

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from save22_productspiders.items import Www_Expansys_Com_Sg

class WwwExpansysComSgCrawler ():
  name = "www_expansys_com_sg_crawler"
  allowed_domains = ["expansys.com.sg"]
  start_urls = [
        "http://www.expansys.com.sg/mobile-phones/",
    ]
  
  rules = (
    Rule (
          LinkExtractor(
              allow = (r'(.+)',),
          ),
          callback = 'parse_item',
          ),
  )

  def parse_item(self, response):

    content = response.xpath()
    #pass