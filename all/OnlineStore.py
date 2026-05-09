class Product:
    def __init__(self, name, price, is_available):
        self.name = name
        self.price = price
        self.is_available = is_available

    def show_info(self):
        print(f'Product Name: {self.name}')
        print(f'Product Price: ${self.price}')
        print(f'Available: {self.is_available}')

macBookPro = Product("MacBookPro16", 1200, True)
airPods4 = Product("Air Pods 4", 150, True)

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_total(self):
        total = 0
        if self.products:
            for product in self.products:
                total += product.price

        return total

    def print_receipt(self):
        total = self.get_total()

        if total != 0:
            for product in self.products:
                print(f'{product.name} ------- ${product.price}')

        print(f'=== TOTAL: ${total} ===')


cart = Cart()
cart.add_product(macBookPro)
cart.add_product(airPods4)
cart.print_receipt()