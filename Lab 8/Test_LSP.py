from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier
from Inventory import Inventory


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


supplier = Supplier("S001", "Tech Supplies", "sales@example.com")

physical = PhysicalProduct("P001", "Laptop", 1200.0, 15, 2.5, supplier)
digital = DigitalProduct("D001", "E-book", 15.0, 20, 50.0, supplier)

show_product_details(physical)
show_product_details(digital)

inventory = Inventory()
inventory.add_product(physical)
inventory.add_product(digital)
inventory.display_all()

print("\nUpdating stock for both product types:")

products: list[Product] = [physical, digital]

for product in products:
    product.update_stock(10)
    product.display_information()