from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    Интерфейс Абстрактной Фабрики объявляет набор методов, которые возвращают
    различные абстрактные продукты. Эти продукты называются семейством и связаны
    темой или концепцией высокого уровня. Продукты одного семейства обычно могут
    взаимодействовать между собой. Семейство продуктов может иметь несколько
    вариаций, но продукты одной вариации несовместимы с продуктами другой.
    """
    @abstractmethod
    def create_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_b(self) -> AbstractProductB:
        pass
    
    @abstractmethod
    def create_c(self) -> AbstractProductC:
        pass


class Orcs(AbstractFactory):
    """
    Конкретная Фабрика производит семейство продуктов одной вариации. 
    """

    def create_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_b(self) -> AbstractProductB:
        return ConcreteProductB1()
    
    def create_c(self) -> AbstractProductC:
        return ConcreteProductC1()


class Elvs(AbstractFactory):
    """
    Каждая Конкретная Фабрика имеет соответствующую вариацию продукта.
    """

    def create_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_b(self) -> AbstractProductB:
        return ConcreteProductB2()
    
    def create_c(self) -> AbstractProductC:
        return ConcreteProductC2()


class AbstractProductA(ABC):

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Конкретные продукты создаются соответствующими Конкретными Фабриками.
"""


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "Warlord of orcs."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "Warlord of elvs."


class AbstractProductB(ABC):

    @abstractmethod
    def useful_function_b(self) -> None:
        pass

"""
Конкретные Продукты создаются соответствующими Конкретными Фабриками.
"""


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "General of orcs."


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "General of elvs."

    
class AbstractProductC(ABC):

    @abstractmethod
    def useful_function_c(self) -> None:
        pass
"""
Конкретные Продукты создаются соответствующими Конкретными Фабриками.
"""


class ConcreteProductC1(AbstractProductC):
    def useful_function_c(self) -> str:
        return "Soldiery of orcs."


class ConcreteProductC2(AbstractProductC):
    def useful_function_c(self) -> str:
        return "Soldiery of elvs."


def client_code(factory: AbstractFactory) -> None:
    """
    Работает с фабриками и продуктами только через абстрактные
    типы: Абстрактная Фабрика и Абстрактный Продукт.
    """
    product_a = factory.create_a()
    product_b = factory.create_b()
    product_c = factory.create_c()

    print(f"{product_a.useful_function_a()}")
    print(f"{product_b.useful_function_b()}")
    print(f"{product_c.useful_function_c()}")


if __name__ == "__main__":
    
    print("Orcs:")
    client_code(Orcs())

    print("\n")

    print("Elvs")
    client_code(Elvs())
