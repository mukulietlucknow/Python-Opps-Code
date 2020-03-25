class Polygon:

    def __init__(self, width , height):
        self.__width = width
        self.__height = height

    def set_value(self, width , height):
        self.__width = width
        self.__height = height

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width