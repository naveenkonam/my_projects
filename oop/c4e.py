class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("sellig price : {}".format(self.__maxprice))

    def setmaxprice(self,price):
        self.__maxprice = price


c = Computer()
c.sell()

#change the price
c.__maxprice = 1000
c.sell()

#using setter function
c.setmaxprice(1100)
c.sell()
