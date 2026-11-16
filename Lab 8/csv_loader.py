import csv

from Inventory import Inventory
from ProductFactory import ProductFactory
from Supplier import Supplier


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="", encoding="utf-8-sig")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        loaded: int = 0

        with file:
            reader = csv.reader(file)
            next(reader, None)

            for row_number, row in enumerate(reader, start=2):
                try:
                    product_type, product_id, name, price_text, stock_text, weight_text, download_size_text = row

                    price = float(price_text)
                    stock_quantity = int(stock_text)

                    weight: float | None = None
                    download_size: float | None = None

                    if weight_text.strip():
                        weight = float(weight_text)

                    if download_size_text.strip():
                        download_size = float(download_size_text)

                    product = ProductFactory.create(
                        product_type=product_type,
                        product_id=product_id,
                        name=name,
                        price=price,
                        stock_quantity=stock_quantity,
                        supplier=supplier,
                        weight=weight,
                        download_size=download_size
                    )

                    if inventory.search_product(product_id) is not None:
                        raise ValueError(f"Product ID already exists: {product_id}")

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as error:
                    print(f"Row {row_number} skipped: {error}")

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")