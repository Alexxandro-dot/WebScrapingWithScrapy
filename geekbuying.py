# -*- coding: utf-8 -*-
import scrapy


class GeekbuyingSpider(scrapy.Spider):
    name = 'geekbuying'
    allowed_domains = ['www.geekbuying.com']
    start_urls = ['https://www.geekbuying.com/deals/categorydeals/']

    def parse(self, response):
        products= response.xpath("//div[@class='flash_li']")
        for product in products:
            yield{
                'product_name': product.xpath(".//a[@class='flash_li_link']/text()").get(),
                'product_price':product.xpath(".//div[@class='flash_li_price']/span/text()").get(),
                'product_discount':product.xpath(".//div[@class='category_li_off']/text()").get(),
                'product_old_price':product.xpath(".//div[@class='flash_li_price']/del/text()").get()
            }

        next_page=response.xpath("//a[@class='next']/@href").get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
