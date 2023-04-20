from Product import Product
from Store import Store
from os import system

system("clear")

print()

print("___ Products ___")
apple = Product("Apple", 1.00, "Fruit")
apple.print_info()
pineapple = Product("Pineapple", 2.00, "Fruit")
pineapple.print_info()
milk = Product("Milk", 3.00, "Dairy")
milk.print_info()
eggs = Product("Eggs", 4.00, "Dairy")
eggs.print_info()
bacon = Product("Bacon", 5.00, "Meat")
bacon.print_info()
bread = Product("Bread", 6.00, "Bakery")
bread.print_info()
capnCrunch = Product("Cap'n Crunch", 7.00, "Cereal")
capnCrunch.print_info()
blackbeans = Product("Black Beans", 8.00, "Beans")
blackbeans.print_info()

print()

# Store instance 1
store1 = Store("Cragar's Store")
store1.add_product(apple)
store1.add_product(milk)
store1.add_product(bread)
store1.add_product(bacon)
store1.add_product(capnCrunch)

apple.update_price(0.10, True)

store1.inflation(0.05)

store1.sell_product("App-456-Fru")


print()

# Store instance 2
store2 = Store("Sam's Store")
store2.add_product(pineapple)
store2.add_product(blackbeans)
store2.add_product(bread)
store2.add_product(bacon)
store2.add_product(capnCrunch)

capnCrunch.update_price(0.20, False)

store2.sell_product("Pin-456-Fru")


print()
# Store instance 3
store3 = Store("Buck's Store")
store3.add_product(blackbeans)
store3.add_product(apple)
store3.add_product(pineapple)
store3.add_product(bacon)
store3.add_product(capnCrunch)

blackbeans.update_price(0.30, True)

store3.set_clearance("Fruit", 0.10)

print()

store1.print_products()
print()

store2.print_products()
print()

store3.print_products()
print()

print(store1)
print(store2)
print(store3)

#
#
#
print()
