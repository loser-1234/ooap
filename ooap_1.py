from abc import ABC, abstractmethod

class Strategy(ABC):
   """
    Интерфейс Стратегии объявляет операции, общие для всех поддерживаемых версий
    некоторого алгоритма.

    Контекст использует этот интерфейс для вызова алгоритма, определённого
    Конкретными Стратегиями.
   """
    @abstractmethod
    def do_algorithm(self, data: str):
        pass

class Context():
    """
    Контекст определяет интерфейс.
    """
    def __init__(self, strategy: Strategy) -> None:

        self._strategy = strategy

    def do_something(self) -> None:
        
        """
        Вместо того, чтобы самостоятельно реализовывать множественные версии
        алгоритма, Контекст делегирует некоторую работу объекту Стратегии.
        """
        
        result = self._strategy.do_algorithm('Какой-то текст')
        print("Печатаем текст")

"""
Конкретные Стратегии реализуют алгоритм, следуя базовому интерфейсу Стратегии.
Этот интерфейс делает их взаимозаменяемыми в Контексте.
"""

class ConcreteStrategyRED(Strategy):
    def do_algorithm(self, data: str) -> str:
        return print("\033[31m {}" .format('data'))

class ConcreteStrategyYELLOW(Strategy):
    def do_algorithm(self, data: str) -> str:
        return print(print("\033[33m {}" .format('data')))
    
class ConcreteStrategyBLUE(Strategy):
    def do_algorithm(self, data: str) -> str:
        return print(print("\033[36m {}" .format('data')))
        
if __name__ == "__main__":

    context = Context(ConcreteStrategyRED())
    context.do_something()
    
    context = Context(ConcreteStrategyBLUE())
    context.do_something()
    
    context = Context(ConcreteStrategyYELLOW())
    context.do_something()
