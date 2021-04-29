import scrapy


class BookparserItem(scrapy.item):
    _id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    discount_price = scrapy.Field()
    rating = scrapy.Field()
