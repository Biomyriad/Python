from product import Product

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
    def sell_product(self, id):
        for product in self.products:
            if product.product_id == id:
                self.products.remove(product)
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
    def set_clearance(self,  category, percent_discount):
        for product in self.products:
            if product.product_category == category:
                product.update_price(percent_discount, False)