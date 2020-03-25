class Polygon:
    __width = None
    __height = None

    def set_value(self, width , height):
        self.__width = width
        self.__height = height

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width


class Square(Polygon):
    def area(self):
        return (self.get_height() * self.get_width())


s1 = Square()
s1.set_value(10,10)
print(s1.area())