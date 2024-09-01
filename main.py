from modules.Dev import Dev

class Person():
    def __init__(self,name,id):
        n,s = name.split(' ')
        self.name = n
        self.surname = s
        self.id = id
    def __str__(self):
        return f'id:{self.id}\nname : {self.name} {self.surname}'

#person
p1 = Person('Nuttaphon Popardit',1)
# print(p1)

class Student(Person):
    def __init__(self,name,id,number):
        self.__number = number
        super().__init__(name,id)
    def __str__(self):
        return f'id:{self.id}\nname : {self.name} {self.surname}\nnumber:{self.__number}'

s1 = Student('Nuttaphon Popardit',1,2)
print(s1)

d1 = Dev('Software Engineer')
print(d1)