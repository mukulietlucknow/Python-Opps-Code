import collections



def main():
    Point = collections.namedtuple("point" , "x y z")
    p1 = Point(10,20 , 30)
    p1 = p1._replace(x = 100)
    print(p1.x)

    fruits = ["apple","apple","apple", "orange"]

    countList = collections.defaultdict(int) # we can pass indside lambda : 100 the it will start from 100

    for fruit in fruits:
        countList[fruit] += 1

    for k,v in countList.items():
        print(k,v)




if __name__ == "__main__":
    main()