#Define an absract class

from abc import *

class Car(ABC):
    def __init__(self,reg):
        self.reg = reg
        
    def opentack(self):
        print(self.reg)

    @abstractmethod
    def steering(self):
        pass

    @abstractmethod
    def breaking(self):
        pass