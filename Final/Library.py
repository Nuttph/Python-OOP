book = []
borrow = []
class Library:
    def __init__(self,nbook):
        if(nbook not in book):
            book.append(nbook)
        else:
            print('same book!')
    def add(self,nbook):
        if(nbook not in book):
            book.append(nbook)
        else:
            print('same book!')
    def borrow(self,name,nbook1,nbook2=None,nbook3=None,nbook4=None,nbook5=None):
        print(name)
        check = [nbook1,nbook2,nbook3,nbook4,nbook5]
        list_of_borrow = list(filter(lambda x :x!=None,check))
        print(list_of_borrow)
Library = Library('anime')
Library.add('Book')
Library.add('BooA')
Library.borrow('fname','a','b')
print(book)