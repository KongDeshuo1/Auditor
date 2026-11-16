from ProductFactory import ProductFactory
from Supplier import Supplier
from file_handler import load_inventory, save_inventory
from input_helpers import get_positive_float
from csv_loader import load_products

import csv


def main() -> None:
    try:
        inventory = load_inventory()

    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Unable to load inventory: {error}")
        print("Check inventory_lab7.json before running again.")
        return

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("7. Load Products from CSV")
        print("----------------------------")

        option = input("Enter option: ").strip()

        if option == "1":
            inventory.display_all()

        elif option == "2":
            product_id = input("Product ID: ").strip().upper()

            if not product_id:
                print("Product ID cannot be empty.")
                continue

            if inventory.search_product(product_id) is not None:
                print("Product ID already exists.")
                continue

            name = input("Product Name: ").strip()

            if not name:
                print("Product name cannot be empty.")
                continue

            price = get_positive_float("Price: ")

            while True:
                try:
                    stock = int(input("Stock Quantity: "))

                    if stock < 0:
                        print("Stock cannot be negative.")
                        continue

                    break

                except ValueError:
                    print("Stock must be a whole number.")

            supplier_id = input("Supplier ID: ").strip().upper()
            supplier_name = input("Supplier Name: ").strip()
            contact_email = input("Supplier Contact Email: ").strip()

            if not supplier_id or not supplier_name or not contact_email:
                print("Supplier details cannot be empty.")
                continue

            supplier = Supplier(supplier_id, supplier_name, contact_email)

            print("\nProduct Type")
            print("1. Physical Product")
            print("2. Digital Product")

            choice = input("Choose product type: ").strip()

            weight: float | None = None
            download_size: float | None = None

            if choice == "1":
                product_type = "physical"
                weight = get_positive_float("Weight (kg): ")

            elif choice == "2":
                product_type = "digital"
                download_size = get_positive_float("Download size (MB): ")

            else:
                print("Invalid product type. Please choose 1 or 2.")
                continue

            try:
                product = ProductFactory.create(
                    product_type=product_type,
                    product_id=product_id,
                    name=name,
                    price=price,
                    stock_quantity=stock,
                    supplier=supplier,
                    weight=weight,
                    download_size=download_size
                )

            except ValueError as error:
                print(f"Unable to create product: {error}")
                continue

            inventory.add_product(product)

        elif option == "3":
            product_id = input("Enter Product ID: ").strip().upper()
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
                continue

            product.display_information()
            print("Enter the new total stock quantity.")

            while True:
                try:
                    quantity = int(input("Stock Quantity: "))
                    product.update_stock(quantity)
                    break

                except ValueError:
                    print("Stock must be a whole number of 0 or more.")

        elif option == "4":
            product_id = input("Enter Product ID: ").strip().upper()
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")

            else:
                product.display_information()
                product.display_supplier()

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

        elif option == "7":
            path = input("CSV filename [products.csv]: ").strip()

            if not path:
                path = "products.csv"

            print("Enter the supplier for the products in this file.")

            supplier_id = input("Supplier ID: ").strip().upper()
            supplier_name = input("Supplier Name: ").strip()
            contact_email = input("Supplier Contact Email: ").strip()

            if not supplier_id or not supplier_name or not contact_email:
                print("Supplier details cannot be empty.")
                continue

            supplier = Supplier(supplier_id, supplier_name, contact_email)

            try:
                load_products(path, inventory, supplier)

            except OSError as error:
                print(f"Unable to read products file: {error}")

            except (UnicodeError, csv.Error) as error:
                print(f"Invalid CSV file: {error}")

        else:
            print("Invalid option. Please enter 1 to 7.")


if __name__ == "__main__":
    main()