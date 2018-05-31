# -*- coding: utf-8 -*-
import scrapy
import sys
import io
from scrapy.http import Request
from scrapy.selector import Selector, HtmlXPathSelector
from ..items import SteamshanItem
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from scrapy.http.cookies import CookieJar
class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['steam.com']
    # start_urls = ['https://store.steampowered.com/search/?filter=topsellers']
    start_urls = ['https://store.steampowered.com/search/?sort_by=&sort_order=0&special_categories=&filter=topsellers&page=1']
    visited_urls =set()
    def parse(self, response):
        # print('9999')
        # print(response)
        hxs=Selector(response=response).xpath('//div[@id="search_result_container"]/div')
        for obj in hxs:
            if(obj.xpath('//a[@class="search_result_row ds_collapse_flag"]')!=[]):
                liebiao=obj.xpath('.//a[@class="search_result_row ds_collapse_flag"]')
                for lielist in liebiao:
                    title=lielist.xpath('.//div[@class="col search_name ellipsis"]/span[@class="title"]/text()').extract_first().strip()
                    if(lielist.xpath('.//div[@class="col search_price discounted responsive_secondrow"]')==[]):
                        price=lielist.xpath('.//div[@class="col search_price  responsive_secondrow"]/text()').extract_first().strip()
                        cost=price
                    else:
                        price=lielist.xpath('.//div[@class="col search_price discounted responsive_secondrow"]/text()').extract()[1].strip()
                        cost=lielist.xpath('.//div[@class="col search_price discounted responsive_secondrow"]//strike/text()').extract_first().strip()

                    urld=lielist.xpath('@href').extract_first().strip()
                    # print(title)
                    # print(cost)
                    # print(price)
                    # print(urld)
                    item_obj=SteamshanItem(title=title,cost=cost,price=price,urld=urld)
                    yield item_obj


            if(obj.xpath('//div[@class="search_pagination"]//div[@class="search_pagination_right"]')!=[]):
                pages=obj.xpath('//div[@class="search_pagination"]//div[@class="search_pagination_right"]/a/@href').extract()
                for urls in pages:
                    md5_url = self.md5(urls)
                    if md5_url in self.visited_urls:
                        pass
                    else:
                        self.visited_urls.add(md5_url)
                        #将新要访问的url添加到调度器
                        # print(urls)
                        yield Request(url=urls,callback=self.parse,dont_filter=True)
                        # yield Request(
                        #     url=urls,
                        #     method="POST",
                        #     cookies=self.cookie_dict,
                        #     callback=self.show
                        # )
                #print(self.visited_urls)











    def md5(self,url):
        import hashlib
        obj = hashlib.md5()
        obj.update(bytes(url,encoding='utf-8'))
        return obj.hexdigest()



