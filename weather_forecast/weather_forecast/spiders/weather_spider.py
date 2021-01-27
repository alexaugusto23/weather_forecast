import logging
import scrapy
from scrapy.selector.unified import _response_from_text

class Weather(scrapy.Spider):
    name = "weather"
    start_urls = ['https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/558/saopaulo-sp']

    def parse(self, response):
        for x in response.css('span.-bold -gray-dark-2 -font-55 _margin-l-20 _center'):
            yield{
                'temperatura': x.css('_center')
            
            }
