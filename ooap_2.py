from abc import ABC, abstractmethod
class AbstractClass(ABC):


    def template_method(self) -> None:
        """
        Шаблонный метод определяет скелет алгоритма.
        """

        self.base_operation1_catch()
        self.hook1_talk()
        self.required_operations_cooking()
        self.base_operation2_eat()
        self.hook2_look()
        self.base_operation3_sleep()
        

    # Эти операции уже имеют реализации.

    def base_operation1_catch(self) -> None:
        print("Monster catch someone")

    def base_operation2_eat(self) -> None:
        print("Monster eat")

    def base_operation3_sleep(self) -> None:
        print("Monster sleep")

    # А эти операции должны быть реализованы в подклассах.

    @abstractmethod
    def required_operations_cooking(self) -> None:
        pass

    # Это «хуки». Подклассы могут переопределять их, но это необязательно,
    # поскольку у хуков уже есть стандартная (но пустая) реализация.

    def hook1_talk(self) -> None:
        pass

    def hook2_look(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    """
    Определение операций для первого монстра
    """
    def hook1_talk(self) -> None:
        print("Monster talk with someone")
    
    def required_operations_cooking(self) -> None:
        print("Boiling food")


class ConcreteClass2(AbstractClass):
    """
    Определение операций для второго монстра
    """
    def required_operations_cooking(self) -> None:
        if input("Today is ") == 'W':
            print("Grill food")
        else: 
            print("Boiling food")
            
    def hook2_look(self) -> None:
        print("Monster look at window")


def client_code(abstract_class: AbstractClass) -> None:
    """
    Вызывает шаблонный метод для выполнения алгоритма. Не знает конкретный класс объекта, с которым работает
    """
    abstract_class.template_method()


if __name__ == "__main__":

    client_code(ConcreteClass1()) #вызовы для конкретного класса
    print("")

    client_code(ConcreteClass2())
    print("")
