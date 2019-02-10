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
		image=response.css('img.recipe-media__image'). xpath('@src').extract()
		prep_time=response.css('p.recipe-metadata__prep-time::text').extract_first()
		cook_time=response.css('p.recipe-metadata__cook-time::text').extract_first()
		serves=response.css('p.recipe-metadata__serving::text').extract_first()
		cheff=response.css('div.chef__name a')
		chef=cheff. xpath("//a[@class='chef__link'] /text()").extract_first()
		chef_url=cheff.xpath('@href').extract_first()
		ingredients=response.css('.recipe-ingredients__list-item::text,.recipe-ingredients__link::text').extract()
		enc=enc.join(ingredients)
		method=response.css('p.recipe-method__list-item-text::text').extract()
		description=response.css('p.recipe-description__text::text').extract()
		prog=response.css('div.chef__programme-name a')
		programme=prog.css('.chef__link::text').extract_first()
		programme_url=prog.xpath('@href').extract_first()
		items['name']=index
		items['images']=image
		items['preparation_time']=prep_time
		items['cooking_time']=cook_time
		items['serves']=serves
		items['chef_name']=chef
		items['chef_url']=chef_url
		items['chef_imagge']=chef_imagge
		items['ingredients']=enc
		items['methods']=method
		items['description']=description
		items['programme_name']=programme
		items['programme_url']=programme_url
		
		yield items
		
