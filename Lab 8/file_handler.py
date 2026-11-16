import json

from Inventory import Inventory
from ProductFactory import ProductFactory
from Supplier import Supplier


INVENTORY_FILE = "inventory_lab7.json"


def save_inventory(inventory: Inventory) -> None:
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory.to_list(), file, indent=4)

    print("Inventory saved successfully.")


def load_inventory() -> Inventory:
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
        if not isinstance(item, dict):
            raise ValueError("Each product must be a dictionary.")

        supplier_data = item.get("supplier")

        if supplier_data is None:
            supplier = Supplier("UNKNOWN", "Not recorded", "Not recorded")

        else:
            if not isinstance(supplier_data, dict):
                raise ValueError("Supplier data must be a dictionary.")

            supplier = Supplier(
                supplier_data["supplier_id"],
                supplier_data["name"],
                supplier_data["contact_email"]
            )

        product = ProductFactory.create(
            product_type=item["type"],
            product_id=item["id"],
            name=item["name"],
            price=item["price"],
            stock_quantity=item["stock"],
            supplier=supplier,
            weight=item.get("weight"),
            download_size=item.get("download_size")
        )

        inventory.add_product(product)

    print("Inventory loaded successfully.")
    return inventory