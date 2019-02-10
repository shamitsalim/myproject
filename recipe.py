import scrapy
from..items import CuisineItem

class RecipeScraper(scrapy.Spider):

	name="recipe"
	allowed_domain=["http://www.bbc.co.uk/food/recipes/search?cuisines[]=british"]
	start_urls=["http://www.bbc.co.uk/food/recipes/bunny_chow_38916"]
						
	def parse(self,response):
		items=CuisineItem()
		enc=" "
		index=response.css('h1.gel-trafalgar.content-title__text::text').extract_first()
		
