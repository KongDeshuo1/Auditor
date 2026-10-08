import json

INVENTORY_FILE = "inventory.json"


# Load saved inventory
def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:
            inventory = json.load(file)

        print("Inventory loaded successfully.")
        return inventory

    except FileNotFoundError:
        print("No saved inventory found. Starting with an empty inventory.")
        return []


# Save inventory to JSON
def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully.")


# Find a product using its ID
def find_product(inventory, product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product

    return None


# Get a valid stock quantity
def get_valid_stock():
    while True:
        entry = input("Stock Quantity: ").strip()

        try:
            stock = int(entry)

            if stock >= 0:
                return stock

        except ValueError:
            pass

        print("Invalid quantity. Enter a whole number of 0 or more.")


# Get a valid price
def get_valid_price():
    while True:
        entry = input("Price: ").strip()

        try:
            price = float(entry)

            if 0 <= price < float("inf"):
                return price

        except ValueError:
            pass

        print("Invalid price. Enter a finite number of 0 or more.")


# Add a new product
def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ").strip().upper()

    if product_id == "":
        print("Product ID cannot be empty.")
        return

    if find_product(inventory, product_id) is not None:
        print("Product ID already exists.")
        return

    name = input("Product Name: ").strip()

    if name == "":
        print("Product name cannot be empty.")
        return

    price = get_valid_price()
    stock = get_valid_stock()

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock,
        "transactions": [
            {
                "quantity_change": stock,
                "amount": round(price * stock, 2)
            }
        ]
    }

    inventory.append(product)

    print("Product added successfully!")


# Replace a product's stock with a new quantity
def update_stock(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip().upper()
    product = find_product(inventory, product_id)

    if product is None:
        print("Product not found.")
        return

    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")
    print("Enter the new total stock quantity.")

    new_stock = get_valid_stock()
    quantity_change = new_stock - product["stock"]

    # Support products that do not yet have transaction history
    if "transactions" not in product:
        product["transactions"] = []

    product["transactions"].append({
        "quantity_change": quantity_change,
        "amount": round(quantity_change * product["price"], 2)
    })

    product["stock"] = new_stock

    print("Stock updated successfully!")


# Search for and display one product
def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip().upper()
    product = find_product(inventory, product_id)

    if product is None:
        print("Product not found.")
        return

    print("\nProduct Found")
    print("-" * 40)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print("-" * 40)


# Display every product
def display_all(inventory):
    print("\nCurrent Inventory")

    if not inventory:
        print("Inventory is empty.")
        return

    print("-" * 70)

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("-" * 70)


# Main menu
def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    try:
        inventory = load_inventory()

    except (OSError, ValueError) as error:
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
            display_all(inventory)

        elif option == "2":
            add_product(inventory)

        elif option == "3":
            update_stock(inventory)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            try:
                save_inventory(inventory)

            except OSError as error:
                print(f"Unable to save inventory: {error}")

        elif option == "6":
            print("Saving inventory before exit...")

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