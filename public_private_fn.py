class Example:
    def __init__(self):
        self.x = 10
        self._y = 20
        self.__z = 100

    def public_method(self):
        print(self.x)
        self.__pvt_fn()

    def __pvt_fn(self):
        print("fn invoked")


e = Example()
e.public_method()