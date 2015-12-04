
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
import scrapy
import pdb
import re
from scrapy.http import Request
from save22_productspiders.items import Www_Expansys_Com_Sg

class Expansys(scrapy.Spider):
    name = "expansys"
    allowed_domains = ["expansys.com.sg"]
    start_urls = [
        "http://www.expansys.com.sg/"
    ]

    urls = ""

    def parse(self, response):
        
        cat_links = response.xpath('//a[@class="nitem"]/@href').extract()
        for link in cat_links[1:]:
            print link
            #pdb.set_trace()
            

            accessories = "http://www.expansys.com.sg/accessory-finder/"
            smart_gadget = "http://www.expansys.com.sg/smart-gadget-offers/"
            if accessories == link:
                print "accessories"
                yield Request(url="http://www.expansys.com.sg/accessory-finder/", callback=self.parse_accessories)
            else:
                yield Request(url=link, callback=self.parse_item_na)

              

    def parse_item_na(self, response):
        
        items = response.xpath('//div[@class="productGrid"]/ul/li[@class="image"]/a/@href').extract()
        #pdb.set_trace()
        for item in items:
            #print item
            yield Request(url='http://www.expansys.com.sg'+str(item), callback=self.parse_dir_contents)

        #next page   
        if response.xpath('//li[@class="next"]/a/@href').extract():
            next_page=response.xpath('//li[@class="next"]/a/@href').extract()[0]
            yield Request(url='http://www.expansys.com.sg'+str(next_page), callback=self.parse_item_na)



    def parse_accessories(self,response):
        #pass
        #pdb.set_trace()

        man_links = response.xpath('//ul[@class="menus"]/li/select[@id="manufacturer"]/option/@value').extract()[1:]
        for man in man_links:
            print "Pumasok"
            urls = 'http://www.expansys.com.sg/#manid='+ str(man)
            self.urls = urls
            #print urls 
            #yield Request( url = 'http://www.expansys.com.sg/#manid='+ str(man) , callback=self.parse_accessories)
            if  self.urls:
                print "######################################################"
                yield Request(url='http://www.expansys.com.sg/accessoryservice.aspx?action=getmodels&manid='+str(man), callback=self.parse_get_model)

        
    def parse_get_model(self ,response):
        #pdb.set_trace()
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        body = response.xpath('//accessories/options/text()').extract()
        print body
        model = re.search('value\=\"(\d+)', body).group(1)
        print model
        for m in model:
            yield Request( url = self.urls+'&instockcode='+str(m) , callback=self.parse_dir_contents)

    def  parse_dir_contents(self, response):
        #pdb.set_trace()
        sku = list()
        items = list()
        item_na = response.xpath('//ul[@id="breadcrumbs"]')
        item_sku = response.xpath('//@data-sku').extract()  

        if item_sku in sku:
            return
        sku.insert(len(sku), item_sku)

        for i in item_na:
            item = Www_Expansys_Com_Sg()
            item['sku'] = item_sku
            #pdb.set_trace()
            item['url'] = response.url or None
            item['title'] = i.xpath('//div[@id="title"]/h1/text()').extract()
            # item['description'] = i.xpath()
            # item['image_urls'] = i.xpath()
            items.append(item)
            yield item