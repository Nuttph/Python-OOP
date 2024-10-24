from abc import abstractmethod, ABC

class Bank(ABC):
    def __init__(self, money):
        self.money = money

    @staticmethod
    def lfMoney(a, b):
        return a.money < b.money

    @abstractmethod
    def abs(self):
        return True

class MyBank(Bank):
    def abs(self):
        return super().abs()  # สามารถ implement เมธอดนี้ตามความต้องการ

if __name__ == "__main__":
    A = MyBank(10)
    B = MyBank(5)
    print(Bank.lfMoney(A, B))  # ผลลัพธ์คือ True เพราะ 10 > 5
    