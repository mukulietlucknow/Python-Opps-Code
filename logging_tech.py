import logging

extData  = {
    'user' : "mukul_varshney"
}

def main():
    fmt = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s: Line:%(lineno)d %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(level=logging.DEBUG , filename="output.log" , format=fmt, datefmt = datestr)
    logging.debug("mukul varshney" , extra=extData)
    


if __name__ == "__main__":
    main()