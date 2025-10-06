from abc import ABC, abstractmethod


class Promotion(ABC):

    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Promotion name cannot be empty.")
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """
        Calculate the final price for the given product and quantity
        after applying the promotion.
        """
        pass

    def __str__(self):
        return self.name


class PercentDiscount(Promotion):
    """
    A promotion that applies a percentage discount to the total price.
    """

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        if not (0 <= percent <= 100):
            raise ValueError("Percent must be between 0 and 100.")
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        total = product.price * quantity
        discount = total * (self.percent / 100)
        final_price = total - discount
        return round(final_price, 2)


class SecondHalfPrice(Promotion):
    """
    promotion where every second item is half price.
    """

    def __init__(self, name: str = "Second Half Price!"):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        final_price = full_price_items * product.price + half_price_items * (product.price / 2)
        return round(final_price, 2)


class ThirdOneFree(Promotion):
    """
    promotion where every third item is free.
    (Buy 3 get 1 free)
    """

    def __init__(self, name: str = "Third One Free!"):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        paid_items = quantity - (quantity // 3)
        final_price = paid_items * product.price
        return round(final_price, 2)
