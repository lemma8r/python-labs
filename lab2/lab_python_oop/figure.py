from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        """Вычисление площади фигуры"""
        pass
