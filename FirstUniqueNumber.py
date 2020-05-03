from collections import OrderedDict
class firstNumber:
    def __init__(self,nums):
        self.od = OrderedDict()
        self.s=set()
        for n in nums:
            self.add(n)
    def showFirstUniqueNumber(self):
        if len(self.od)==0: return -1
        else :
            for i in self.od:
                return i
    def add(self,values):
        if values not in self.s:
            self.s.add(values)
            self.od[values]=None
        else:
            self.od.pop(values,None)
nums=[2,3,5]
firstNumber(nums)
firstNumber([7])
firstNumber([])
firstNumber(7)
firstNumber(7)
firstNumber(5)
print(firstNumber().showFirstUniqueNumber())
firstNumber(8)
firstNumber(6)
print(firstNumber().showFirstUniqueNumber())
firstNumber(3)
print(firstNumber().showFirstUniqueNumber())
