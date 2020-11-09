import scrapy
from ..items import ScrapepaginationItem

class scrapePagination(scrapy.Spider):
    name = 'pagination'
    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]
    def parse(self, response):
        items = ScrapepaginationItem()
        all_quotes = response.css('div.quote')
        for q in all_quotes:
            title = q.css('span.text::text').extract()
            author = q.css('.author::text').extract()
            tags = q.css('a.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            yield items

        next_page = 'https://quotes.toscrape.com/page/'+ str(scrapePagination.page_number) +'/'
        if scrapePagination.page_number <11:
            scrapePagination.page_number += 1
            yield response.follow(next_page, callback= self.parse)