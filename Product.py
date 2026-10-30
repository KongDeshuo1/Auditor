import json

INVENTORY_FILE = "inventory.json"

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

    def to_dict(self):
        
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

class Physical_Product(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

class Digital_Product(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")

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

    def to_list(self):
        data = []

        for product in self.__products:
            data.append(product.to_dict())

        return data


def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory.to_list(), file, indent=4)

    print("Inventory saved successfully.")


def load_inventory():
    inventory = Inventory()

    try:
        with open(INVENTORY_FILE, "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("No saved inventory found. Starting with an empty inventory.")
        return inventory

    for item in data:
        product = Product(
            item["id"],
            item["name"],
            item["price"],
            item["stock"]
        )

        inventory.add_product(product)

    print("Inventory loaded successfully.")
    return inventory

def main():

    try:
        inventory = load_inventory()

    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Unable to load inventory: {error}")
        print("Check inventory.json before running again.")
        return

    

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
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

        elif option == "3":
            product_id = input("Enter Product ID: ").strip().upper()
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
                continue

            product.display_information()
            print("Enter the new total stock quantity.")

            try:
                quantity = int(input("Stock Quantity: "))

            except ValueError:
                print("Stock must be a whole number.")
                continue

            product.update_stock(quantity)

        elif option == "4":
            product_id = input("Enter Product ID: ").strip().upper()
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
            else:
                product.display_information()
        
        elif option == "5":
            try:
                save_inventory(inventory)

            except OSError as error:
                print(f"Unable to save inventory: {error}")

        elif option == "6":
            try:
                save_inventory(inventory)

            except OSError as error:
                print(f"Unable to save inventory: {error}")
                print("Your changes are still in memory. Please try again.")
                continue

            print("Thank you for using Inventory Management System.")
            break

        else:
            print("Invalid option. Please enter 1 to 6.")


if __name__ == "__main__":
    main()

