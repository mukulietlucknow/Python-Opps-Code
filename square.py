from Polygon import Polygon
from shape import Shape

class Square(Polygon , Shape):
    def area(self):
        print(self.get_color())
        return (self.get_height() * self.get_width())
