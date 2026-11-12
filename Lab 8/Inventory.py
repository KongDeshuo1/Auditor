from Product import Product

class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product):
        if self.search_product(product.get_product_id()) is not None:
            print("Product ID already exists.")
            return

        self.__products.append(product)
        print("Product added successfully!")

    def search_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None


    def find_product(self, product_id: str) -> Product | None:
        return self.search_product(product_id)

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)

        if product is None:
            print("Product not found.")
            return

        self.__products.remove(product)
        print("Product removed successfully.")

    def display_all(self) -> None:
        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            product.display_information()
            print("-" * 31)

    def to_list(self) -> list[dict[str, str | float | int]]:
        data = list[dict[str, str | float | int]]()

        for product in self.__products:
            data.append(product.to_dict())

        return data

    ###comments###

