#Concrete Method
def sleep():
    print("sleeping")
def eat():
    print('eating')

#Abstract Method

def sound():
    pass #override method

##################################

from abc import ABC,abstractmethod

class Myclass(ABC):
    @abstractmethod
    def cal(self,x):
        pass

class sub1(Myclass):
    def cal(self,x):
        print(x*x)

s1 = sub1()
s1.cal(13)

