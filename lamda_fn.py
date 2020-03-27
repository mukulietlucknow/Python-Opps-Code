def c2f(temp):
    return (temp*9/5) +32

def f2c(temp):
    return (temp-32)*5/9

def main():
    ctemps = [0,12,34,100]
    ftemps = [32,65,100,212]

    print(list(map(c2f,ctemps))) # normal fns

    print(list(map(lambda t: (t-32)*5/9 , ctemps)))  # lambda function
    



if __name__ == "__main__":
    main()