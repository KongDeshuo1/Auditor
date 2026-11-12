import json

from Inventory import Inventory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct


INVENTORY_FILE = "inventory_lab7.json"


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

    if not isinstance(data, list):
        raise ValueError("Inventory data must be a list.")

    for item in data:
        if item["type"] == "physical":
            product = PhysicalProduct(
                item["id"],
                item["name"],
                item["price"],
                item["stock"],
                item["weight"]
            )

        elif item["type"] == "digital":
            product = DigitalProduct(
                item["id"],
                item["name"],
                item["price"],
                item["stock"],
                item["download_size"]
            )

        else:
            raise ValueError(f"Unknown product type: {item['type']}")

        inventory.add_product(product)

    print("Inventory loaded successfully.")
    return inventory