#Define the Maruthi class

from Define import Car

class Maruthi(Car):
    def steering(self):
        print("Maruthi")

    def breaking(self):
        print(self.reg)

    
m1 = Maruthi(123)
m1.opentack()   
m1.steering()
m1.breaking()