import random


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.id = f"{self.name[0:3]}-456-{self.category[0:3]}"

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price + (self.price * percent_change)
        else:
            self.price = self.price - (self.price * percent_change)
        return self

    def print_info(self):
        print(f"ID: {self.id} -- {self.name}, {self.price}, {self.category}")
        return self

    # @staticmethod
    # def random_id():
    #     r = random.randint(100000, 999999)
    #     return r
