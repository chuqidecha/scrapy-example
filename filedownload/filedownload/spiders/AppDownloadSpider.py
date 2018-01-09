# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

from filedownload.items import AppDownloadItem


class AppdownloadspiderSpider(scrapy.Spider):
    name = 'AppDownloadSpider'
    allowed_domains = ['wandoujia.com']
    start_urls = ['http://www.wandoujia.com/category/5026',
                  'http://www.wandoujia.com/category/5023']

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//*[@id="j-tag-list"]/li/div[1]/a')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_download)

    def parse_download(self, response):
        download_url = response.xpath('//div[@class="qr-info"]/a/@href').extract_first()
        item = AppDownloadItem()
        item['file_urls'] = [download_url]
        yield item