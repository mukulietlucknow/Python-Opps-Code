def squarefn(x):
    return x**2

def main():
    nums = (1,2,3,4,5,6,7,8,9,10)
    chars = "jhkerbn,ndbaiyiure"
    grades = (87,56,78,89,34)


    #using filter with map function
    squares = list(map(squarefn , nums))
    print(squares)

    # ***** sorted() to sort the list ****



if __name__ == "__main__":
    main()