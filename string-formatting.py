from string import Template

def main():
    str1 = "you are pplaying game with {0} and {1}".format("mukul" , "neha")
    print(str1)

    tepml = Template("you are pplaying game with ${name1} and ${name2}")
    str2 = tepml.substitute(name1 = "mukul" , name2 = "neha") # this is more readable and also give control , there is no security glitches
    print(str2)


if __name__ == "__main__":
    main()