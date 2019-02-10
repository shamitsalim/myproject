import scrapy


class CuisineItem(scrapy.Item):
    # define the fields for your item here like:
	name = scrapy.Field()
	images = scrapy.Field()
	preparation_time = scrapy.Field()
	cooking_time = scrapy.Field()
	serves = scrapy.Field()
	chef_name = scrapy.Field()
	chef_url = scrapy.Field()
	chef_imagge = scrapy.Field()
	ingredients = scrapy.Field()
	methods = scrapy.Field()
	description = scrapy.Field()
	programme_name =scrapy.Field()
	programme_url =scrapy.Field()
    

