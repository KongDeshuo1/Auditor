from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from Inventory import Inventory


supplier = Supplier("S001", "Tech Supplies", "sales@example.com")
product = PhysicalProduct("P001", "Laptop", 1200.0, 15, 2.5, supplier)

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(product)
inventory_a.remove_product("P001")

print("\nProduct in Inventory A:")
print(inventory_a.find_product("P001"))

print("\nProduct still exists:")
product.display_information()

inventory_b.add_product(product)

print("\nInventory B contains the same product object:")
print(inventory_b.find_product("P001") is product)