# -*- coding: utf-8 -*-
import scrapy


class ImagedownloadSpider(scrapy.Spider):
    name = "ImageDownload"
    allowed_domains = []
    # 仅爬取动漫动画和文化艺术两个大类的首页
    start_urls = ['http://www.nipic.com/design/acg/index.html', 'http://www.nipic.com/design/wenyi/index.html']

    def parse(self, response):
        img_src = response.xpath('//ul[@class="search-result-box clearfix"]/li/a/span/img/@src').extract()
        # 提取同一个个页面所有下载图片链接到一个列表
        yield {'image_urls': [img_url for img_url in img_src]}
