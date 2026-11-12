from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from file_handler import load_inventory, save_inventory
from Supplier import Supplier



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

            product_type = input("Choose product type: ").strip()

            if product_type == "1":
                try:
                    weight = float(input("Weight (kg): "))

                except ValueError:
                    print("Weight must be a number.")
                    continue

                if not (0 < weight < float("inf")):
                    print("Weight must be a finite number greater than 0.")
                    continue

                product = PhysicalProduct(
                    product_id, name, price, stock, weight, supplier
                )

            elif product_type == "2":
                try:
                    download_size = float(input("Download size (MB): "))

                except ValueError:
                    print("Download size must be a number.")
                    continue

                if not (0 < download_size < float("inf")):
                    print("Download size must be a finite number greater than 0.")
                    continue

                product = DigitalProduct(
                    product_id, name, price, stock, download_size, supplier
                )

            else:
                print("Invalid product type. Please choose 1 or 2.")
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
