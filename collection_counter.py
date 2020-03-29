from collections import Counter

def main():
    class1 = ["mukul" , "kumar" , "varshney" , "mukul"]

    class2 = ["mukul3" , "kumar3" , "varshney3"]

    c1 = Counter(class1)
    c2 = Counter(class2)

    print(c1["mukul"]) # will give number of mukul 
    print(sum(c1.values()))  # t count all member

    c1.update(c2)
    print(sum(c1.values()))  # will update the existing class and this is mutuable class

    print(c1.most_common(3))
    print(c1)

    c1.subtract(c2)
    print(c1)

    print(c1 & c2)



if __name__ == "__main__":
    main()