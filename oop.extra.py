#a
class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        
    def describe_shop(self):
        print("This shop is called {} and it is a {} store.".format(self.shop_name, self.store_type))
        
    def open_shop(self):
        print("The shop is open now!")

#b
store1 = Shop("Vivat", "Bookshop")
store2 = Shop("Marsal", "Supermarket")
store3 = Shop("Osafay", "Clothing shop")

store1.describe_shop()
store1.open_shop()
store2.describe_shop()
store2.open_shop()
store3.describe_shop()
store3.open_shop()

#c
class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0
        
    def describe_shop(self):
        print("This is a {} shop called {}.".format(self.store_type, self.shop_name))
        
    def open_shop(self):
        print("The online shop is now open.")

store = Shop("Vivat", "Bookshop")
print(store.number_of_units)
store.number_of_units = 10
print(store.number_of_units)

#d
class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 10
        
    def describe_shop(self):
        print("This is a {} shop called {}.".format(self.store_type, self.shop_name))
        
    def open_shop(self):
        print("The online shop is now open.")
        
    def set_number_of_units(self, number):
        self.number_of_units = number
        
    def increment_number_of_units(self, increment):
        self.number_of_units += increment

store = Shop("Vivat", "Bookshop")
print(store.number_of_units)

store.increment_number_of_units(15)
print(store.number_of_units)

#e
class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = []
        
    def get_discount_products(self):
        print("Discounted products:")
        for product in self.discount_products:
            print("- " + product)

store_discount = Discount("Vivat", "Bookshop")
store_discount.discount_products = ["Book 1", "Book 2", "Book 3"]
store_discount.get_discount_products()

