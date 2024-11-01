book = []
borrow = [
    {
        'name':'nut',
        'borrow':['1','2']
    },
    ]
mockdata = ['nut','a']
class Library:
    global borrow
    def __init__(self,nbook):
        if(nbook not in book):
            book.append(nbook)
        else:
            print('same book!')
            
    def add(self,nbook):
        for i in nbook:
            if(i not in book):
                book.extend(nbook)
            else:
                print('same book!')
    
    def borrow_book(self,name,nbook):
        obj_name = list(filter(lambda x:x['name']==name,borrow))
        print(f'obj = {obj_name}')
        print(f'borrow = {len(obj_name[0]['borrow'])}')
        if(len(obj_name[0]['borrow']) >= 5):
            print('can not borrow!!')
        elif(len(nbook)+len(obj_name[0]['borrow']) >= 5):
            print('can not borrow')
        else:
            print('borrow')
            obj_name[0]['borrow'].extend(nbook)

library = Library('b1')
library.add(['b2','b3'])
library.add(['b2','b3'])
library.borrow_book('nut',['b3','b4'])
library.borrow_book('nut',['b5','b6'])
print(borrow)
# print("hello world")