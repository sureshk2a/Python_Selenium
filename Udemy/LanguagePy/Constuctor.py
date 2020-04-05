class Calculator:
    num = 100
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumer = b
    def add(self):
        print("Sum Value: "+str(self.firstNumber+self.secondNumer))
    def getData(self):
        print("Data retrived")


