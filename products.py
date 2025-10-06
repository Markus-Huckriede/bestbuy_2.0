class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if name.strip() == "":
            raise ValueError("Enter a product name")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    """
    promotions
    """

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    """
    quantities of the products
    """

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    """
    status activate and deactivate
    """

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    """
    show functions for displaying to the user
    """

    def show(self) -> str:
        promo_info = f" | Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name} - ${self.price:.2f} ({self.quantity} pcs){promo_info}"

    def __str__(self):
        return self.show()

    """
    buy functions
    """

    def buy(self, quantity: int) -> float:
        if not self.active:
            raise Exception(f"Product '{self.name}' is not active or in stock.")
        if quantity <= 0:
            raise Exception("Quantity must be greater than 0.")
        if quantity > self.quantity:
            raise Exception(f"Not enough '{self.name}' in stock. Available: {self.quantity}")

        total_price = (
            self.promotion.apply_promotion(self, quantity)
            if self.promotion
            else self.price * quantity
        )

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return total_price


"""
non stocked products
"""


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        raise Exception("Non-stocked products do not have a quantity.")

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise Exception("Quantity must be greater than 0.")
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def show(self) -> str:
        promo_info = f" | Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name} - ${self.price:.2f} (Unlimited){promo_info}"


"""
limited Products
"""


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise Exception("Quantity must be greater than 0.")
        if quantity > self.maximum:
            raise Exception(f"Maximum {self.maximum} of '{self.name}' per order.")
        return super().buy(quantity)

    def show(self) -> str:
        promo_info = f" | Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name} - ${self.price:.2f} (Limit {self.maximum}/order){promo_info}"
