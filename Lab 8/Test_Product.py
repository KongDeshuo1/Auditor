from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct


physical = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5)
digital = DigitalProduct("D001", "E-book", 15.00, 20, 50)

print(physical.get_fulfilment_info())
print(digital.get_fulfilment_info())

# Check that a generic Product cannot be created
try:
    product = Product("P003", "Generic Product", 10.00, 5)

except TypeError as error:
    print(f"Expected error: {error}")

mouse = PhysicalProduct("P002", "Mouse", 25.50, 40, 0.2)

print(f"Laptop shipping: ${physical.calculate_shipping_cost():.2f}")
print(f"Mouse shipping: ${mouse.calculate_shipping_cost():.2f}")