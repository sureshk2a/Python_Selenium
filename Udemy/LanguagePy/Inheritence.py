from Udemy.LanguagePy.Constuctor import Calculator
class childImp( Calculator):
    num2 = 200
    def __init__(self):
        Calculator.__init__(self,2,3)
    def getCompleteData(self):
        print(self.num+self.num2+self.firstNumber)
obj = childImp()
obj.getCompleteData()