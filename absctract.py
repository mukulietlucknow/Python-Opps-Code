from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


    @abstractmethod
    def perimeter(self):
        pass


class Sqaure(Shape):
    def __init__(self,side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return self.__side * 4


square_obj = Sqaure(10)
print(square_obj.area())






