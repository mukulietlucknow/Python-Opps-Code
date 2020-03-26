import itertools

def testFunction(x):
    return x < 30

def main():
    seq1 = ["mukul" , "kumar" , "varshney"]
    cycle1 = itertools.cycle(seq1) # it's an infinite iterator it comes on starting point again
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))


    count1 = itertools.count(100 , 10)  #100 110 120
    print(next(count1))
    print(next(count1))
    print(next(count1))

    vals = [10,20,30,40,50]
    acc = itertools.accumulate(vals)
    print(list(acc))  #[10, 30, 60, 100, 150]  this behaviour can be changed by creating the function

    vals = [10,20,30,40,50 , 40 , 30]
    acc = itertools.accumulate(vals , max)
    print(list(acc))  #[10, 20, 30, 40, 50 , 50 , 50]  this behaviour can be changed by creating the function


    x = itertools.chain("ABCD" , "1234")
    print (list(x)) # it's to chain two sequence together  ['A', 'B', 'C', 'D', '1', '2', '3', '4']

    print(list(itertools.dropwhile(testFunction , vals)))
    print(list(itertools.takewhile(testFunction , vals)))
    # [30, 40, 50, 40, 30]
    # [10, 20]


if __name__ == "__main__":
    main()



