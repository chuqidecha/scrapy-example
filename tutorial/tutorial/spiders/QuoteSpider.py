# -*- coding: utf-8 -*-
from scrapy.spider import Spider


class QuoteSpider(Spider):
    # 每个爬虫的唯一名字
    name = "quotes"

    # 起始URL列表
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    # 页面解析，后续URL生成
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
        # 下一页
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
