from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        pass