class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    def get_product_id(self):
        return self.__product_id


    def update_stock(self, quantity):
        if quantity < 0:
            print("Invalid quantity. Stock cannot be negative.")
            return

        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")



class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.get_product_id()) is not None:
            print("Product ID already exists.")
            return

        self.__products.append(product)
        print("Product added successfully!")

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            product.display_information()
            print("-" * 30)


inventory = Inventory()

product1 = Product("P001", "Laptop", 1200.00, 15)
product2 = Product("P002", "Mouse", 25.50, 40)

inventory.add_product(product1)
inventory.add_product(product2)

inventory.display_all()

    