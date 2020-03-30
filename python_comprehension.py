import logging



def main():
    ctemps = [0,12,34,100]
    odds = [1,3,5,7,9]
    evens = [2,4,6,8]

    oddSqared = [e ** 2 for e in evens if e > 3 and e < 17] 
    print(oddSqared)

    tempDict = {t: (t*9/5)+32 for t in ctemps}
    print(tempDict)

    newTeam = {k:v for team in (tempDict , tempDict) for k,v in team.items()}
    print(newTeam)
    
    


if __name__ == "__main__":
    main()