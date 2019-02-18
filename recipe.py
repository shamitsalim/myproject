import scrapy
from..items import CuisineItem

class RecipeScraper(scrapy.Spider):

	name="recipe"
	
	start_urls=["http://www.bbc.co.uk/food/recipes/search?cuisines[]=british",]
	def parse(self,response):
	
		all_recipes=response.css("li.article.with-image")
		al_recipes=response.css("li.article.no-image")
		
		
		for each in all_recipes:
			for href in each.css("div.left.with-image h3 a::attr(href)"):
				url=response.urljoin(href.extract())
				
				yield scrapy.Request(url,callback=self.parse_dir_contents)
				next_page=response.css("li.pagInfo-page-numbers-next a::attr(href)").extract_first()
				if next_page is not  None:
					next_page=response.urljoin(next_page)
					yield scrapy.Request(url=next_page,callback=self.parse)
					
				
		for eachh in al_recipes:
			for href in eachh.css("div.left h3 a::attr(href)"):
				url=response.urljoin(href.extract())
				yield scrapy.Request(url,callback=self.parse_dir_contents)
				next_pagge=response.css("li.pagInfo-page-numbers-next a::attr(href)").extract_first()
				if next_pagge is not None:
					next_pagge=response.urljoin(next_pagge)
					yield scrapy.Request(url=next_pagge,callback=self.parse)
						
			
	def parse_dir_contents(self,response):
		items=CuisineItem()
		enc=" "
		
		
		index=response.css('h1.gel-trafalgar.content-title__text::text').extract_first()
		

		image=response.css('img.recipe-media__image'). xpath('@src').extract()
		

		prep_time=response.css('p.recipe-metadata__prep-time::text').extract_first()
		

		cook_time=response.css('p.recipe-metadata__cook-time::text').extract_first()
		

		serves=response.css('p.recipe-metadata__serving::text').extract_first()
		

		cheff=response.css('div.chef__name a')
		chef=cheff. xpath("//a[@class='chef__link'] /text()").extract_first()
		
		#chef_url=cheff.xpath("//a['@href']").extract_first()
		chef_url=response.urljoin(cheff.xpath('@href').extract_first())
		#we=response.css('a.chef__image-link div')
		#chef_imagge=response.xpath("//img[@class='chef__image lazy-loaded']/@href").extract()
		chef_imagge=response.css("a.chef__image-link").xpath("@href").extract_first()
		#cheff_image=chef_imagge.xpath('@src').extract_first()
		ingredients=response.css('.recipe-ingredients__list-item::text,.recipe-ingredients__link::text').extract()
		enc=enc.join(ingredients)
																																																																					
		method=response.css('p.recipe-method__list-item-text::text').extract()
		description=response.css('p.recipe-description__text::text').extract()
		prog=response.css('div.chef__programme-name a')
		programme=prog.css('.chef__link::text').extract_first()
		programme_url=response.urljoin(prog.xpath('@href').extract_first())
																																																																																																												
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
