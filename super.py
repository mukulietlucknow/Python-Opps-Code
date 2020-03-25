class Parent:
    def __init__(self , name):
        print ("parent __init" , name)

class Parent2:
    def __init__(self , name):
        print ("parent2 __init" , name)

class Child(Parent , Parent2):
    def __init__(self):
        print("child __init")
        super().__init__("mukul")
        Parent2.__init__(self , "varshney")

c1 = Child()
print (Child.__mro__)
