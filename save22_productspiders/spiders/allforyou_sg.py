import scrapy
from save22_productspiders.items import AllForYou_Sg

class AllForYou(scrapy.Spider):
    name = "allforyou"
    allowed_domains = ["allforyou.sg"]
    start_urls = [
        "https://allforyou.sg/",
    ]

    def parse(self, response):
        for href in response.css("div.span2.categorybox-span > div.categorybox.thumbnail.text-center > div.thumb > a::attr('href')"):
          url = response.urljoin(href.extract())
          #print url
          request = scrapy.Request(url, callback=self.parse_item_na)
          yield request
            
    def parse_item_na(self, response):
        for href in response.css("div.FeaturedHeader > h2> a::attr('href')"):
          #print "pumasok"
          url2 = response.urljoin(href.extract())
          #print url2
          request = scrapy.Request(url2, callback=self.parse_dir_contents)
          yield request
           
                     
    def parse_dir_contents(self, response):


        categories = []
        contents = response.xpath('//*[@id="content_breadcrumb"]/li/a/img')
        for content in contents:
            categories.append(content.xpath('@title').extract()[0])

        items = []
        item_na = response.xpath('//div[@class="prod-data"]')
        categories = response.xpath('//title/text()').extract()[0]
     
        
        for i in item_na:
            item = AllForYou_Sg()
            item['url'] = response.url or None
            item['categories'] = str(categories) or None
            item['sku'] = i.xpath('@id').extract() or None
            item['title'] = i.xpath('@data-name').extract() or None
            item['description'] = i.xpath('@data-desc').extract()
            item['image_urls'] = i.xpath('@data-imgurl').extract() or None
            item['price'] = i.xpath('@data-price').extract() or None
            item['old_price'] = i.xpath('@data-oldprice').extract() or None
            item['offer'] = i.xpath('@data-offername').extract()  or None
            item['out_of_stock'] = i.xpath('@data-outofstock').extract()   or None
            items.append(item)
            yield item
        #return items

        next_page = response.css("div.pager > a::attr('href')")
        if next_page:
            url3 = response.urljoin(next_page[0].extract())
            print "Next Page: " + url3
            yield scrapy.Request(url3, self.parse_dir_contents)
        


        
           
        
        