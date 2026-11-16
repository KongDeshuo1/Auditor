from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier


supplier = Supplier("S001", "Tech Supplies", "sales@example.com")

products: list[Product] = [
    PhysicalProduct("P001", "Laptop", 1200.0, 15, 2.5, supplier),
    DigitalProduct("D001", "E-book", 15.0, 20, 50.0, supplier)
]

for product in products:
    product.display_information()
    print(product.get_fulfilment_info())
    print("-" * 30)