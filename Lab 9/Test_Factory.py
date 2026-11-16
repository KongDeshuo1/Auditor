from ProductFactory import ProductFactory
from Supplier import Supplier


supplier = Supplier("S001", "Tech Supplies", "sales@example.com")

physical = ProductFactory.create(
    "physical", "P001", "Desk Lamp", 25.0, 10, supplier, weight=1.0
)

digital = ProductFactory.create(
    "digital", "D001", "Photo Editor", 49.90, 100, supplier, download_size=500.0
)

physical.display_information()
print(physical.get_fulfilment_info())

print("-" * 30)

digital.display_information()
print(digital.get_fulfilment_info())

print("-" * 30)

try:
    ProductFactory.create("service", "S001", "Installation", 30.0, 5, supplier)

except ValueError as error:
    print(f"Expected error: {error}")