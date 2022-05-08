
class Product:
    def __init__(self, product_name, product_price, product_category):
        self.product_name = product_name
        self.product_price = product_price
        self.product_category = product_category
        self.product_id = f"{product_category}_{product_name}"
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.product_price += self.product_price * percent_change
        else:
            self.product_price -= self.product_price * percent_change 
        self.product_price = round(self.product_price, 2)
    def print_info(self):
        print(f"{self.product_name} @ ${self.product_price} - Category: {self.product_category} ID: {self.product_id}")