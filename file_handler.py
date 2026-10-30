import json

from Product import Product
from Inventory import Inventory

INVENTORY_FILE = "inventory.json"


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
