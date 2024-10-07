import scrapy

class CompetitorSpider(scrapy.Spider):
    name = "competitor"
    allowed_domains = ["syra.coffee", "www.syra.coffee"]
    start_urls = ["https://syra.coffee/collections/coffee"]

    def parse(self, response):
        # Seleccionar todos los productos dentro de la lista con el id 'product-grid'
        products = response.css('ul#product-grid li.grid__item')
        
        for product in products:
            # Extraer el nombre del producto
            product_name = product.css('h3.card__heading a::text').get().strip()

            # Extraer el precio bajo
            price_low = product.xpath('.//span[@class="price-low-v2"]/span[@class="money"]/text()').get()

            # Extraer el precio alto (si existe)
            price_high = product.xpath('.//span[@class="price-high-v2"]/span[@class="money"]/text()').get()

            product_origin = product.xpath('.//div[@class="product-origin"]/text()').get().strip()


            # Crear un diccionario con los datos del producto
            yield {
                'name': product_name,
                'product_origin': product_origin,
                'price_low': price_low,
                'price_high': price_high if price_high else None  # Algunos productos no tienen precio alto
            }
