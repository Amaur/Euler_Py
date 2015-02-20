import math

class SumSaqureDiff():
    def __init__(self,value):
        self.lastValue = value

    def SumElements(self):
        self.elementSum =0
        for i in range(1,self.lastValue):
            self.elementSum = self.elementSum + i
        return self.elementSum**2

    def SumSquare(self):
        self.squareSum =0
        for i in range(1, self.lastValue):
            self.squareSum = self.squareSum + i**2
        return self.squareSum

    def SumDiff(self):
        return  self.SumElements() - self.SumSquare()


bo = SumSaqureDiff(101)

#bo(10)

print(bo.SumDiff())