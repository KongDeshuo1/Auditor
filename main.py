from Product import Product
from file_handler import load_inventory, save_inventory


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
