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

def main():
    inventory = Inventory()

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("4. Search Product")
        print("6. Exit")
        print("----------------------------")

        option = input("Enter option: ").strip()

        if option == "1":
            inventory.display_all()

        elif option == "2":
            product_id = input("Product ID: ").strip().upper()

            if product_id == "":
                print("Product ID cannot be empty.")
                continue

            if inventory.search_product(product_id) is not None:
                print("Product ID already exists.")
                continue

            name = input("Product Name: ").strip()

            if name == "":
                print("Product name cannot be empty.")
                continue

            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))

            except ValueError:
                print("Enter a number for price and a whole number for stock.")
                continue

            if not (0 <= price < float("inf")):
                print("Price must be a finite number of 0 or more.")
                continue

            if stock < 0:
                print("Stock cannot be negative.")
                continue

            product = Product(product_id, name, price, stock)
            inventory.add_product(product)

        elif option == "4":
            product_id = input("Enter Product ID: ").strip().upper()
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
            else:
                product.display_information()

        elif option == "6":
            print("Thank you for using Inventory Management System.")
            break

        else:
            print("Invalid option. Please enter 1, 4 or 6.")


if __name__ == "__main__":
    main()

    