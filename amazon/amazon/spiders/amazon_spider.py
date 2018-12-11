import scrapy
import time
from scrapy.selector import Selector
from amazon.items import AmazonItem

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = ['https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=backpack&rh=i%3Aaps%2Ck%3Abackpack']
    # start_urls = ['http://127.0.0.1:8020/demo/demo.html?__hbt=1541055069943']
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'upgrade-insecure-requests': 1,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
    }

    # def start_requests(self):
    #     for url in self.start_urls:
    #         print("--" + url)
    #         yield self.make_requests_from_url(url)

    def parse(self, response):
        # productUl = response.css("#s-results-list-atf")
        # print("---" + str(len(productUl.css(".s-result-item"))) + "---")

        productList = response.css(".s-result-item.celwidget")

        # tempResponse = HtmlResponse(url="demo.html",)
        # productList = tempResponse.css("#s-results-list-atf>li")
        # productList = productUl.css(".s-result-item.celwidget")
        # productList = response.css("#s-results-list-atf>li")
        print("---" + str(len(productList)) + "---")
        for product in productList:
            # print(product.css("::text").extract_first())
            id = product.css("::attr(id)").extract_first()
            code = product.css("::attr(data-asin)").extract_first()
            # link = product.css("a.a-link-normal.s-access-detail-page")
            title = product.css("a.a-link-normal.s-access-detail-page h2.a-size-medium::attr(data-attribute)").extract_first()


            print(str(id) + "---" + str(code))
            print(title)
            print("----")
            item = AmazonItem(title = title)
            yield item
            # productInner = product.css(".s-item-container>.a-fixed-left-grid>.a-fixed-left-grid-inner")
            # print(productInner)
            # if len(productInner) == 0: continue
            # print(product.css(".a-row.a-spacing-small h2::text").extract_first())
