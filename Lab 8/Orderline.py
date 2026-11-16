from Product import Product


class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        self.__product: Product = product
        self.__quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity