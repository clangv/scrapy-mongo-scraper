import scrapy

from books.items import BooksItem

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url, callback=self.parse, errback=self.log_error
            )

    def log_error(self, failure):
        self.longer.error(repr(failure))

    def parse(self, response):
        """
        @url https://book.toscrape.com
        @returns items 20 20
        @returns request 1 50
        @scrapes url title price
        """

        for book in response.css("article.product_pod"):
            item = BooksItem()
            item["url"] = response.urljoin(book.css("h3 a::attr(href)").get())
            item["title"] = book.css("h3 a::attr(title)").get()
            item["price"] = book.css("p.price_color::text").get()
            yield item

        next_page = response.css("li.next > a::attr(href)").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            self.logger.info(
                f"Navigating to next page with URL {next_page_url}."
            )
        yield scrapy.Request(
            url=next_page_url, 
            callback=self.parse,
            errback=self.log_error
            )
