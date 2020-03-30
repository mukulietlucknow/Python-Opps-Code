class Person:
    def __init__(self):
        self.fname = "mukul"
        self.lname = "varshney"
        self.age = 28

    def __repr__(self):
        return("my name is mukul")



def main():
    cls1 = Person()


    print(str(cls1))
    print(repr(cls1))
    


if __name__ == "__main__":
    main()