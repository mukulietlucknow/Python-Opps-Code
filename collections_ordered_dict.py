from collections import OrderedDict

def main():
    sportTeam = [("mukul" , (18,12)),("mukul" , (18,12)),("kumar" , (19,12)),("mukul" , (18,12))]

    sortedTeam = sorted(sportTeam , key = lambda t :t[1][0] , reverse=True)

    teams = OrderedDict(sortedTeam)
    print(teams)
    print(sortedTeam)

    tm , wl = teams.popitem(False)
    print ("pop team : " , tm , wl)

    for i , team in enumerate(teams , start=1):
        print(i , team)
        if i == 4:
            break


    



if __name__ == "__main__":
    main()