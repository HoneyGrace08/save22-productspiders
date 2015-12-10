# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Www_Expansys_Com_Sg(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    #retailer_sku_code = scrapy.Field()
    #model = scrapy.Field()
    mfr = scrapy.Field()
    sku = scrapy.Field()
    upc = scrapy.Field()
    ean = scrapy.Field()
    image_urls = scrapy.Field()
    currency = scrapy.Field()
    price = scrapy.Field()
    old_price = scrapy.Field()
    #crawl_time = scrapy.Field()
    #promo_price = scrapy.Field()
    #promo_qty = scrapy.Field()
    #promo_data = scrapy.Field()
    #promo_expiry = scrapy.Field()
    #current_price = scrapy.Field()
    brand = scrapy.Field()
    offer = scrapy.Field()
    stock = scrapy.Field()
    #pass

class AllForYou_Sg(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    categories = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    image_urls = scrapy.Field()
    old_price = scrapy.Field()
    offer = scrapy.Field()
    out_of_stock = scrapy.Field() 
    #retailer_sku_code = scrapy.Field()
    #model = scrapy.Field()
    #mpn = scrapy.Field()
    sku = scrapy.Field()
    #ean = scrapy.Field()
    #currency = scrapy.Field()
    price = scrapy.Field()
    #crawl_time = scrapy.Field()
    #promo_price = scrapy.Field()
    #promo_qty = scrapy.Field()
    #promo_data = scrapy.Field()
    #promo_expiry = scrapy.Field()
    #current_price = scrapy.Field()
    #brand = scrapy.Field()
    #pass
