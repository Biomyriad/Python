from store import Store
from product import Product

sw = Store("SafeWay")

pickels = Product("Pickles", 3.99, "food")
cake = Product("Cake", 5.99, "food")
hammer = Product("Hammer", 11.95, "hardware")

sw.add_product(pickels)
sw.add_product(cake)
sw.add_product(hammer)

for i in sw.products:
    i.print_info()
print("-----------------------")

sw.inflation(1.5)

for i in sw.products:
    i.print_info()
print("-----------------------")

sw.set_clearance("hardware", 0.75)

for i in sw.products:
    i.print_info()
print("-----------------------")

sw.sell_product("food_Pickles")

for i in sw.products:
    i.print_info()
print("-----------------------") 