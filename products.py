class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if name.strip() == "":
            raise ValueError("Enter a product name")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")


    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity):
        if quantity < 0:
            raise Exception("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self) -> str:
        return f"{self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"


    def buy(self, quantity) -> float:
        if not self.active:
            raise Exception(f"Product '{self.name}' is not in stock.")
        if quantity <= 0:
            raise Exception("Quantity cannot be negative.")
        if quantity > self.quantity:
            raise Exception(f"Not enough '{self.name}' in stock. Available: {self.quantity}")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price