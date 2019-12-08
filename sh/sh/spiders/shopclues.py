# -*- coding: utf-8 -*-
import scrapy


class ShopcluesSpider(scrapy.Spider):
    name = 'shopclues'
    allowed_domains = ['https://www.shopclues.com/mobiles-smartphones.html?facet_network_type[]=4G&fsrc=facet_network_type']
    start_urls = ['http://www.shopclues.com/mobiles-smartphones.html?facet_network_type[]=4G&fsrc=facet_network_type/']
    custom_settings = {
        "FEED_URI":'tmp/shopclues.csv'
        }

    def parse(self, response):
        product = response.xpath("//span[@class='prod_name']").extract()
        prices = response.xpath("//span[@class='p_price']").extract()
        discount = response.xpath("//span[@class='prd_discount']").extract()
        img = response.css('img::attr(data-img)').extract()
        for item in zip(product,prices,discount,img):
            scrapped_info = {
                 "product":item[0],
                 "price": item[1],
                 "discount":item[2],
                 "img":item[3]
                 }
            yield scrapped_info
        pass
