class Person:
    def __init__(self,name,empId):
        self.name = name
        self.__empId = empId
    def __str__(self):
        return f'name:{self.name}\nid:{self.__empId}'
    def returnId(self):
        return f'id:{self.__empId}'
p1 = Person('Nutaphon',123456789)
# print(p1)
# print(p1.returnId())

class Spacial(Person):
    def __init__(self,classed):
        self.classed = classed
        super().__init__('Nathan',123456789)
    def returnSId(self):
        return f'ids:{self.__empId}'

s1 = Spacial('312')
print(s1.returnId())