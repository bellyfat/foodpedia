import scrapy

class GoodItem(scrapy.Item):
    goodsmatrix_url = scrapy.Field()
    name = scrapy.Field()
    name_en = scrapy.Field()
    barcode = scrapy.Field()
    best_before = scrapy.Field()
    comment = scrapy.Field()
    comment_en = scrapy.Field()
    ingredients = scrapy.Field()
    e_additives = scrapy.Field()
    netto_weight = scrapy.Field()
    standart = scrapy.Field()
    store_conditions = scrapy.Field()
    esl_as_string = scrapy.Field()
    pack_type = scrapy.Field()
    proteins_as_double = scrapy.Field()
    fats_as_double = scrapy.Field()
    carbohydrates_as_double = scrapy.Field()
    calories_as_double = scrapy.Field()
    agrovoc_ingredients = scrapy.Field()
