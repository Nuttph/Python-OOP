from abc import abstractmethod,ABC

class Bank(ABC):
    def __init__(self,money):
        self.money = money
    @staticmethod
    def lfMoney(a,b):
        return a.money < b.money
    
    @abstractmethod
    def abs(self):
        return True
    

A = Bank(10)
B = Bank(5)
print(Bank.lfMoney(A,B))