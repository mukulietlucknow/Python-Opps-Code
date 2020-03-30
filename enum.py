from enum import Enum , unique , auto

@unique # for creating the unique enum classes
class Fruit(Enum):
    APPLE = 1
    ORANGE =2
    TOMATO = 4
    BANANA = 3
    PEAR = auto()

def main():
    print(Fruit.APPLE)

    print(Fruit.APPLE.name) # even we can use these as a key
    print(Fruit.APPLE.value)
    print(Fruit.PEAR.value)


if __name__ == "__main__":
    main()