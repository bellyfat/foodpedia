import scrapy
from scrapy.contrib.spiders import CrawlSpider

from goodsmatrix import xpath_extractor
from goodsmatrix import url_extractor
from goodsmatrix.good_item import GoodItem
from goodsmatrix import esl_parser


class GoodsMatrixSpider(CrawlSpider):
    name = 'goodsmatrix'
    allowed_domains = ['goodsmatrix.ru']
    start_urls = ['http://www.goodsmatrix.ru/goods-catalogue/Frozen-meat-natural-convenience-foods.html']
    #start_urls = ['http://www.goodsmatrix.ru/goods-catalogue/Goods/Foodstuffs.html']

    def parse(self, response):
        return self.parse_catalog_node(response)

    def parse_catalog_node(self, response):
        child_nodes_urls = url_extractor.extract_child_nodes_urls(response)
        if child_nodes_urls:
            for child_node_url in child_nodes_urls:
                yield scrapy.Request(child_node_url, callback=self.parse_catalog_node)
        else:
            yield self.parse_catalog_end_node(response)

    def parse_catalog_end_node(self, response):
        """parse catalog node without children.
        return prepeared request to  parse the category's list of goods."""
        return scrapy.Request(
            url_extractor.extract_url_with_list_of_goods(response),
            callback=self.parse_list_of_goods
        )

    def parse_list_of_goods(self, response):
        for goods_url in url_extractor.extract_goods_urls(response):
            yield scrapy.Request(goods_url, callback=self.parse_good)

    def parse_good(self, response):
        good = GoodItem(xpath_extractor.extract_goods_properties_dict(response))
        esl_dict = esl_parser.parse_esl(good['esl'])
        good['proteins_as_double'] = esl_dict.get('proteins', None)
        good['fats_as_double'] = esl_dict.get('fats', None)
        good['carbohydrates_as_double'] = esl_dict.get('carbohydrates', None)
        good['calories_as_double'] = esl_dict.get('calories', None)
        good['url'] = response.url
        return good