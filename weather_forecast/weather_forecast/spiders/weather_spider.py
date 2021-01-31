import scrapy

class Weather(scrapy.Spider):
    name = "weather"
    start_urls = ['https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/558/saopaulo-sp']

    def parse(self, response):
        yield{            
            'cidade': response.css('span::text')[26].get(), 
            'temperatura': response.css('span::text')[29].get(), 
            'previsao': response.css('span::text')[30].get(),  
            'sensacao': response.css('span::text')[31].get(),
            'umidade':  response.css('span::text')[34].get(),
            'pressao': response.css('span::text')[36].get(),
            'vento': response.css('div::text')[374].get()
        }

