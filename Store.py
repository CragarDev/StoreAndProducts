class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        print("=== Product Added ===")
        new_product.print_info()
        return self

    def sell_product(self, id):
        # product_sold = self.products.pop(id)
        for product in self.products:
            if product.id == id:
                product_sold = product
                self.products.remove(product)
                print("=== Product Sold ===")
                product_sold.print_info()
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self

    def print_products(self):
        print(f"*** {self.name} Products ***")
        print("--------------------------")
        for product in self.products:
            product.print_info()
        return self

    def __repr__(self):
        return f"Store: {self.name}, Products: {self.products}"
