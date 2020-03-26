def main():
    days = ["mon",'tue', 'wed' ,'thurs' ,'fri' ,'sat' ,'sun']


    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))


    #diffrent way of reading file in python it will stop if it will get empty line
    # with open("text.file" , 'r') as fp:
    #     for line in iter(fp.readline() , ''):
    #         print(line)


    # enumerate methode
    for (i,m) in enumerate(days , start = 1):
        print(i,m)


    #zip function 
    for m in zip(days,days):
        print(m)

    for (i,m) in enumerate(zip(days ,days), start = 1):
        print(i,m[0] , "is same as" , m[1])
    
    


if __name__ == "__main__":
    main()