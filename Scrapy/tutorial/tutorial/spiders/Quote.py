import scrapy


class QuoteSpider(scrapy.Spider):
    name = "Quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        for link_href in response.css("a::attr(href)"):
            yield{
                "href": link_href.get()
            }
              
