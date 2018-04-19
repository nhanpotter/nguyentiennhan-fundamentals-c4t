class Car:
    def __init__(self):
        self.brand1=""
    def setBrand(self):
        self.brand1=input("Brand?")
    def setMaxSpeed(self):
        self.ms= input("Max speed?")
    def printData(self):
        print("Brand: ",self.brand1,"\nMax Speed: ",self.ms,"km/h")
c=Car()
c.setBrand()
c.setMaxSpeed()
c.printData()