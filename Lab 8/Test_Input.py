from input_helpers import get_positive_float


price = get_positive_float("Enter price: ")
print(f"Accepted price: ${price:.2f}")